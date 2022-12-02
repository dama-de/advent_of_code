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
	var games [][]int

	scanner := bufio.NewScanner(strings.NewReader(input))
	for scanner.Scan() {
		l := scanner.Text()
		game := make([]int, 2)
		game[0] = int(l[0]) - 'A'
		game[1] = int(l[2]) - 'X'
		games = append(games, game)
	}

	taskOne(games)
	taskTwo(games)
}

func taskOne(games [][]int) {
	var points int
	for _, game := range games {
		p1, p2 := game[0], game[1]
		result := p1 - p2

		points += p2 + 1

		switch result {
		case -2, 1: // loss
			points += 0
		case 2, -1: // win
			points += 6
		case 0: // draw
			points += 3
		}
	}
	fmt.Println(points)
}

func taskTwo(games [][]int) {
	var points int
	for _, game := range games {
		p1, result := game[0], game[1]

		offset := result + 2
		p2 := (p1 + offset) % 3

		points += p2 + 1 + result*3
	}
	fmt.Println(points)
}
