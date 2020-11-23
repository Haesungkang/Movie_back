from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .serializers import UserSerializer

# Create your views here.
@api_view(['POST'])
def signup(request):
    # Client에서 보내온 정보 받기
    password = request.data.get('password')
    passwordConfirmation = request.data.get('passwordConfirmation')

    # 비밀번호 일치 여부 확인
    if password != passwordConfirmation:
        return Response({ 'error': '비밀번호가 일치하지 않습니다.' })

    # 사용자가 보낸 데이터로 UserSerializer를 통해 데이터 생성
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        # 그냥 저장하고 끝내면 비밀번호 유출
        user = serializer.save()

        # 비밀번호 해싱
        user.set_password(request.data.get('password'))
        user.save()

        return Response(serializer.data)

        