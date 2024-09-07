chrome.webRequest.onBeforeRequest.addListener(
    function(details) {
        const blockedWebsites = JSON.parse(localStorage.getItem('blockedWebsites')) || [];
        const urls = blockedWebsites.map(url => `*://*.${url}/*`);
        for (let i = 0; i < urls.length; i++) {
            if (details.url.includes(blockedWebsites[i])) {
                return { cancel: true };
            }
        }
    },
    {urls: ["<all_urls>"]}, // Listen to all URLs
    ["blocking"]
);

