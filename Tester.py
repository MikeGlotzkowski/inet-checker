from typing import Text
import requests
from requests.exceptions import ReadTimeout, ConnectionError


class Tester(object):

    def __init__(self, url: Text, timeout: float, log_file_path: str):
        self.url: Text = url
        self.timeout: float = timeout
        self.log_file_path: str = log_file_path
        self.wasSuccessful = False
        self.elapsed: float = None
        self.run_index:int =  0

    def run(self):
        self.run_index += 1
        try:
            r = requests.get(url=self.url, timeout=self.timeout)
            self.elapsed = r.elapsed.total_seconds()
            self.wasSuccessful = True
        except (ReadTimeout, ConnectionError) as timeout_e:
            self.elapsed = self.timeout
            self.wasSuccessful = False
        return self

    def print_elapsed(self):
        print(
            f"Call {self.run_index} {'was successful' if self.wasSuccessful else 'failed'} in {self.elapsed} seconds.")
        return self

    def save_elapsed(self):
        with open (self.log_file_path, "a") as log_file:
            log_file.write(f'{self.run_index},{self.elapsed}\n')
        return self