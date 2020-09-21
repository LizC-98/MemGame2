import boto3
#s3_client = boto3.client('s3')
#s3_resource = boto3.resource('s3')

class AWSManager:  
    def __init__(self):
        self.client = boto3.client('s3')
        self.resource = boto3.resource('s3')
    def listBucketFile(self, bucketName):
        bucket = self.resource.Bucket(bucketName)
        files = bucket.objects.all()
        for file in files:
            print(file.key)

    def save_to_s3(self):
        boto3.client('s3').upload_file('index.html', 'lmtd-class', 'index.html')





my_aws = AWSManager()

#my_aws.save_to_s3()

my_aws.listBucketFile("lmtd-class")