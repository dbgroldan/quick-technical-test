from flask import make_response, jsonify

# Build Response with content-type
def buildResponse(content_type, content):
    code, message = content
    resp = make_response(jsonify(message), code)
    resp.headers['Content-Type'] = content_type
    return resp

# Error Message in content-type
def errorContent():
    return 403, {"error": "Request should have 'Content-Type' header with value 'application/json'"}

# Get element by Email
def existEmail(email, control):
    filt = {
        'and': [
            {
                'condition': '=',
                'param': 'email',
                'value': "'{}'".format(email)
            }
            ]}
    return control.findByFilter(filt)

# Remove Password in  data
def removePass(res):
    code, data = res
    if isinstance(data, list):
        del data[0]['password']
    else:
        del data['password']
    return code, data

def removePassSet(res):
    code, data = res
    final_data = []
    for d in data:
        del d['password']
        final_data.append(d)
    return code, final_data
