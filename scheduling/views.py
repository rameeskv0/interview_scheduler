from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Availability
from .serializers import UserSerializer, AvailabilitySerializer, AvailabilityInputSerializer
from datetime import timedelta

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

@api_view(['POST'])
def input_candidate_availability(request, candidate_id):
    try:
        candidate = User.objects.get(id=candidate_id, user_type='CANDIDATE')
    except User.DoesNotExist:
        return Response({"error": "Candidate not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AvailabilityInputSerializer(data=request.data)
    if serializer.is_valid():
        # Check for existing availability
        existing_availability = Availability.objects.filter(user=candidate).first()
        if existing_availability:
            # Update existing entry
            existing_availability.start_time = serializer.validated_data['start_time']
            existing_availability.end_time = serializer.validated_data['end_time']
            existing_availability.save()
            return Response({"message": "Availability updated successfully"}, status=status.HTTP_201_CREATED)
        
        # Create new availability if none exists
        Availability.objects.create(
            user=candidate,
            start_time=serializer.validated_data['start_time'],
            end_time=serializer.validated_data['end_time']
        )
        return Response({"message": "Availability added successfully"}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def input_interviewer_availability(request, interviewer_id):
    try:
        interviewer = User.objects.get(id=interviewer_id, user_type='INTERVIEWER')
    except User.DoesNotExist:
        return Response({"error": "Interviewer not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AvailabilityInputSerializer(data=request.data)
    if serializer.is_valid():
        # Check for existing availability
        existing_availability = Availability.objects.filter(user=interviewer).first()
        if existing_availability:
            # Update existing entry
            existing_availability.start_time = serializer.validated_data['start_time']
            existing_availability.end_time = serializer.validated_data['end_time']
            existing_availability.save()
            return Response({"message": "Availability updated successfully"}, status=status.HTTP_201_CREATED)
        
        # Create new availability if none exists
        Availability.objects.create(
            user=interviewer,
            start_time=serializer.validated_data['start_time'],
            end_time=serializer.validated_data['end_time']
        )
        return Response({"message": "Availability added successfully"}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_availability(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    availabilities = Availability.objects.filter(user=user)
    serializer = AvailabilitySerializer(availabilities, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def get_available_slots(request):
    candidate_id = request.data.get('candidate_id')
    interviewer_id = request.data.get('interviewer_id')
    
    candidate_slots = Availability.objects.filter(user_id=candidate_id)
    interviewer_slots = Availability.objects.filter(user_id=interviewer_id)
    
    available_slots = set()
    
    for c_slot in candidate_slots:
        for i_slot in interviewer_slots:
            start = max(c_slot.start_time, i_slot.start_time)
            end = min(c_slot.end_time, i_slot.end_time)
            
            if start < end:
                current = start
                while current + timedelta(hours=1) <= end:
                    slot = (
                        current.strftime("%Y-%m-%d %H:%M"),
                        (current + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M")
                    )
                    available_slots.add(slot)
                    current += timedelta(hours=1)
    
    return Response(list(available_slots))
