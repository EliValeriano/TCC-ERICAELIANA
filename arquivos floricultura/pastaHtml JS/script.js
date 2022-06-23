const botao = document.querySelector
("#botao-carregar");
const tabela = document.querySelector
("#tabela-Floricultura");

botao.addEventListenner("click", function() {
    carregarDados();
  })

  function carregarDados() {
      fetch("http://127.0.0.1:5000/todos")
      .then(function(resposta) {
         return resposta.json()
   })
      .then(function(listaFloricultura) {
        popularTabela(listaFloricultura)
   })
}

function popularTabela(listaFloricultura) {
  const tamanholista = listaCarros.legth;

  for(let index = 0; index < tamanholista; index++) { 
    const linha = document.createElement("tr");

    const id = document.createElement("td");
    const nome = document.createElement("td");
    const preco = document.createElement("td");
    

    id.innerHTML = listaFloricultura[index][0];
    nome.innerHTML = listaFloricultura[index][1];
    preco.innerHTML = listaFloricultura[index][2];
    

    linha.appendChild(id);
    linha.appendChild(nome);
    linha.appendChild(preco);
    tabela.appendChild(linha);
}~
}