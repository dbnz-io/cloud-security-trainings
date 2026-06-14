import json


def process_cloudtrail_event(event, context):
    print("Received CloudTrail event from EventBridge:")
    print(json.dumps(event, indent=2, default=str))

    detail = event.get("detail", {})

    print("Event name:", detail.get("eventName"))
    print("Event source:", detail.get("eventSource"))
    print("AWS region:", detail.get("awsRegion"))
    print("User identity:", json.dumps(detail.get("userIdentity", {}), indent=2))

    return {
        "statusCode": 200,
        "body": "CloudTrail event processed"
    }