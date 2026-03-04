function askProfessor() {
    const text = document.getElementById("userInput").value;
    const output = document.getElementById("output");
    const audio = document.getElementById("audioPlayer");
    const video = document.getElementById("professorVideo");

    if (!text.trim()) {
        alert("Please enter a topic!");
        return;
    }

    output.innerHTML = "✨ Professor is thinking...";

    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    })
        .then(res => res.json())
        .then(data => {
            output.innerText = data.text;

            if (data.audio) {
                audio.src = data.audio;
                audio.playbackRate = 1.25;  // 🔥 speed up voice

                video.currentTime = 0;
                video.play();
                audio.play();

                audio.onended = () => {
                    video.pause();
                    video.currentTime = 0;
                };
            }
        })
        .catch(() => {
            output.innerText = "Something went wrong.";
        });
}