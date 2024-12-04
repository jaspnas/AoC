package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func check_decrease(input []int, idx int) bool {
	if idx+1 == len(input) {
		return true
	}
	if input[idx]-input[idx+1] <= 3 && input[idx]-input[idx+1] > 0 {
		return check_decrease(input, idx+1)
	}
	return false
}

func check_increase(input []int, idx int) bool {
	if idx+1 == len(input) {
		return true
	}
	if input[idx]-input[idx+1] >= -3 && input[idx]-input[idx+1] < 0 {
		return check_increase(input, idx+1)
	}
	return false
}

func main() {
	// 1. Read input
	input, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	lines := strings.Split(string(input), "\n")

	safe := 0

	for _, line := range lines {
		linedata := []int{}
		numbers := strings.Split(line, " ")
		for _, number := range numbers {
			conv, _ := strconv.Atoi(number)
			linedata = append(linedata, conv)
		}
		if len(linedata) < 2 {
			continue
		}
		if check_decrease(linedata, 0) || check_increase(linedata, 0) {
			safe++
		}
	}

	fmt.Println(safe)
}
