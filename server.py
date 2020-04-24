import math
import time
from threading import Thread
from time import sleep

import grpc
from concurrent import futures

import calculator_pb2
import calculator_pb2_grpc


def square_root(x):
    y = math.sqrt(x)
    return y


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = square_root(request.value)
        return response

    def ListNumbers(self, request, context):
        for i in range(10):
            sleep(0.1)
            response = calculator_pb2.Number()
            response.value = i
            yield response
        for i in range(20):
            sleep(0.2)
            response = calculator_pb2.Number()
            response.value = i*100
            yield response
        # for i in range(int(request.value)):
        #     sleep(0.1)
        #     response = calculator_pb2.Number()
        #     response.value = i
        #     yield response

    def ReverseWord(self, request_iterator, context):
        for m in request_iterator:
            sleep(0.5)
            response = calculator_pb2.Messages()
            response.word = m.word[::-1]
            yield response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

calculator_pb2_grpc.add_CalculatorServicer_to_server(
    CalculatorServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
