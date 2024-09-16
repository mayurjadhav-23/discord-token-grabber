chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "sendToken") {
        fetch("http://localhost:5000/storeToken", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ token: request.token })
        }).then(response => response.json()).then(data => {
            console.log("Token sent to server");
        });
    }
});
