package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func check_decrease(input []int, idx int, bad_blocks int) bool {
	if idx+1 >= len(input) {
		return true
	} else if input[idx]-input[idx+1] <= 3 && input[idx]-input[idx+1] > 0 {
		return check_decrease(input, idx+1, bad_blocks)
	} else if bad_blocks == 0 {
		if idx == 0 && check_decrease(input, idx+1, 1) {
			return true
		}
		inputCopy := make([]int, len(input))
		copy(inputCopy, input)
		newList2 := append(input[:idx], input[idx+1:]...)
		newList := append(inputCopy[:idx+1], inputCopy[idx+2:]...)
		fmt.Println(newList)
		fmt.Println(newList2)
		return check_decrease(newList, 0, 1) || check_decrease(newList2, 0, 1)
	}
	return false
}

func check_increase(input []int, idx int, bad_blocks int) bool {
	if idx+1 >= len(input) {
		return true
	} else if input[idx]-input[idx+1] >= -3 && input[idx]-input[idx+1] < 0 {
		return check_increase(input, idx+1, bad_blocks)
	} else if bad_blocks == 0 {
		if idx == 0 && check_increase(input, idx+1, 1) {
			return true
		}
		inputCopy := make([]int, len(input))
		copy(inputCopy, input)
		newList2 := append(input[:idx], input[idx+1:]...)
		newList := append(inputCopy[:idx+1], inputCopy[idx+2:]...)
		fmt.Println(newList)
		fmt.Println(newList2)
		return check_increase(newList, 0, 1) || check_increase(newList2, 0, 1)
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
		fmt.Println(linedata)
		linedatacopy := make([]int, len(linedata))
		copy(linedatacopy, linedata)
		if check_decrease(linedata, 0, 0) || check_increase(linedatacopy, 0, 0) {
			fmt.Println("safe")
			safe++
		} else {
			fmt.Println("unsafe")
		}
	}

	fmt.Println(safe)
}
