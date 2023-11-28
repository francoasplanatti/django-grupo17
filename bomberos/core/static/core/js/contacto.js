// Formulario de contacto

document.addEventListener("DOMContentLoaded", function () {
    const subjectInput = document.querySelector(".contact__input");
    const messageTextarea = document.querySelector("textarea.contact__input");
    const sendButton = document.querySelector(".submit-btn a.button");
    sendButton.addEventListener("click", function (event) {
        event.preventDefault();
        const subject = encodeURIComponent(subjectInput.value);
        const message = encodeURIComponent(messageTextarea.value);
        const email = "francoasplanatti@gmail.com";
        const url = `https://mail.google.com/mail/u/0/?fs=1&to=${email}&su=${subject}&body=${message}&tf=cm`;
        window.location.href = url;
    });
});