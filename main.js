chrome.webRequest.onBeforeRequest.addListener(
    function(details) { return { cancel: true }},
    {urls:["*://*.facebook.com/*"]}, // Add your url here in this format *://*.YOUR_URL.com/* //
    ["blocking"]
)