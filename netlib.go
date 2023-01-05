package main

import (
	"fmt"
	"net"
)

func sendMessage(message string, address string) error {
	conn, err := net.Dial("tcp", address)
	if err != nil {
		return err
	}
	defer conn.Close()

	fmt.Fprintln(conn, message)
	return nil
}

func main() {
	err := sendMessage("Hello, World!", "localhost:8080")
	if err != nil {
		fmt.Println(err)
	}
}
