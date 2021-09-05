import logging
from concurrent.futures import ThreadPoolExecutor

import grpc

from model import model
from service import service_pb2_grpc
from service.service_pb2 import PredictOneReq, PredictOneRsp


class PredictService(service_pb2_grpc.PricePredictServicer):
    def PredictOne(self, request: PredictOneReq, context):
        rsp = PredictOneRsp(price=model.predict(request.car.original_price,
                                                request.car.mileage,
                                                request.car.register_timestamp))
        return rsp


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_PricePredictServicer_to_server(PredictService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


def main():
    logging.basicConfig()
    model.pre_train()
    print("ready to serve")
    serve()


if __name__ == '__main__':
    main()
