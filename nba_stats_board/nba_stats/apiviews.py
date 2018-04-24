# coding: utf-8

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Team, City, Arena


class TeamListView(View):
    """球队列表"""

    def get(self, request):
        team_list = list()
        team_objs = Team.objects.all()
        if not team_objs:
            result = dict(
                status='fail',
                code=1,
                message='Not found',
                data=dict()
            )
        else:
            for team_obj in team_objs:
                team = {
                    'name': team_obj.name,
                    'founded': team_obj.founded,
                    'city': team_obj.city.name,
                    'logo': team_obj.team_logo_url
                }
                team_list.append(team)
            result = dict(
                status='success',
                code=0,
                message='Found',
                data=dict(teams=team_list)
            )
        return JsonResponse(result)


class TeamDetailView(View):
    """球队详情"""

    def get(self, request, pk):
        try:
            team_obj = Team.objects.get(pk=pk)
        except Team.DoesNotExist as e:
            print(e)
            result = dict(
                status='fail',
                code=1,
                message='Not found',
                data=dict()
            )
        else:
            team = {
                'name': team_obj.name,
                'founded': team_obj.founded,
                'city': team_obj.city.name,
                'arena': team_obj.arena.name,
                'owner': team_obj.owner,
                'generalManager': team_obj.general_manager,
                'headCoach': team_obj.head_coach,
                'logo': team_obj.team_logo_url
            }
            result = dict(
                status='success',
                code=0,
                message='Found',
                data=team
            )
        return JsonResponse(result)


@method_decorator(csrf_exempt, 'dispatch')
class TeamCreateView(View):
    """创建球队"""

    def post(self, request):
        data = request.POST

        city = data.get('city')
        city_obj = City.objects.get_or_create(name=city)[0]

        arena = data.get('arena')
        arena_obj = Arena.objects.get_or_create(name=arena, city=city_obj)[0]

        name = data.get('name')
        founded = data.get('founded')
        owner = data.get('owner')
        general_manager = data.get('general_manager')
        head_coach = data.get('head_coach')
        team_logo_url = data.get('team_logo_url')

        team_obj = Team.objects.get_or_create(
            name=name,
            founded=founded,
            owner=owner,
            general_manager=general_manager,
            head_coach=head_coach,
            team_logo_url=team_logo_url,
            city=city_obj,
            arena=arena_obj
        )[0]

        team = dict(
            id=team_obj.id,
            name=team_obj.name,
            founded=team_obj.founded,
            owner=team_obj.owner,
            general_manager=team_obj.general_manager,
            head_coach=team_obj.head_coach,
            team_logo_url=team_obj.team_logo_url,
            city=city_obj.name,
            arena=arena_obj.name
        )

        result = dict(
            status='success',
            code=0,
            message='Created',
            data=team
        )

        return JsonResponse(result)
