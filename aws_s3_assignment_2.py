import boto3
import json
import argparse
from botocore.exceptions import ClientError


def get_bucket_policy(s3_client, bucket_name):
    try:
        policy = s3_client.get_bucket_policy(Bucket=bucket_name)
        return policy['Policy']
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'NoSuchBucketPolicy':
            return None
        elif error_code == 'AccessDenied':
            print("Access denied when attempting to retrieve the bucket policy.")
            return "Error"
        else:
            print(f"Unhandled error: {e}")
            return "Error"
    except Exception as e:
        print(f"Error getting bucket policy: {e}")
        return "Error"


def create_public_access_policy(bucket_name):
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadForDevAndTestPrefixes",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": [f"arn:aws:s3:::{bucket_name}/dev/*", f"arn:aws:s3:::{bucket_name}/test/*"]
            }
        ]
    }
    return json.dumps(policy)


def set_bucket_policy(s3_client, bucket_name, policy):
    try:
        s3_client.put_bucket_policy(Bucket=bucket_name, Policy=policy)
        print(
            f"Public access policy set for /dev and /test prefixes in bucket {bucket_name}")
    except Exception as e:
        print(f"Error setting bucket policy: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Check or set a public access policy on S3 bucket prefixes /dev and /test.")
    parser.add_argument("bucket_name", type=str, help="Name of the S3 bucket")
    args = parser.parse_args()

    s3_client = boto3.client("s3")

    current_policy = get_bucket_policy(s3_client, args.bucket_name)
    if current_policy is None:
        print("No existing policy found. Creating a new one for public access to /dev and /test prefixes.")
        new_policy = create_public_access_policy(args.bucket_name)
        set_bucket_policy(s3_client, args.bucket_name, new_policy)
    elif current_policy == "Error":
        print("An error occurred while retrieving the bucket policy.")
    else:
        print("A policy already exists for this bucket.")


if __name__ == "__main__":
    main()
