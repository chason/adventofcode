package main

import (
    "os"
    "bufio"
    "fmt"
    "strconv"
)

func sum(inputs []int) int {
    sum := 0
    for _, num := range inputs {
        sum += num
    }
    return sum
}

func contains(m map[int]int, c int) bool {
    _, p := m[c]
    return p
}

func double(inputs []int) int {
    seen := make(map[int]int)
    cv := 0
    for {
        for _, a := range inputs {
            cv += a
            if contains(seen, cv) {
                return cv
            }
            seen[cv] = 1
        }
    }
}

func main() {
    var inputs []int
    fileHandle, _ := os.Open(os.Args[1])
    defer fileHandle.Close()
    fileScanner := bufio.NewScanner(fileHandle)
    for fileScanner.Scan() {
        new_input, _ := strconv.Atoi(fileScanner.Text())
        inputs = append(inputs, new_input)
    }
    fmt.Println("Problem 1: ", sum(inputs))
    fmt.Println("Problem 2: ", double(inputs))
}
