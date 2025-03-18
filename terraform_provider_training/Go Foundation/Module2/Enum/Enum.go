package main

import "fmt"

const Bold = 1
const Underline = 2
const Italics = 3

const (
	Small  = 0
	Medium = 1
	Large  = 2
	XLarge = 3
)

// const (
// 	Bold = 1 << iota
// 	Underline
// 	Italics
// )

func main() {
	fmt.Println(Bold, Underline, Italics)
}
