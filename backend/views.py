from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from backend.models import Member, Habit, Type
from backend.serializers import MemberSerializer, HabitSerializer, TypeSerializer


# GETs
@swagger_auto_schema(method='GET', responses={200: MemberSerializer(many=True)})
@api_view(['GET'])
def member_list(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: HabitSerializer(many=True)})
@api_view(['GET'])
def habit_list(request):
    habits = Habit.objects.all()
    serializer = HabitSerializer(habits, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: TypeSerializer(many=True)})
@api_view(['GET'])
def type_option_list(request):
    types = Type.objects.all()
    serializer = TypeSerializer(types, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: MemberSerializer()})
@api_view(['GET'])
def member_form_get(request, pk):
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return Response({'error': 'Member does not exist.'}, status=404)

    serializer = MemberSerializer(member)
    return Response(serializer.data)


@swagger_auto_schema(method='GET', responses={200: HabitSerializer()})
@api_view(['GET'])
def habit_form_get(request, pk):
    try:
        habit = Habit.objects.get(pk=pk)
    except Habit.DoesNotExist:
        return Response({'error': 'Habit does not exist.'}, status=404)

    serializer = HabitSerializer(habit)
    return Response(serializer.data)


# POSTs
@swagger_auto_schema(method='POST', request_body=MemberSerializer, responses={200: MemberSerializer()})
@api_view(['POST'])
def member_form_create(request):
    data = JSONParser().parse(request)
    serializer = MemberSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='POST', request_body=HabitSerializer, responses={200: HabitSerializer()})
@api_view(['POST'])
def habit_form_create(request):
    data = JSONParser().parse(request)
    serializer = HabitSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# POSTs
@swagger_auto_schema(method='POST', request_body=TypeSerializer, responses={200: TypeSerializer()})
@api_view(['POST'])
def type_create(request):
    data = JSONParser().parse(request)
    serializer = TypeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# PATCHs
@swagger_auto_schema(method='PATCH', request_body=MemberSerializer, responses={200: MemberSerializer()})
@api_view(['PATCH'])
def member_form_update(request, pk):
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return Response({'error': 'Member does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = MemberSerializer(member, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(method='PATCH', request_body=HabitSerializer, responses={200: HabitSerializer()})
@api_view(['PATCH'])
def habit_form_update(request, pk):
    try:
        habit = Habit.objects.get(pk=pk)
    except Habit.DoesNotExist:
        return Response({'error': 'Habit does not exist.'}, status=404)

    data = JSONParser().parse(request)
    serializer = HabitSerializer(habit, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# DELETEs
@api_view(['DELETE'])
def member_delete(request, pk):
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return Response({'error': 'Member does not exist.'}, status=404)
    member.delete()
    return Response(status=204)


@api_view(['DELETE'])
def habit_delete(request, pk):
    try:
        habit = Habit.objects.get(pk=pk)
    except Habit.DoesNotExist:
        return Response({'error': 'Habit does not exist.'}, status=404)

    habit.delete()
    return Response(status=204)
