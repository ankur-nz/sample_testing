import boto3
from pprint import pprint
import sys
import os

def main():

    def enumerate_s3():
        if os.path.exists("output.csv"):
            os.remove("output.csv")
        else:
            print("")
        s3 = boto3.resource('s3')
        for bucket in s3.buckets.all():
             print("Name: {}".format(bucket.name), file=open("output.csv", "a"))
             print("All Info: {}\n".format(bucket.meta.client.list_objects_v2(Bucket=bucket.name,
                                           FetchOwner=True)).translate({ord('{'):None, ord('}'):None})
, file=open("output.csv", "a"))
             for object in bucket.objects.all():
                 print("Bucket files: {}".format(object.key), file=open("output.csv", "a"))

    enumerate_s3()


if __name__ == '__main__':
    main()