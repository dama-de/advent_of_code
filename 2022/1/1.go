package main

import (
	"bufio"
	_ "embed"
	"fmt"
	"log"
	"sort"
	"strconv"
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

	var buckets []int
	current := 0
	for _, l := range lines {
		if l == "" {
			buckets = append(buckets, current)
			current = 0
		} else {
			n, err := strconv.Atoi(l)
			if err != nil {
				log.Fatal(err)
			}
			current += n
		}
	}

	sort.Sort(sort.Reverse(sort.IntSlice(buckets)))

	fmt.Println(buckets[0])

	fmt.Println(buckets[0] + buckets[1] + buckets[2])
}
