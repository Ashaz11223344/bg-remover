const dropArea = document.getElementById("drop-area");
const fileInput = document.getElementById("fileInput");
const previewBox = document.getElementById("preview-box");
const previewImg = document.getElementById("preview-img");
const uploadText = document.getElementById("upload-text");

dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.style.borderColor = "black";
});

dropArea.addEventListener("dragleave", () => {
    dropArea.style.borderColor = "#999";
});

dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    fileInput.files = e.dataTransfer.files;
    showPreview(fileInput.files[0]);
    dropArea.style.borderColor = "#999";
});

fileInput.addEventListener("change", () => {
    showPreview(fileInput.files[0]);
});

function showPreview(file) {
    if (!file) return;

    const reader = new FileReader();
    reader.onload = () => {
        previewImg.src = reader.result;
        previewBox.style.display = "block";
        uploadText.innerText = "Image selected";
    };
    reader.readAsDataURL(file);
}
