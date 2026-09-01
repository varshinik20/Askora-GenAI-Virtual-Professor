let selectedSubject = "General";
let selectedLanguage = "english";

function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    sidebar.style.left = sidebar.style.left === "0px" ? "-280px" : "0px";
}

function selectSubject(subject) {
    selectedSubject = subject;
    document.getElementById("selectedSubject").innerText = subject;
    toggleSidebar();
}

function updateLanguage() {
    selectedLanguage = document.getElementById("languageSelect").value;
    console.log("Language switched to:", selectedLanguage);
}

document.addEventListener("click", function (event) {
    const sidebar = document.getElementById("sidebar");
    const menuBtn = document.querySelector(".menu-btn");
    const sidebarOpen = sidebar.style.left === "0px";

    if (sidebarOpen && !sidebar.contains(event.target) && !menuBtn.contains(event.target)) {
        sidebar.style.left = "-280px";
    }
});

function setStatus(state) {
    const dot = document.getElementById("statusDot");
    const icon = document.getElementById("speakerIcon");
    
    if (state === "thinking") {
        dot.style.opacity = "1";
        dot.style.background = "#ea8cd8";
        dot.style.animation = "pulse 1.5s infinite";
        icon.style.opacity = "0.4";
    } else if (state === "speaking") {
        dot.style.opacity = "1";
        dot.style.background = "#00ffcc";
        dot.style.animation = "pulse 0.8s infinite";
        icon.style.opacity = "1";
    } else {
        dot.style.opacity = "0";
        dot.style.animation = "none";
        icon.style.opacity = "0.4";
    }
}

// Add CSS pulse animation dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes pulse {
        0% { transform: scale(1); box-shadow: 0 0 10px currentColor; }
        50% { transform: scale(1.4); box-shadow: 0 0 20px currentColor; }
        100% { transform: scale(1); box-shadow: 0 0 10px currentColor; }
    }
`;
document.head.appendChild(style);

function askProfessor() {
    const textInput = document.getElementById("userInput");
    const text = textInput.value;
    const output = document.getElementById("output");
    const video = document.getElementById("professorVideo");

    if (!text.trim()) {
        alert("Enter your question");
        return;
    }

    // 1. UI Status
    output.innerHTML = '<p style="color: #ea8cd8; font-weight: bold;">Professor is thinking...</p>';
    setStatus("thinking");
    video.pause();

    const requestData = {
        subject: selectedSubject,
        language: selectedLanguage,
        text: text
    };

    // 2. Fetch Text & Audio URL
    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestData)
    })
    .then(res => {
        if (!res.ok) throw new Error("Server failed.");
        return res.json();
    })
    .then(data => {
        if (!data.text) throw new Error("No response.");
        
        // 3. Display full text
        const cleanedText = data.text.replace(/\*\*/g, "");
        output.innerHTML = `<p>${cleanedText.replace(/\n/g, '<br>')}</p>`;

        // 4. Play High-speed Neural Audio file
        if (data.audio) {
            console.log("Audio generated:", data.audio);
            const audio = new Audio(data.audio);
            
            audio.onplay = () => {
                setStatus("speaking");
                video.play().catch(e => console.warn("Video blocked:", e));
            };
            
            audio.onended = () => {
                setStatus("idle");
                video.pause();
                video.currentTime = 0;
            };

            audio.onerror = (e) => {
                console.error("Audio error:", e);
                setStatus("idle");
                video.pause();
            };

            audio.play().catch(e => {
                console.error("Playback blocked. Triggered by manual click.", e);
                setStatus("idle");
            });
        } else {
            setStatus("idle");
        }
    })
    .catch(err => {
        console.error("Request error:", err);
        output.innerText = `Error: ${err.message || "Connection failed."}`;
        setStatus("idle");
        video.pause();
    });
}