# Chord Protocol with Distributed Hash Table

# Objective
This project implements a Simplest Chord Protocol to analyse the number of jumps needed to find a specific node. For this implementation the network, P2P-TCP/IP connections, was disregarded.

# Features
There are three different ways to search in P2P network.
- **Sequential** - Do not use DHT, only jump for next node.
- **Single Jump** - Use DHT only on first jump, the next jumps are for next node.
- **Full Jump** - Always use DHT

# Credits
Created by diego.giovanini4@gmail.com

