const qrText = document.getElementById("message");
const generateBtn = document.getElementById("generate-qr");
const downloadBtn = document.createElement('a');
const cleanBtn = document.createElement('button');
const container = document.querySelector('.qr-image-container');

generateBtn.addEventListener("click", function () {
    fetch('/qr-code-generator', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ 'text': qrText.value }),
    })
    .then(res => res.blob())
    .then(blob => {
        const imgURL = URL.createObjectURL(blob);
        let img = new Image();
        img.src = imgURL;

        const p = document.createElement('p')
        p.textContent = 'Your QR Code: ';
        p.className = 'created-text';


        downloadBtn.download = 'qr-code.png'
        downloadBtn.href = imgURL;
        downloadBtn.textContent = 'Download';
        downloadBtn.className = 'btn';

        cleanBtn.textContent = 'Delete';
        cleanBtn.className = 'delete-btn';
        cleanBtn.onclick = function () {
            container.innerHTML = ''
        }

        container.innerHTML = '';

        const div = document.createElement('div');
        div.className = 'qr-container-options';

        container.appendChild(p);
        container.appendChild(img);
        div.appendChild(downloadBtn);
        div.appendChild(cleanBtn);
        container.appendChild(div);

    })
    .catch(error => console.error('Ошибка:', error));
});
