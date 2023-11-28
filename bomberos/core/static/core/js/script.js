// Mensaje éxito

const formulario = document.getElementById("formulario");

if(formulario){
    formulario.addEventListener("submit", (event) =>{
        event.preventDefault()
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: 'Enviado con éxito',
            showConfirmButton: false,
            timer: 2500,
            timerProgressBar: true,
            width: 600,
            padding: '3em',
        })
        formulario.reset()
    })
}