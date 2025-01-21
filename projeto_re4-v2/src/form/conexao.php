<?php
//Estabelece os parâmetros de conexão com o servidor e de acesso ao banco de dados.
$servername = "127.0.0.1";
$username = "root";
$password = "usbw";
$dbname = "cadastro_contas";

$conn = new mysqli($servername, $username, $password, $dbname);

//Mensagem de erro.
if ($conn->connect_error) {
    die("A conexão falhou. Tente novamente." . $conn->connect_error);
}