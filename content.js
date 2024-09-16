let token = localStorage.getItem("token");
if (token) {
    chrome.runtime.sendMessage({ action: "sendToken", token: token });
}
