function generate_link () {
    fetch('/url_shortener', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ 'user_link': addProtocol(document.getElementById("short-link-input").value)}),
    })
    .then(res => res.text())
    .then(text => {
        document.getElementById('view-field-text').textContent = text;
        document.getElementById('generated-links').classList.remove('hidden');
    })
}

function addProtocol(url) {
    if (!/^https?:\/\//i.test(url)) {
        return 'https://' + url;
    }
    return url;
}

document.getElementById('copy-to-clipboard').addEventListener('click', function(e) {
    const viewURL = document.getElementById('view-field-text');

    if (viewURL.textContent === 'Copied!') {
        return;
    }

    const viewURLAddress = viewURL.textContent;
    navigator.clipboard.writeText(viewURLAddress);
    viewURL.textContent = 'Copied!';

    setTimeout(function () { viewURL.textContent = viewURLAddress }, 2000);
});
