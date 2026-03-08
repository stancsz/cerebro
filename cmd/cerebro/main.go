package main

import (
	"context"
	"log"
	"os"
	"os/signal"
	"syscall"

	"github.com/stancsz/cerebro/internal/mcp"
)

func main() {
	log.Println("Starting Cerebro-MCP Core Engine...")

	// Initialize the main context with cancellation
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	// Handle graceful shutdown
	sigChan := make(chan os.Signal, 1)
	signal.Notify(sigChan, os.Interrupt, syscall.SIGTERM)

	go func() {
		<-sigChan
		log.Println("Received termination signal. Executing graceful shutdown...")
		cancel()
	}()

	// Initialize the MCP Server (The Go side of the Polyglot Architecture)
	server := mcp.NewServer()

	// Start the main execution loop
	if err := server.Run(ctx); err != nil {
		log.Fatalf("Cerebro-MCP Core Engine crashed: %v", err)
	}

	log.Println("Cerebro-MCP shut down successfully.")
}
