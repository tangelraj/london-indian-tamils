document.addEventListener("DOMContentLoaded", function () {

    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");

    if (menuToggle && navLinks) {

        menuToggle.addEventListener("click", function () {

            navLinks.classList.toggle("show");

            const isOpen = navLinks.classList.contains("show");

            menuToggle.setAttribute("aria-expanded", isOpen);

            menuToggle.innerHTML = isOpen
                ? '<i class="fa-solid fa-xmark"></i>'
                : '<i class="fa-solid fa-bars"></i>';

        });

    }

    document.querySelectorAll(".nav-links a").forEach(link => {

        link.addEventListener("click", function () {

            document.querySelectorAll(".nav-links a").forEach(item => {
                item.classList.remove("active");
            });

            this.classList.add("active");

            navLinks.classList.remove("show");

            menuToggle.setAttribute("aria-expanded", "false");

            menuToggle.innerHTML =
                '<i class="fa-solid fa-bars"></i>';

        });

    });

});
// Floating button background colours from Django Admin

document.addEventListener("DOMContentLoaded", function () {

    const floatingButtons = document.querySelectorAll(
        ".floating-btn"
    );

    floatingButtons.forEach(function (button) {

        const backgroundColor = button.dataset.bgColor;

        if (backgroundColor) {
            button.style.backgroundColor = backgroundColor;
        }

    });

});