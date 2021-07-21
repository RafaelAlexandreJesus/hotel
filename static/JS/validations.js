// função para validação de campos
function numbers() {
    // apenas números no campo
    let key = event.keyCode;
    if (key >= 48 && key <= 57) {
      return true;
    } else {
      return false;
    }
  }
  
  function words() {
    // apenas letras no campo
    let key = event.keyCode;
    if (key >= 48 && key <= 57) {
      return false;
    } else {
      return true;
    }
  }