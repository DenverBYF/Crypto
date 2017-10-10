<?php

	//error_reporting(0);
	require_once('aes.php');
	$aes = new CryptAES();
	$plainText = '2016niandiqijiequanguowangluoanquandasai0123456789abcdef-->xdctfxdnum=2015auid=4;xdctfxdctf'; 
	$aes->set_key('1234567812345678');
	$aes->set_iv('0102030405060708');
	$aes->require_pkcs5();
	$encText = $aes->encrypt($plainText);
	$cookieData = isset($_COOKIE['user'])?$_COOKIE['user']:$encText;
	$decString = $aes->decrypt($cookieData);
	$user = isset($_COOKIE['user'])?$decString:$plainText;
	$num1 = substr($user,strpos($user,"uid")+4,1);
	$num2 = substr($user,strpos($user,"num")+4,4);
	echo '</br><h3>ID: '.$num1."</h3><br>";
	if ($num1 == 1  && $num2 == 2016){
	    die ("假装有flag");
	}
	else{
	    echo "HELLO CLIENT";
	}
	setcookie('user',$encText);
