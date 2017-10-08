<?php 

	/**
	* 
	*/
	class AES
	{
		private $key = 'UITN25LMUQC436IM';
		//private $iv = '4ca00ff4c898d61e1edbf1800618fb28';
		function __construct()
		{
			# code...
		}
		public function encrypt($plaintext)
		{

			$module = mcrypt_module_open(MCRYPT_RIJNDAEL_128,'',MCRYPT_MODE_CBC,'');
			//$iv=mcrypt_create_iv(mcrypt_enc_get_iv_size($module));
			mcrypt_generic_init($module,hex2bin($this->key),hex2bin($this->iv));
			$block = mcrypt_get_block_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_CBC);
			$pad = $block - (strlen($plaintext) % $block);
			$plaintext .= str_repeat(chr($pad),$pad);
			$chaintext = mcrypt_generic($module,$plaintext);
			mcrypt_generic_deinit($module);
			mcrypt_module_close($module);
			return $chaintext;
		}
		public function decrypt($chaintext)
		{
			$module = mcrypt_module_open(MCRYPT_RIJNDAEL_128,'',MCRYPT_MODE_CBC,'');
			mcrypt_generic_init($module,hex2bin($this->key),hex2bin($this->iv));
			$plaintext = mcrypt_generic($module,$chaintext);
			mcrypt_generic_deinit($module);
			mcrypt_module_close($module);
			return $plaintext;
		}
	}

	/*$aes = new AES();
	$ret=$aes->encrypt('this is a string will be AES_Encrypt');
	//echo bin2hex($ret);
	echo bin2hex($ret);
	//echo $aes->decrypt(hex2bin('28a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'));
*/

class CryptAES
{
    protected $cipher = MCRYPT_RIJNDAEL_128;
    protected $mode = MCRYPT_MODE_ECB;
    protected $pad_method = NULL;
    protected $secret_key = '';
    protected $iv = '';
 
    public function set_cipher($cipher)
    {
        $this->cipher = $cipher;
    }
 
    public function set_mode($mode)
    {
        $this->mode = $mode;
    }
 
    public function set_iv($iv)
    {
        $this->iv = $iv;
    }
 
    public function set_key($key)
    {
        $this->secret_key = $key;
    }
 
    public function require_pkcs5()
    {
        $this->pad_method = 'pkcs5';
    }
 
    protected function pad_or_unpad($str, $ext)
    {
        if ( is_null($this->pad_method) )
        {
            return $str;
        }
        else
        {
            $func_name = __CLASS__ . '::' . $this->pad_method . '_' . $ext . 'pad';
            if ( is_callable($func_name) )
            {
                $size = mcrypt_get_block_size($this->cipher, $this->mode);
                return call_user_func($func_name, $str, $size);
            }
        }
        return $str;
    }
 
    protected function pad($str)
    {
        return $this->pad_or_unpad($str, '');
    }
 
    protected function unpad($str)
    {
        return $this->pad_or_unpad($str, 'un');
    }
 
    public function encrypt($str)
    {
        $str = $this->pad($str);
        $td = mcrypt_module_open($this->cipher, '', $this->mode, '');
 
        if ( empty($this->iv) )
        {
            $iv = @mcrypt_create_iv(mcrypt_enc_get_iv_size($td), MCRYPT_RAND);
        }
        else
        {
            $iv = $this->iv;
        }
 
        mcrypt_generic_init($td, $this->secret_key, $iv);
        $cyper_text = mcrypt_generic($td, $str);
        $rt=base64_encode($cyper_text);
        //$rt = bin2hex($cyper_text);
        mcrypt_generic_deinit($td);
        mcrypt_module_close($td);
 
        return $rt;
    }
 
    public function decrypt($str){
        $td = mcrypt_module_open($this->cipher, '', $this->mode, '');
 
        if ( empty($this->iv) )
        {
            $iv = @mcrypt_create_iv(mcrypt_enc_get_iv_size($td), MCRYPT_RAND);
        }
        else
        {
            $iv = $this->iv;
        }
 
        mcrypt_generic_init($td, $this->secret_key, $iv);
        //$decrypted_text = mdecrypt_generic($td, self::hex2bin($str));
        $decrypted_text = mdecrypt_generic($td, base64_decode($str));
        $rt = $decrypted_text;
        mcrypt_generic_deinit($td);
        mcrypt_module_close($td);
 
        return $this->unpad($rt);
    }
 
    public static function pkcs5_pad($text, $blocksize)
    {
        $pad = $blocksize - (strlen($text) % $blocksize);
        return $text . str_repeat(chr($pad), $pad);
    }
 
    public static function pkcs5_unpad($text)
    {
        $pad = ord($text{strlen($text) - 1});
        if ($pad > strlen($text)) return false;
        if (strspn($text, chr($pad), strlen($text) - $pad) != $pad) return false;
        return substr($text, 0, -1 * $pad);
    }
}
 
$keyStr = 'UITN25LMUQC436IM';
$plainText = 'this is a string will be AES_Encrypt';
 
$aes = new CryptAES();
$aes->set_key($keyStr);
$aes->require_pkcs5();
$encText = $aes->encrypt($plainText);
$decString = $aes->decrypt($encText);
 
echo $encText,"n",$decString;
