package main

import (
	"bufio"
	_ "embed"
	"fmt"
	"strings"
)

//go:embed input.txt
var input string

func main() {
	var lines []string
	scanner := bufio.NewScanner(strings.NewReader(input))
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	taskOne(lines)
	taskTwo(lines)
}

func taskTwo(lines []string) {
	var score int
	for i := 0; i < len(lines); i += 3 {
		for _, char := range lines[i] {
			if strings.Contains(lines[i+1], string(char)) &&
				strings.Contains(lines[i+2], string(char)) {
				score += priority(char)
				break
			}
		}
	}
	fmt.Println(score)
}

func taskOne(lines []string) {
	var score int
	for _, line := range lines {
		a := line[0 : len(line)/2]
		b := line[len(line)/2:]

		for _, chari := range a {
			if strings.Contains(b, string(chari)) {
				p := priority(chari)
				score += p
				break
			}
		}
	}
	fmt.Println(score)
}

func priority(char int32) int {
	if 'a' <= char && char <= 'z' {
		return int(1 + char - 'a')
	} else {
		return int(27 + char - 'A')
	}
}
