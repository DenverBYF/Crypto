<?php 
	$t=function($array){
		return array_slice($array,0,count($array)/2)==array_slice($array,count($array)/2)?true:false;
	};
	$a=[1,1,0,0,1];
	$ret=[];
	while (true){ 
		$tmp=$a[4]^$a[1];
		$ret[]=array_pop($a);
		if(count($ret)%2==0){
			if ($t($ret)) {
				break;
			}
		}
		array_unshift($a,$tmp);
	}
	print_r($ret);
	echo "T:  ".count($ret)/2;