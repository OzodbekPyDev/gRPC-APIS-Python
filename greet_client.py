import greet_pb2_grpc
import greet_pb2

import time

import grpc

def get_client_stream_request():
    while True:
        name = input("Enter your name: ")

        if name == "":
            break

        hello_request = greet_pb2.HelloRequest(name=name, greeting="Hello")
        yield hello_request
        time.sleep(1)

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - Unary")
        print("2. ParrotSaysHello - Server Side Streaming")
        print("3. ChattyClientSaysHello - Client Side Streaming")
        print("4. InteractingHello - Both streaming")
        rpc_call = input("Enter your choice: ")

        if rpc_call == "1":
            hello_request = greet_pb2.HelloRequest(name="John", greeting="Hello")
            hello_reply = stub.SayHello(hello_request)
            print("SayHello Response Received: ")
            print(hello_reply)

        elif rpc_call == "2":
            hello_request = greet_pb2.HelloRequest(name="John", greeting="Hello")
            hello_replies = stub.ParrotSaysHello(hello_request)
            for hello_reply in hello_replies:
                print("ParrotSaysHello Response Received: ")
                print(hello_reply)

        elif rpc_call == "3":
            delayed_reply = stub.ChattyClientSaysHello(get_client_stream_request())

            print("ChattyClientSaysHello Response Received: ")
            print(delayed_reply)
        elif rpc_call == "4":
            responses = stub.InteractingHello(get_client_stream_request())
            for response in responses:
                print("InteractingHello Response Received: ")
                print(response)



if __name__ == "__main__":
    run()