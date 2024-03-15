import datetime
import json

STAND_SETTINGS = {
    "shchedule": True,
    "last": "01.01.01",
    "delta": 7
}

def get_cleanup_json():
    try:
        with open('cleanup.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        with open('cleanup.json', 'w') as file:
            json.dump(file, STAND_SETTINGS)
            return STAND_SETTINGS

class Cleanup:
    def __init__(self) -> None:
        self.cleanup_json = get_cleanup_json()
        
        self.last_cleanup = datetime.datetime.strptime(self.cleanup_json['last'], "%Y-%m-%d %H:%M:%S")
        self.delta_cleanup = datetime.timedelta(days=self.cleanup_json['delta'])
        
    def get_last_cleanup(self):
        return self.last_cleanup
    
    def get_delta_cleanup(self):
        return self.delta_cleanup

    def is_cleanup_due(self):
        """
        Проверяет, подошло ли время для уборки.
        """
        next_cleanup = self.last_cleanup + self.delta_cleanup
        return datetime.datetime.now() >= next_cleanup
