document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("predict-form");
    const loadingText = document.getElementById("loading");
    const predictBtn = document.getElementById("predict-btn");

    form.addEventListener("submit", function () {
        // Show loading text and disable button
        loadingText.classList.remove("hidden");
        predictBtn.disabled = true;
        predictBtn.textContent = "Predicting...";
    });
});
