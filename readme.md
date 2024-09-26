curl -X POST http://localhost:8000/api/users/ \
-H "Content-Type: application/json" \
-d '{
    "user_type": "INTERVIEWER",
    "name": "John Doe"
}'


curl -X POST http://localhost:8000/api/candidate/<candidate_id>/availability/ \
-H "Content-Type: application/json" \
-d '{
    "start_time": "2024-09-30T09:00:00Z",
    "end_time": "2024-09-30T17:00:00Z"
}'

curl -X POST http://localhost:8000/api/interviewer/<interviewer_id>/availability/ \
-H "Content-Type: application/json" \
-d '{
    "start_time": "2024-09-30T09:00:00Z",
    "end_time": "2024-09-30T17:00:00Z"
}'

curl -X GET http://localhost:8000/api/user/<user_id>/availability/


curl -X POST http://localhost:8000/api/get_available_slots/ \
-H "Content-Type: application/json" \
-d '{
    "candidate_id": <candidate_id>,
    "interviewer_id": <interviewer_id>
}'



curl -X GET http://localhost:8000/api/users
