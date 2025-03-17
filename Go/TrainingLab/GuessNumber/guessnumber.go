package main

import (
	"fmt";
	"time";
	"math/rand";
	"strconv"
	
)

func main(){
	now:= time.Now()
	fmt.Println(now)
	input := get_user_input()
	

	value,_ := strconv.Atoi(input)
	random_number:=generate_random_number(now)

	if value == random_number {
		fmt.Println("You got it", input)
	} else {
		fmt.Println("Wrong guess", input)
		fmt.Println("generated number",random_number)
	}

}

func generate_random_number(now time.Time) int {
	seed := rand.NewSource(int64(now.Second()))
	generator := rand.New(seed)
	return generator.Intn(5) + 1 

}
func get_user_input() string {
	var final_str string
	for {
		var s string
		fmt.Println("Enter text: ")
		fmt.Scanln(&s)
		if len(s)== 0 {
			fmt.Println("done")
			break
		}
		final_str = final_str + s
	}
	return final_str
}
