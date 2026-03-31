function addMessage(text, sender) {
    let box = document.getElementById("chat-box");

    let div = document.createElement("div");
    div.classList.add("message", sender);
    div.innerText = text;

    box.appendChild(div);
    box.scrollTop = box.scrollHeight;

    return div;
}

// TEXT + IMAGE
async function send() {
    let input = document.getElementById("input");
    let fileInput = document.getElementById("imageInput");

    let text = input.value.trim();
    let file = fileInput.files[0];

    if (!text && !file) return;

    if (text) addMessage(text, "user");
    if (file) addMessage("📷 Image uploaded", "user");

    input.value = "";

    let formData = new FormData();
    if (file) formData.append("file", file);
    if (text) formData.append("question", text);

    try {
        let res = file
            ? await fetch("/image-upload", { method: "POST", body: formData })
            : await fetch("/chat?user_input=" + encodeURIComponent(text), { method: "POST" });

        let data = await res.json();
        addMessage(data.response, "bot");

    } catch (err) {
        addMessage("❌ Server error", "bot");
    }

    removeImage();
}

document.getElementById("input").addEventListener("keydown", e => {
    if (e.key === "Enter") send();
});

// IMAGE PREVIEW
document.getElementById("imageInput").addEventListener("change", function () {
    let file = this.files[0];
    let container = document.getElementById("imagePreviewContainer");

    container.innerHTML = "";

    if (file) {
        let reader = new FileReader();
        reader.onload = e => {
            container.innerHTML = `
                <div class="image-preview">
                    <img src="${e.target.result}" />
                    <span>${file.name}</span>
                    <span class="remove-btn" onclick="removeImage()">✖</span>
                </div>
            `;
        };
        reader.readAsDataURL(file);
    }
});

function removeImage() {
    document.getElementById("imageInput").value = "";
    document.getElementById("imagePreviewContainer").innerHTML = "";
}

// VOICE
let mediaRecorder, audioChunks = [], isRecording = false, timeout;

async function toggleRecording() {
    let btn = document.getElementById("micBtn");

    if (!isRecording) {
        let stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];

        mediaRecorder.start();
        isRecording = true;
        btn.innerText = "⏹ Stop";

        mediaRecorder.ondataavailable = e => audioChunks.push(e.data);

        mediaRecorder.onstop = async () => {
            let blob = new Blob(audioChunks, { type: "audio/wav" });

            let formData = new FormData();
            formData.append("file", blob);

            try {
                let res = await fetch("/audio", { method: "POST", body: formData });
                let data = await res.json();

                addMessage("🎤 " + data.user_text, "user");
                addMessage(data.response_text, "bot");

                if (data.audio_file) {
                    new Audio(data.audio_file).play();
                }

            } catch {
                addMessage("❌ Voice error", "bot");
            }

            btn.innerText = "🎤 Start";
            isRecording = false;
        };

        timeout = setTimeout(() => mediaRecorder.stop(), 300000);

    } else {
        clearTimeout(timeout);
        mediaRecorder.stop();
    }
}