package main

import (
	"fmt"
	
)

func main(){
	display([6]int{1,2,3,4,5})
}

func display(args ...any) {
	for i,v:=range args{
		fmt.Println(i,v)
	}
}
