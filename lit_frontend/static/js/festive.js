document.addEventListener("DOMContentLoaded", function () {

    const openButtons = document.querySelectorAll(
        "[data-festive-open]"
    );

    const closeButtons = document.querySelectorAll(
        "[data-festive-close]"
    );

    const dialogs = document.querySelectorAll(
        ".festive-dialog"
    );


    // Open flyer or video popup

    openButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const dialogId = button.getAttribute(
                "data-festive-open"
            );

            const dialog = document.getElementById(dialogId);

            if (dialog && !dialog.open) {

                dialog.showModal();

            }

        });

    });


    // Close popup

    closeButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const dialog = button.closest("dialog");

            if (dialog) {

                dialog.close();

            }

        });

    });


    dialogs.forEach(function (dialog) {

        // Close when clicking outside the popup

        dialog.addEventListener("click", function (event) {

            if (event.target === dialog) {

                const rect = dialog.getBoundingClientRect();

                const outside =
                    event.clientX < rect.left ||
                    event.clientX > rect.right ||
                    event.clientY < rect.top ||
                    event.clientY > rect.bottom;

                if (outside) {

                    dialog.close();

                }

            }

        });


        // Stop video when popup is closed

        dialog.addEventListener("close", function () {

            const video = dialog.querySelector("video");

            if (video) {

                video.pause();

            }

        });

    });

});