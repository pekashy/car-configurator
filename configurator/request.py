import json

import requests
import bleach
import os

endpoint = os.getenv('BACKEND_ENDPOINT')


def send_configuration(configuration):
    configuration["name"] = bleach.clean(configuration.get("name", ""))
    try:
        res = requests.post(
            "{}/save".format(endpoint), json=configuration
        )
    except requests.exceptions.ConnectionError:
        return "Failed to connect to server. Please try again later"
    except Exception:
        return "Failed to submit configuration. Please try again later"
    if res.status_code != 200:
        return "Failed to submit configuration, we are already fixing it, please try one more time later ({})".format(
            res.status_code
        )
    return "Configuration requested. We will contact you soon."


def count_processed():
    try:
        res = requests.get(
            "{}/count".format(endpoint)
        )
    except requests.exceptions.ConnectionError:
        return "Failed to connect to server. Please try again later"
    except Exception:
        return "Failed to get server report. Please try again later"
    if res.status_code != 200:
        return "Failed to get server report, we are already fixing it, please try one more time later ({})".format(
            res.status_code
        )
    return str(json.loads(res.content))
