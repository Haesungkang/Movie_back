from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from .serializers import UserSerializer

# from django.contrib.auth.forms import (
#     AuthenticationForm,
#     PasswordChangeForm,
# )
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_POST, require_http_methods, require_safe
# from django.contrib.auth import update_session_auth_hash
# from .forms import CustomUserChangeForm




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

        
# @login_required
# @require_http_methods(['GET', 'POST'])
# def update(request):
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('community')
#     else:
#         form = CustomUserChangeForm(instance=request.user)
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/update.html', context)


# @login_required
# @require_http_methods(['GET', 'POST'])
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             return redirect('community')
#     else:
#         form = PasswordChangeForm(request.user)
#     context = {'form': form}
#     return render(request, 'accounts/change_password.html', context)
