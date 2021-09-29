from aws_cdk import core as cdk
from aws_cdk import aws_s3 as _s3



####S3 Stack : Creating two buckets and exporting one bucker name.
class CdkProject01Stack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        _s3.Bucket(
            self,
            "mybucketID",
            bucket_name="my-cdk-bucket-01-123321",
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED            
        )    

        bucket_1 = _s3.Bucket(self,"mybucketID1",bucket_name="my-cdk-bucket-02-123321")
        print(bucket_1.bucket_name)

        myBucketOutput_1_local = cdk.CfnOutput(self,"myBucketOutputID1",
                    value=bucket_1.bucket_name,
                    export_name="myBucketOutput1")
    