import boto3
import configparser
import argparse

config = configparser.ConfigParser()
config.read('secrets.ini')

aws_access_key_id = config['SECRETS']['AWS_ACCESS_KEY_ID']
aws_secret_access_key = config['SECRETS']['AWS_SECRET_ACCESS_KEY']
aws_region_name = config['SECRETS']['AWS_REGION_NAME']


def init_client():
    try:
        client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region_name
        )

        return client
    except Exception as e:
        print(e)


def bucket_exists(name="my-bucket-from-boto3"):
    try:
        response = s3_client.list_buckets()
        for bucket in response['Buckets']:
            if bucket['Name'] == name:
                return True

        return False
    except Exception as e:
        print(e)
        return False


def delete_bucket(name="my-bucket-from-boto3"):
    try:
        s3_client.delete_bucket(Bucket=name)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    s3_client = init_client()
    parser = argparse.ArgumentParser(description="Please Enter A Bucket Name")
    parser.add_argument("bucket_name", type=str, help="Name: ")
    args = parser.parse_args()

    new_bucket_name = args.bucket_name

    if (s3_client):
        exists = bucket_exists(new_bucket_name)
        if exists:
            delete_bucket(new_bucket_name)
            print("Bucket Deleted Successfully With Name: " + new_bucket_name)
        else:
            print("Bucket Does Not Exist With Name: " + new_bucket_name)
