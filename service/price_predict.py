import logging
from concurrent.futures import ThreadPoolExecutor

import grpc

from service import service_pb2_grpc
from service.service_pb2 import PredictOneReq, PredictOneRsp


class PredictService(service_pb2_grpc.PricePredictServicer):
    def PredictOne(self, request: PredictOneReq, context):
        rsp = PredictOneRsp(price='1.0')
        return rsp


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_PricePredictServicer_to_server(PredictService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
