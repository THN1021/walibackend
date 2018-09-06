from rest_framework import serializers
from appraisalsys.models import AppraisalInfo


class SubmitAppraisalSerializer(serializers.Serializer):
    user_sid = serializers.CharField(max_length=60)
    ivid = serializers.IntegerField()
    in_accordance = serializers.BooleanField()
    parameter = serializers.JSONField()
    check_photos = serializers.ListField(child=serializers.IntegerField(min_value=1), required=False)

    def validate(self, attrs):
        if not attrs["in_accordance"]:
            seri_cls = AppraisalInfoSubmitSerializerForAccordance
        else:
            seri_cls = AppraisalInfoSubmitSerializerForNotAccordance
        seri = seri_cls(data=attrs["parameter"])
        seri.is_valid(raise_exception=True)
        attrs["parameter"] = seri.validated_data
        return attrs


class AppraisalInfoSubmitSerializerForAccordance(serializers.ModelSerializer):
    class Meta:
        model = AppraisalInfo
        fields = (
          "final_total_price", "description", "net_weight", "pure_net_weight",
          "wcid", "impcid",
          "price_1", "price_2", "price_3"
        )


class AppraisalInfoSubmitSerializerForNotAccordance(serializers.Serializer):
    pass