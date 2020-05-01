import json
from dataclasses import dataclass

from util import resource_path


@dataclass
class Args:
    LISTEN_PORT: int
    PROXY_PORT: int


with open(resource_path('config.json')) as file:
    config = Args(**json.load(file))
