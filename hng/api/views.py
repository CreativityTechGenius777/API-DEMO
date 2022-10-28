from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = {'slackUsername' : 'Destiny', 'backend': True, 'age' : 17, 'bio' : 'My name is John Destiny. I am a Web Developer as well as a Mechatronics Engineering student. I am very passionate about Technology and Engineering. I am a very creative person and also a problem solver'}
    
    return Response(person)