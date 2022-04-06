from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Alert
from app.serializers import AlertSerializer


#Get All Alerts
@api_view(['GET', 'POST'])
def alert_list(request):
    if request.method == 'GET':
        all_alerts = Alert.objects.all()
        serializer = AlertSerializer(all_alerts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        pass

#Get Alert By Id
@api_view(['GET', 'POST'])
def getAlertById(request, id):
    if request.method == 'GET':
        try:
            alert = Alert.objects.get(id=id)
            serializer = AlertSerializer(alert)
            return Response(serializer.data)
        except:
            return Response(status=404)

#Get Alert by level

#Get Alert by location

#Get Alert by type

#Get Alert by date

#Get Alert by source