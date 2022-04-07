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
def getAlertById(request):
    if request.method == 'GET':
        try:
            id = request.GET.get('id', '')
            alert = Alert.objects.get(id=id)
            serializer = AlertSerializer(alert)
            return Response(serializer.data)
        except:
            return Response(status=404)

#Get Alert by level
@api_view(['GET', 'POST'])
def getAlertByLevel(request):
    if request.method == 'GET':
        try:
            alerts = Alert.objects.all()
            level = request.GET.get('level', '')
            alerts = alerts.filter(level=level) if level != '' else alerts
            type = request.GET.get('type', '')
            alerts = alerts.filter(type=type) if type != '' else alerts
            source = request.GET.get('source', '')
            alerts = alerts.filter(source=source) if source != '' else alerts
            location = request.GET.get('location', '')
            alerts = alerts.filter(location=location) if location != '' else alerts
            
            serializer = AlertSerializer(alerts, many=True)
            return Response(serializer.data)
        except:
            return Response(status=404)

#Get Alert by location

#Get Alert by type

#Get Alert by date

#Get Alert by source