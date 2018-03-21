from pyswagger import App, Security
from pyswagger.contrib.client.requests import Client
from pyswagger.utils import jp_compose

# load Swagger resource file into App object
app = App._create_('http://192.168.164.135:7100/api/v1/swagger.json')
auth = Security(app)
#auth.update_with('api_key', '12312312312312312313q') # api key
auth.update_with('accessTokenAuth', 'Bearer 0f55cdd792c34e74b879d07ab29bb6a9ed5e730728e541e09d49b69ebab5c8bb') # oauth2

# init swagger client
client = Client(auth)


# a dict is enough for representing a Model in Swagger
#pet_Tom=dict(id=1, name='Tom', photoUrls=['http://test']) 
# a request to create a new pet
#client.request(app.op['addPet'](body=pet_Tom))

# - access an Operation object via App.op when operationId is defined
# - a request to get the pet back
req, resp = app.op['getUser']()

# prefer json as response
#req.produce('application/json')
user = client.request((req, resp)).data
print(user)
#assert pet.id == 1
#assert pet.name == 'Tom'

## new ways to get Operation object corresponding to 'getPetById'.
## 'jp_compose' stands for JSON-Pointer composition
#req, resp = app.resolve(jp_compose('/pet/{petId}', base='#/paths')).get(petId=1)
#req.produce('application/json')
#pet = client.request((req, resp)).data
#assert pet.id == 1
