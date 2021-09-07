import logging
from concurrent import futures

import grpc

import services
from proto import users_pb2_grpc


def serve():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(services.UsersService(), server)
    logger.info("Starting Users Service GRPC in port ::50051")
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
