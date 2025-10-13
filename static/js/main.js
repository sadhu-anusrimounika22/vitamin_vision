document.addEventListener("DOMContentLoaded", function() {
  const fileInput = document.querySelector("input[type='file']");
  const fileLabel = document.createElement("p");
  if (fileInput) {
    fileInput.after(fileLabel);
    fileInput.addEventListener("change", () => {
      const fileName = fileInput.files.length ? fileInput.files[0].name : "No file chosen";
      fileLabel.innerText = "Selected: " + fileName;
      fileLabel.style.color = "#0071e3";
      fileLabel.style.fontWeight = "500";
    });
  }
});
