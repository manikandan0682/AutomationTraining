package main

import (
	"fmt",
	"time",
	"rand"	
)

func main(){
	var now time = time.Now()

	
}
func getuserinput() string
{
	for {
		var s string
		fmt.Println("Enter text: ")
		fmt.Scanln(&s)
		fmt.Println(s)
		if(len(s)==0){
			fmt.Println("done")
			break
		}
	}

}
