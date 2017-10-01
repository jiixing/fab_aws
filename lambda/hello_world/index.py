from __future__ import print_function

import json

print('Loading function')


def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')

if __name__ == '__main__':
    # For invoking the lambda function in the local environment.
    from hello_world import LocalContext
    context = LocalContext()
    event = {"key1":"key1val"}
    handler(event, context)
