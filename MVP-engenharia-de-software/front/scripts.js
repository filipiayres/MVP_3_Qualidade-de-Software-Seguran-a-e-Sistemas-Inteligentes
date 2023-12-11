/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/apanhados';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.apanhados.forEach(item => insertList(item.id,
                                                item.age, 
                                                item.gender, 
                                                item.height,
                                                item.weight,
                                                item.ap_hi,
                                                item.ap_lo,
                                                item.cholesterol,
                                                item.gluc,
                                                item.smoke,
                                                item.alco,
                                                item.active,
                                                item.cardio
                                                
                                              ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()




/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputId, inputAge, inputGender, inputHeight,
                        inputWeight, inputAp_hi, inputAp_lo,
                        inputCholesterol, inputGluc,inputSmoke, 
                        inputAlco, inputActive, inputCardio) => {
    
  const formData = new FormData();
  formData.append('id', inputId);
  formData.append('age', inputAge);
  formData.append('gender', inputGender);
  formData.append('height', inputHeight);
  formData.append('weight', inputWeight);
  formData.append('ap_hi', inputAp_hi);
  formData.append('ap_lo', inputAp_lo);
  formData.append('cholesterol', inputCholesterol);
  formData.append('gluc', inputGluc);
  formData.append('smoke', inputSmoke);
  formData.append('alco', inputAlco);
  formData.append('active', inputActive);
  formData.append('cardio', inputCardio);

  let url = 'http://127.0.0.1:5000/apanhado';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const idItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(idItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (id) => {
  console.log(id)
  let url = 'http://127.0.0.1:5000/apanhado?id='+id;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com apanhado 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputId = document.getElementById("newId").value;
  let inputAge = document.getElementById("newAge").value;
  let inputGender = document.getElementById("newGender").value;
  let inputHeight = document.getElementById("newHeight").value;
  let inputWeight = document.getElementById("newWeight").value;
  let inputAp_hi = document.getElementById("newAp_hi").value;
  let inputAp_lo = document.getElementById("newAp_lo").value;
  let inputCholesterol = document.getElementById("newCholesterol").value;
  let inputGluc = document.getElementById("newGluc").value;
  let inputSmoke = document.getElementById("newSmoke").value;
  let inputAlco = document.getElementById("newAlco").value;
  let inputActive = document.getElementById("newActive").value;
  let inputCardio = document.getElementById("newCardio").value;

  // Verifique se o id do produto já existe antes de adicionar
  const checkUrl = `http://127.0.0.1:5000/apanhados?id=${inputId}`;
  fetch(checkUrl, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.apanhados && data.apanhados.some(item => item.name === inputId)) {
        alert("O id já está cadastrado.\nCadastre o apanhado com um id diferente ou atualize o existente.");
      } else if (inputId === '') {
        alert("o id precisa ser preencida");
      } else if (isNaN(inputGender) || isNaN(inputHeight) || isNaN(inputAp_hi) 
      || isNaN(inputAp_lo) || isNaN(inputCholesterol) || isNaN(inputGluc)
      || isNaN(inputSmoke) || isNaN(inputAlco)|| isNaN(inputActive) || isNaN(inputCardio))  
      {
        alert("Esse(s) campo(s) precisam ser números!");
      } else {
        insertList(inputId, inputAge, inputGender, inputHeight, inputWeight, inputAp_hi, inputAp_lo, inputCholesterol, inputGluc,inputSmoke,inputAlco, inputActive, inputCardio );
        postItem(inputId,inputAge, inputGender, inputHeight, inputAp_hi, inputAp_lo, inputCholesterol, inputGluc, inputSmoke, inputAlco, inputActive, inputCardio );
        alert("Item adicionado!");
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista 
  --------------------------------------------------------------------------------------
*/
const insertList = (id, age, gender, height,weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio ) => {
  var item = [id, age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio ];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);


  document.getElementById("newId").value = "";
  document.getElementById("newAge").value = "";
  document.getElementById("newGender").value = "";
  document.getElementById("newHeight").value = "";
  document.getElementById("newWeight").value = "";
  document.getElementById("newAp_hi").value = "";
  document.getElementById("newAp_lo").value = "";
  document.getElementById("newCholesterol").value = "";
  document.getElementById("newGluc").value = "";
  document.getElementById("newSmoke").value = "";
  document.getElementById("newAlco").value = "";
  document.getElementById("newActive").value = "";
  document.getElementById("newCardio").value = "";

  removeElement();
}