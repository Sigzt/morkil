document.addEventListener("DOMContentLoaded", function () {
    const registerButton = document.getElementById("registerButton");
    const registrationSection = document.getElementById("registrationSection");
    const playerNameInput = document.getElementById("playerNameInput");
    const submitPlayerButton = document.getElementById("submitPlayerButton");
    const playersButton = document.getElementById("playersButton");
    const playerList = document.getElementById("playerList");
    const messageCard = document.getElementById("messageCard");
    const nextPhraseButton = document.getElementById("nextPhraseButton");
    const gameModeButton = document.getElementById("gameModeButton");
    const gameModeMenu = document.getElementById("gameModeMenu");

    let players = [];
    let messages = ["Mensaje 1", "Mensaje 2", "Mensaje 3"];
    let messageIndex = 0;

    submitPlayerButton.addEventListener("click", function () {
        const playerName = playerNameInput.value;
        if (playerName) {
            players.push(playerName);
            playerNameInput.value = "";
            updatePlayerList();
        }
    });

    playersButton.addEventListener("click", function () {
        updatePlayerList();
    });

    nextPhraseButton.addEventListener("click", function () {
        if (messageIndex < messages.length - 1) {
            messageIndex++;
        } else {
            messageIndex = 0;
        }
        showMessage(messages[messageIndex]);
    });

    gameModeButton.addEventListener("click", function () {
        gameModeMenu.style.display = gameModeMenu.style.display === "block" ? "none" : "block";
    });

    function updatePlayerList() {
        playerList.innerHTML = "";
        players.forEach(player => {
            const li = document.createElement("li");
            li.textContent = player;
            playerList.appendChild(li);
        });
    }

    function showMessage(message) {
        messageCard.textContent = message;
    }
});