from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):
  charset = 'UTF-8'
  def render(self, data, accepted_media_type=None, renderer_context=None):
      # accepted_media_type="application/json; nested=true"
      response = {}
      
      if 'ErrorDetail' in str(data):
        response = json.dumps({'errors': data})
      else:
        response = json.dumps({'data': data})
      # import pdb
      # pdb.set_trace()
      # print(response)
      return response

