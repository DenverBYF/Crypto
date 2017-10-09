<?php 

class CryptAES
{
    protected $cipher = MCRYPT_RIJNDAEL_128;
    protected $mode = MCRYPT_MODE_CBC;
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

/**
* 
*/
class cbc_byte_flipping_attack 
{
    protected $ct1;
    protected $ct2;
    protected $pt;
    protected $block_size;
    function __construct($ct1,$ct2,$pt,$block_size)
    {
        $this->ct1 = $ct1;
        $this->ct2 = $ct2;
        $this->pt = $pt;
        $this->block_size = $block_size;
    }
    public function find_diff()
    {
        $ct1_array = str_split($this->ct1,1);
        $ct2_array = str_split($this->ct2,1);
        $diff=[];
        for ($i=16; $i < count($ct1_array) ; $i++) { 
            if($ct1_array[$i] != $ct2_array[$i]){
                $diff[$i] = [$ct1_array[$i],$ct2_array[$i]]; 
            }
        }
        if(empty($diff)){
            die('no diff');
        }
        return $diff;
    }
    public function divmod($num1,$num2)
    {
        return [intval($num1/$num2),$num1%$num2];
    }
    public function attack()
    {
        $diff = $this->find_diff();
        foreach ($diff as $key => $value) {
            $mod = $this->divmod($key,$this->block_size);
            $sp = ($mod[0]-1)*$this->block_size+$mod[1];
            $this->pt[$sp] = chr(ord($this->pt[$sp]) ^ ord($value[0]) ^ ord($value[1]));
        }
        return $this->pt;
    }
}
