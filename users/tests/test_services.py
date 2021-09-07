from ..proto.users_pb2 import RetrieveUserByIDRequest, User
from ..services import UsersService


def test_users_service():
    expected_uuid = "086d1bf5-0b3b-4158-84df-44eff533aa71"
    service = UsersService()
    request = RetrieveUserByIDRequest(uuid=expected_uuid)
    response = service.GetUserByIDRequest(request)
    assert response.uuid == expected_uuid
