from rest_framework.views import APIView
from api.models import Post
from api.serializers import MySerializer
from rest_framework.response import Response
import requests
import json
# Create your views here.


# class MyApiView(APIView):
#         def get(self, request, id=None):
#             url ='https://jsonplaceholder.typicode.com/posts'
#
#             response = requests.get(url)
#             print(type(response))
#
#             if response.status_code == 200:
#                 data = response.json()
#                 # Process the data as needed
#                 # Return a response or render a template with the data
#             else:
#                 # Handle the case when the request fails
#                 data = []
#
#             return Response(data)

class MyApiView(APIView):
    def get(self, request, id=None):
        try:

        # Check if data already exists in the database
            if Post.objects.count() == 0:
                # Fetch data from the external API and save it to the database
                url = 'https://jsonplaceholder.typicode.com/posts'
                response = requests.get(url)
                print(response)
                print(type(response))

                if response.status_code == 200:
                    fetched_data = response.json()

                    # print(response.json())

                    for item in fetched_data:
                        my_model = Post(
                            userId=item['userId'],
                            id=item['id'],
                            title=item['title'],
                            body=item['body']
                        )
                        my_model.save()

            # Fetch data from the database
            data_from_db = Post.objects.all().values()



            return Response(data_from_db)
        except Exception as exception:
            error_message = str(exception)
            return Response([error_message])





    # ===================================================


    # def get(self, request, id=''):
    #     try:
    #         # url = 'https://jsonplaceholder.typicode.com/posts/1/comments'
    #         url = 'https://jsonplaceholder.typicode.com/users'
    #         # payload = {'id': id}
    #         data = request.data
    #         print(data)
    #         print(json.dumps(data))
    #
    #         response = requests.get(url, data=json.dumps(data))
    #         print(response)
    #         print(response.status_code)
    #
    #         if response.status_code == 200:
    #             print(data)
    #             print("=============================")
    #             print(response.json())
    #
    #             data = response.json()
    #             print(data)
    #             # Process the data as needed
    #             # Return a response or render a template with the data
    #         else:
    #             # Handle the case when the request fails
    #             data = []
    #
    #         return Response(data)
    #     except Exception as exception:
    #         print(exception)
        # ========================================================================================



        def put(self, request, id= None):
            url = f'https://jsonplaceholder.typicode.com/posts/{id}'
            data = request.data  # Retrieve the data from the request body
            print(data)

            response = requests.put(url, data)
            data = response.json()
            print(data)

            return Response(data)

        def post(self, request, id=None):
            url = f'https://jsonplaceholder.typicode.com/posts/{id}'
            data = request.data  # Retrieve the data from the request body
            print(data)

            response = requests.put(url, data)
            data = response.json()
            print(data)

            return Response(data)

        def patch(self, request, id = None):
            url = f'https://jsonplaceholder.typicode.com/posts/{id}'
            data = request.data
            print(data)

            response = requests.patch(url, data)

            data = response.json()
            print(data)
            return Response(data)

        def delete(self, request, id=None):
            url = f'https://jsonplaceholder.typicode.com/posts/{id}'

            data = request.data
            params = {'id': id}
            response = requests.delete(url, params= params)
            if response.status_code == 200:
                return Response({"success"})
            else:
                return Response({"Unsuccessful"})






