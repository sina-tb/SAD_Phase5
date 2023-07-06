import requests


class Server:
    def __init__(self):
        pass

    def get_packages(self):
        return self.run_query('http://65.109.206.96:8000/packages/')

    def get_prerequisities(self, package_id):
        return self.run_query(f'http://65.109.206.96:8000/packages/{package_id}/prerequisites-types/')

    def finalize_request_and_get_package(self, new_record):
        supporter = 'Someone'
        return supporter
    
    def run_query(self, end_point):
        for _ in range(30):
            try:
                response = requests.get(end_point, timeout=1)
                return response.content
            except:
                pass
