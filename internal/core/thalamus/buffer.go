package thalamus

import (
	"context"
	"log"
)

// Buffer represents the Massively Parallel Thalamic Buffer
// Responsible for Multimodal Data Ingestion
type Buffer struct {
	// channels for concurrent ingestion
	textStreams  chan string
	visualStream chan []byte // bytes representing images
	audioStream  chan []byte // bytes representing chunked audio
}

func NewBuffer() *Buffer {
	return &Buffer{
		textStreams:  make(chan string, 10000), // Buffer size maps to concurrency required
		visualStream: make(chan []byte, 100),
		audioStream:  make(chan []byte, 500),
	}
}

// StartIngestion spins up the background routines for parsing telemetry
func (b *Buffer) StartIngestion(ctx context.Context) {
	log.Println("Thalamic Buffer: Starting concurrent multimodal ingestion nodes...")

	// 1. Start Textual (ASTs, Logs) Workers
	for i := 0; i < 50; i++ {
		go b.textworker(ctx, i)
	}

	// 2. Start Visual/Audio Handoff Workers (To Python Sidecar)
	go b.multimodalWorker(ctx)
}

func (b *Buffer) textworker(ctx context.Context, id int) {
	for {
		select {
		case <-ctx.Done():
			return
		case data := <-b.textStreams:
			_ = data // Ingest logic (Heuristic filtration to occur here)
			// log.Printf("Worker %d ingested text stream", id)
		}
	}
}

func (b *Buffer) multimodalWorker(ctx context.Context) {
	for {
		select {
		case <-ctx.Done():
			return
		case img := <-b.visualStream:
			_ = img // Pipe via gRPC to python Sidecar
		case audio := <-b.audioStream:
			_ = audio // Pipe via gRPC to python Sidecar
		}
	}
}
