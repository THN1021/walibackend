from rest_framework import serializers
from ordersys.models import OrderProtocol, OrderInfo
from appraisalsys.models import AppraisalInfo


class ObtainOrderLogSerializer(serializers.Serializer):
    user_sid = serializers.CharField()
    oid = serializers.PrimaryKeyRelatedField(queryset=OrderInfo.objects)


class ObtainOrderProtocolLogSerializer(serializers.Serializer):
    user_sid = serializers.CharField()
    opid = serializers.PrimaryKeyRelatedField(queryset=OrderProtocol.objects)


class ObtainAppraisalLogSerializer(serializers.Serializer):
    user_sid = serializers.CharField()
    apprid = serializers.PrimaryKeyRelatedField(queryset=AppraisalInfo.objects)
