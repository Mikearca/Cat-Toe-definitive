const buttons = document.querySelectorAll(".ripple")

// Itera sobre cada elemento de la lista de botones.
buttons.forEach(button => {
    button.addEventListener("click", function (e) {
         //obtiene las coordenadas X e Y del click del mouse.
        const x = e.pageX
        const y = e.pageY

        //obtiene la posicion superior e izquierda del boton.
        const buttonTop = e.target.offsetTop
        const buttonLeft = e.target.offsetLeft

        // Calcula la posiciòn interna del click del mouse.
        const xInside = x - buttonLeft
        const yInside = y - buttonTop

        // Crea un elemento span para representar el efecto.
        const circle = document.createElement("span")
        circle.classList.add("circle")
        circle.style.top = yInside + "px"
        circle.style.left = xInside + "px"

        // Añade el elemento span al botòn.
        this.appendChild(circle)

        // Elimina el elemento span despues de 500 mls.
        setTimeout(() => circle.remove(), 500)
    })
})