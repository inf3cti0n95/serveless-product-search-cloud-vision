import logging
import os
import sys
import json

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(here)

from lib import detect_image


def lambda_handler(event, context):
    """AWS Lambda Handler for API Gateway input"""
    print("Current Event: %s" % event)
    post_args = json.loads(event.get("body", "{}"))
    print(post_args)
    image_url = post_args["image_url"]
    detect_type = post_args.get("detect_type", "PRODUCT_SEARCH")
    max_results = post_args.get("max_results", 5)

    print("Detecting image from URL: %s" % image_url)
    print("Image detection type: %s" % detect_type)
    print("Maximum number of results: %s" % max_results)

    json_return = detect_image(image_url,
                               detect_type,
                               max_results)
    print(json_return)
    return json_return


