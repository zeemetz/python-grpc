import random

import grpc

import calculator_pb2
import calculator_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

stub = calculator_pb2_grpc.CalculatorStub(channel)
number = calculator_pb2.Number(value=81)
list_of_word = ['nhoj', 'wons', 'toile', 'ydnew']


def messages():
    while 1:
        name = random.choice(list_of_word)
        yield calculator_pb2.Messages(word=name)


try:
    # response = stub.ReverseWord(messages())
    # for i in response:
    #     print(i.word)
    response = stub.ListNumbers(number)
    for i in response:
        print(i.value)
except Exception as e:
    print(e._state.code)
    print(e._state.details)
