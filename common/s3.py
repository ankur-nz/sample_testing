import boto3
from botocore.exceptions import ClientError


s3 = boto3.resource('s3')
buckets = s3.buckets.all()

for bucket in buckets:
    print(bucket.name)
    try:
        tag_set = s3.BucketTagging(bucket.name).tag_set
        for tag in tag_set:
            tag_values = list(tag.values())
            print(bucket.name)
            print(tag_values)
    except ClientError as e:
        pass
        # print('No Tags') 