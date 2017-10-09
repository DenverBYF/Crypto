<?php

	//error_reporting(0);
	require_once('aes.php');
	$aes = new CryptAES();
	$plainText = '2016niandiqijiequanguowangluoanquandasai0123456789abcdef-->xdctfxdnum=2015auid=4;xdctfxdctf'; 
	$aes->set_key('1234567812345678');
	$aes->set_iv('0102030405060708');
	$aes->require_pkcs5();
	$encText = $aes->encrypt($plainText);
	echo $encText."\n";
	$cookieData = isset($_COOKIE['user'])?$_COOKIE['user']:$encText;
	//$cookieData = 'ovuXT5DVfRptULIRlUwX8aMvnu7I+DVYrz1njfntKYPtTguqn2Xw/Bc74F/cM1YVgsoE2lEPMUtad6UVuuN0Bw4XOpd2gE0hTc5xuFawSIvz3U98Lzoc+xJ0Ox+118OO';
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
