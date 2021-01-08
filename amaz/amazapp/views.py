from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import json
# Create your views here.
@csrf_exempt
def idx(request):
    context = {
        'test1': ['test']
    }
    context2 = json.dumps(context)

    print(context2)
    return render(request, 'amaz/index.html', {'test' : context2})


def answer_list(request):
    answer = request.POST['answer']
    print(answer)

    def answer2(answer):
        answer_list = list(''.join(str(answer).split(' ')))
        answer_list_set = list(set(answer_list))

        return answer_list ,answer_list_set

    answer_list, answer_list_set = answer2(answer)
    context = {
        'answer_list' : answer_list,
        'answer_list_set' :answer_list_set
    }

    data = [context]
    return JsonResponse(data, safe=False)


def answer3(request):
    answer = request.POST['answer']
    answer_출연진 = request.POST['answer_출연진']

    def answer4(answer, answer_출연진):
        answer_list = list(''.join(str(answer).split(' ')))

        answer_출연진_list = list(''.join(str(answer_출연진).split(' ')))
        answer_출연진_list_set = set(answer_출연진_list)

        정답_출연진_같은언어 = list(set(answer_출연진_list).intersection(set(answer_list)))
        정답_출연진_다른언어 = list(set(answer_list).difference(set(answer_출연진_list)))

        return 정답_출연진_같은언어, 정답_출연진_다른언어, len(정답_출연진_같은언어), list(answer_출연진_list_set), answer_출연진_list

    정답_출연진_같은언어, 정답_출연진_다른언어, 정답개수, answer_출연진_list_set, answer_출연진_list = answer4(answer, answer_출연진)

    data = [{
        'answer_출연진_list' : answer_출연진_list,
        '정답_출연진_같은언어' : 정답_출연진_같은언어,
        '정답_출연진_다른언어' : 정답_출연진_다른언어,
        '정답개수' : 정답개수,
        'answer_출연진_list_set' : answer_출연진_list_set
    }]

    return JsonResponse(data, safe=False)