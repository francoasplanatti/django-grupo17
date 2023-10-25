
const formulario = document.getElementById("formulario");

if(formulario){
    formulario.addEventListener("submit", (event) =>{
        event.preventDefault()
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: 'Registro Exitoso',
            showConfirmButton: false,
            timer: 2500,
            timerProgressBar: true
        })
        formulario.reset()
    })
}
