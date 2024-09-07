document.addEventListener('DOMContentLoaded', function() {
    const blockBtn = document.getElementById('block-btn');
    const urlInput = document.getElementById('url-input');
    const blockedList = document.getElementById('blocked-list');

    // Load blocked websites from localStorage and display them
    let blockedWebsites = JSON.parse(localStorage.getItem('blockedWebsites')) || [];
    blockedWebsites.forEach(url => addToList(url));

    blockBtn.addEventListener('click', function() {
        const url = urlInput.value.trim();
        if (url && !blockedWebsites.includes(url)) {
            blockedWebsites.push(url);
            localStorage.setItem('blockedWebsites', JSON.stringify(blockedWebsites));
            addToList(url);
            urlInput.value = '';
        }
    });

    function addToList(url) {
        const li = document.createElement('li');
        li.textContent = url;

        const removeBtn = document.createElement('button');
        removeBtn.textContent = "Remove";
        removeBtn.className = "remove-btn";

        removeBtn.addEventListener('click', function() {
            blockedWebsites = blockedWebsites.filter(item => item !== url);
            localStorage.setItem('blockedWebsites', JSON.stringify(blockedWebsites));
            blockedList.removeChild(li);
        });

        li.appendChild(removeBtn);
        blockedList.appendChild(li);
    }
});


