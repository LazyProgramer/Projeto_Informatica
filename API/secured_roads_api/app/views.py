from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Alert
from app.serializers import AlertSerializer

@api_view(['GET', 'POST'])
def alert_list(request):
    if request.method == 'GET':
        all_alerts = Alert.objects.all()
        serializer = AlertSerializer(all_alerts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        pass
