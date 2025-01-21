<?php
include 'conexao.php';

//Faz validação do método de requisição e recebe os dados.
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST["nome"];
    $email = $_POST["email"];
    $pergunta1 = $_POST ["p1"];
    $pergunta2 = $_POST ["p2"];
    $pergunta3 = $_POST ["p3"];

//Insere os dados na tabela 
    $sql = "INSERT INTO tb_projetore4 (nome, email, p1, p2, p3) VALUES ('$nome', '$email', '$pergunta1','$pergunta2','$pergunta3')";

    if ($conn->query($sql) === TRUE) {
        header("Location: http://localhost:8080/projeto_re4_v2/index.html?success=true");
        exit(); 

    } else {
        echo "Erro ao enviar" . $conn->error;
    }
}