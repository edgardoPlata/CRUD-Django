(function () {
  const btnEliminaciones = document.querySelectorAll(".btnEliminacion");

  btnEliminaciones.forEach((btnx) => {
    btnx.addEventListener("click", (e) => {
      const confirmacion = confirm("Seguro de eliminar el curso");
      if (!confirmacion) {
        e.preventDefault();
      }
    });
  });
})();
