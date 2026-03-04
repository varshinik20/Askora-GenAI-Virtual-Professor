let selectedSubject = "General";

function toggleSidebar() {

    const sidebar = document.getElementById("sidebar");

    if (sidebar.style.left === "0px") {
        sidebar.style.left = "-260px";
    } else {
        sidebar.style.left = "0px";
    }

}

/* select subject */

function selectSubject(subject) {

    selectedSubject = subject;

    document.getElementById("selectedSubject").innerText = subject;

    toggleSidebar();

}

/* close sidebar when clicking outside */

document.addEventListener("click", function (event) {

    const sidebar = document.getElementById("sidebar");
    const menuBtn = document.querySelector(".menu-btn");

    const sidebarOpen = sidebar.style.left === "0px";

    if (
        sidebarOpen &&
        !sidebar.contains(event.target) &&
        !menuBtn.contains(event.target)
    ) {
        sidebar.style.left = "-260px";
    }

});


/* ask professor */

function askProfessor() {

    const text = document.getElementById("userInput").value;

    const output = document.getElementById("output");
    const audio = document.getElementById("audioPlayer");
    const video = document.getElementById("professorVideo");

    if (!text.trim()) {
        alert("Enter a topic");
        return;
    }

    output.innerHTML = "Professor is thinking...";

    fetch("/ask", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            subject: selectedSubject,
            text: text
        })

    })

        .then(res => res.json())

        .then(data => {

            const cleanedText = data.text.replace(/\*\*/g, "");

            output.innerText = cleanedText;

            if (data.audio) {

                audio.src = data.audio;

                video.currentTime = 0;

                video.play();

                audio.play();

                audio.onended = () => {

                    video.pause();
                    video.currentTime = 0;

                };

            }

        });

}