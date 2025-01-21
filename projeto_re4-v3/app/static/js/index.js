/*Seleciona todos os elementos com as classes "botao" e "personagem", respectivamente, e armazena em variáveis. */
const botoes = document.querySelectorAll(".botao");
const personagens = document.querySelectorAll(".personagem");

/*Itera sobre todos os botões selecionados e adiciona um event listener para cada um. Quando um botão é clicado, ele executa a função que seleciona o botão e o personagem correspondente.*/
botoes.forEach((botao, indice) => {
	botao.addEventListener("click", () => {
		desselecionarBotao();
		desselecionarPersonagem();

		botao.classList.add("selecionado");
		personagens[indice].classList.add("selecionado");
	});
});

/*Removem a classe 'selecionado' dos elementos atualmente selecionados (se houver) para desmarcá-los.*/
function desselecionarPersonagem() {
	const personagemSelecionado = document.querySelector(".personagem.selecionado");
	personagemSelecionado.classList.remove("selecionado");
}

function desselecionarBotao() {
	const botaoSelecionado = document.querySelector(".botao.selecionado");
	botaoSelecionado.classList.remove("selecionado");
}
