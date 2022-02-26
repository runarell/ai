# from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

def index(request):
    """
    게시판 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'pybo/question_list.html', context)

    # 질문 목록 데이터들은 Question.objects.order_by('-create_date')
    # 로 얻어 온다.  order_by 는 조회 결과를 정렬하는 함수이다. 
    # -는 역순으로 정렬한다. 게시물은 보통 최신 순으로 보기때문에 작성일시
    # 역순으로 정렬했다. 

def detail(request, question_id):
    """
    게시판 내용 출력
    """
    question = Question.objects.get(id=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)