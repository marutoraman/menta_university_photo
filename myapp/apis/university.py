from rest_framework.views import APIView, set_rollback
from rest_framework.response import Response
from rest_framework import status

from ..models import Major
from ..selializers.major import MajorSeializer


class MajorAPIView(APIView):
    
    def get(self, request):
        '''
        データ取得
        '''
        # 学校でフィルタ
        seliarizer = MajorSeializer(Major.objects.filter(r_university__id = request.GET.get("university_id")), many=True)
        return Response(seliarizer.data)
    