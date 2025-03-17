package main

import "fmt"

func swap(first int,second int) (int, int){
	var temp int =0
	temp =first
	first=second
	second=temp
	return first, second


}

func Swap(){
	local1:=10
	local2:=20
	local1, local2 = swap(local1,local2)

	fmt.Println(local1,local2)

}