import boto3
import configparser
from requests import get

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


def list_buckets():
    try:
        response = s3_client.list_buckets()
        print("Existing buckets:")
        for bucket in response['Buckets']:
            print("Name:", bucket['Name'])
            print("Creation Date: ", bucket['CreationDate'])

    except Exception as e:
        print(e)


def create_bucket(name="my-bucket-from-boto3"):
    try:
        s3_client.create_bucket(
            Bucket=name)
        print(f"Bucket {name} created.")

    except Exception as e:
        print(e)


def delete_bucket(name="my-bucket-from-boto3"):
    try:
        s3_client.delete_bucket(Bucket=name)
        print(f"Bucket {name} deleted.")
    except Exception as e:
        print(e)


def bucket_exists(name="my-bucket-from-boto3"):
    try:
        s3_client.head_bucket(Bucket=name)
        return True
    except Exception as e:
        print(e)
        return False


def download_file_and_upload_to_s3(bucket_name):
    try:
        random_image = get(
            "https://randomuser.me/api/portraits/lego/6.jpg")

        with open("image.jpg", "wb") as f:
            f.write(random_image.content)

        s3_client.upload_file(
            "image.jpg", bucket_name, "image.jpg"
        )

        image_url = s3_client.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket": bucket_name,
                "Key": "image.jpg",
            },
            ExpiresIn=3600,
        )

        print(f"Image URL: {image_url}")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    s3_client = init_client()
    new_bucket_name = "aws-python-bucket-dijsaoidjasodijasoids-6"

    if (s3_client):
        delete_bucket()
