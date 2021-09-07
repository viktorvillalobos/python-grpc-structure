import grpc

import proto.users_pb2 as users_pb2
import proto.users_pb2_grpc as users_pb2_grpc

MOCKED_USERS_BY_UUID = {
    "086d1bf5-0b3b-4158-84df-44eff533aa71": users_pb2.User(
        first_name="Viktor",
        last_name="Villalobos",
        uuid="086d1bf5-0b3b-4158-84df-44eff533aa71",
    )
}


class UsersService(users_pb2_grpc.UsersServicer):
    def GetUserByID(
        self, request: users_pb2.RetrieveUserByIDRequest, context: grpc.ServicerContext
    ) -> users_pb2.User:
        if request.uuid not in MOCKED_USERS_BY_UUID:
            context.abort(grpc.StatusCode.NOT_FOUND, "User does not exist")

        return MOCKED_USERS_BY_UUID[request.uuid]
