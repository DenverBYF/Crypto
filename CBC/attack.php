<?php 
	require_once('aes.php');
	$ct1 = $_POST['ct1'];
	$ct2 = $_POST['ct2'];
	$enc = base64_decode($_POST['pt']);
	$cbc = new cbc_byte_flipping_attack($ct1,$ct2,$enc,16);
	var_dump($cbc->find_diff());
	var_dump(base64_encode($cbc->attack())); 
