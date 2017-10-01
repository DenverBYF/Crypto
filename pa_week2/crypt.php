<?php 
	/**
	* 
	*/
	class AES
	{
		private $key;
		function __construct($key)
		{
			$this->key = $key;
		}
		public function CBC_decrypt($message)
		{
			$iv = substr($message,0,16);
			$message = substr($message,16);
			$data = mcrypt_decrypt(MCRYPT_RIJNDAEL_128,$this->key,$message,MCRYPT_MODE_CBC,$iv);
			return substr($data,0,-ord($data[strlen($data)-1]));	//abandon padding
		}
		public function CTR_decrypt($message)
		{

		}
	}

	$aes = new AES(hex2bin('140b41b22a29beb4061bda66b6747e14'));
	echo $aes->CBC_decrypt(hex2bin('4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'));