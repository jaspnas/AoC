package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func part1() {
	// 1. Read input
	input, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	re := regexp.MustCompile(`mul\((\d+),\s*(\d+)\)`)

	sum := 0

	for _, match := range re.FindAllStringSubmatch(string(input), -1) {
		token1, _ := strconv.Atoi(match[1])
		token2, _ := strconv.Atoi(match[2])

		sum += token1 * token2
	}

	fmt.Println("Part1: ", sum)
}

func part2() {
	// 1. Read input
	input, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	re := regexp.MustCompile(`(do\(\)|don't\(\))`)
	reMul := regexp.MustCompile(`mul\((\d+),\s*(\d+)\)`)

	parts := re.Split(string(input), -1)
	delimiters := re.FindAllString(string(input), -1)

	result := make([]string, 0, len(parts)+len(delimiters))

	sum := 0
	for i, part := range parts {
		if i < len(delimiters)+1 && i > 0 {
			result = append(result, delimiters[i-1]+part)
		} else {
			result = append(result, part)
		}
	}

	for _, part := range result {
		if strings.Contains(part, "don't()") {
			continue
		}
		for _, match := range reMul.FindAllStringSubmatch(string(part), -1) {
			token1, _ := strconv.Atoi(match[1])
			token2, _ := strconv.Atoi(match[2])

			sum += token1 * token2
		}
	}

	fmt.Println("Part2: ", sum)
}

func main() {

	part1()

	part2()
}
