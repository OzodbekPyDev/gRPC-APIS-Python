# gRPC Greeting Service

This project implements a simple gRPC service for greeting users. The service includes various types of RPC (Remote Procedure Call) methods: unary, server-side streaming, client-side streaming, and bidirectional streaming.

## Features

The gRPC service implements the following types of calls:

1. **Unary**: The client sends a single request and receives a single response.
2. **Server Streaming**: The client sends a single request and receives a stream of responses.
3. **Client Streaming**: The client sends a stream of requests and receives a single response.
4. **Bidirectional Streaming**: Both the client and server exchange streams of data simultaneously.

### Proto File Overview

The `greet.proto` file defines the service and message types for this project. It includes:

- **Greeter Service**: Handles the greeting logic.
- **HelloRequest**: Message for sending a request containing the name and greeting.
- **HelloReply**: Message for the server's response.
- **DelayedReply**: Used for client-side streaming, containing a list of received requests.

### Service Methods

- **SayHello (Unary)**: A simple RPC where the client sends a name and gets a greeting.
- **ParrotSaysHello (Server Streaming)**: The server returns multiple greetings over time.
- **ChattyClientSaysHello (Client Streaming)**: The client sends multiple names, and the server replies after receiving them all.
- **InteractingHello (Bidirectional Streaming)**: The client and server exchange greetings in real-time.

## Setup Instructions

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/yourusername/gRPC_project.git
cd gRPC_project
```

## Create and Activate a Virtual Environment
```bash
python -m venv venv
```
### Activate virtual environment (Windows)
```bash
.\venv\Scripts\activate
```
### Activate virtual environment (Linux/Mac)
```bash
source venv/bin/activate
```

## Install Dependencies
```bash 
pip install -r requirements.txt
```

## Generate Python Code from .proto File
```bash
python -m grpc_tools.protoc -I=protos --python_out=. --pyi_out=. --grpc_python_out=. protos/greet.proto
```

This will generate the following Python files:

1. greet_pb2.py: Contains the message classes (HelloRequest, HelloReply, etc.)
2. greet_pb2_grpc.py: Contains the gRPC service classes and stubs.

## Running the gRPC Server
```bash
python greet_server.py
```
The server will start listening on port 50051 for client requests.

## Running the gRPC Client
```bash
python greet_client.py
```
The client will ask you to choose from one of the following options:

1. Unary Call: Send a single greeting.
2. Server Streaming: Receive multiple greetings from the server.
3. Client Streaming: Send multiple names, and the server replies with a summary.
4. Bidirectional Streaming: Both the client and server exchange messages in real time.

### Example Output
```cmd
1. SayHello - Unary
2. ParrotSaysHello - Server Side Streaming
3. ChattyClientSaysHello - Client Side Streaming
4. InteractingHello - Both streaming
Enter your choice: 1
SayHello Response Received:
message: "Hello, Hello John!"
```

## Project Dependencies
* gRPC: Python gRPC framework to enable client-server communication.
* Protocol Buffers (proto3): The language-neutral, platform-neutral data serialization format.

## How to Contribute
Feel free to fork this repository, make improvements, and submit a pull request. Make sure to open an issue first if you’re adding any significant features or making changes to the service.