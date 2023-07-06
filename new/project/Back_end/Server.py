from DAO import DAO
from DbConnection import DbConnection


class Server:
    def __init__(self):
        self._dao = DAO()
        self._db_connection = DbConnection()

    def get_prerequisities(self, package_id):
        query = self._dao.make_get_prerequisities_query(package_id)
        result = self._db_connection.enter_query(query)
        # parse result and make prerequisities
        prerequisities = []
        return prerequisities

    def finalize_request_and_get_package(self, prerequisities, package_id, user_name):
        query = self._dao.make_add_record_query(
            prerequisities, package_id, user_name)
        result = self._db_connection.enter_query(query)
        # parse result and make message
        message = ''
        return message
