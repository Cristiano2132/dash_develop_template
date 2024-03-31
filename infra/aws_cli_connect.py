import os
import subprocess


class AwsCliConnect:
    def __init__(self) -> None:
        self.aws_default_region = os.getenv('AWS_DEFAULT_REGION')
        self.aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        self.aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.__check_aws_cli()

    def __check_aws_cli(self) -> bool:
        try:
            subprocess.check_output(['aws', '--version'])
            res = self.__check_aws_credentials()
            if not res:
                print('AWS credentials not found, plses set the environment variables')
                raise Exception(
                    'AWS credentials not found, plses set the environment variables')
        except Exception as e:
            print(e)
            return False

    def __check_aws_credentials(self) -> bool:
        if self.aws_default_region is None:
            return False
        if self.aws_access_key_id is None:
            return False
        if self.aws_secret_access_key is None:
            return False
        return True

    def aws_cli_download_object_from_s3(self, bucket_name: str, object_key: str, local_path: str) -> None:
        try:
            cmd = f'aws s3 cp "s3://{bucket_name}/{object_key}" "{local_path}"'
            subprocess.check_output(cmd, shell=True)

        except Exception as e:
            print(e)
            raise Exception(e)

    def aws_cli_upload_object_to_s3(self, bucket_name: str, object_key: str, source: str) -> None:
        try:
            cmd = f'aws s3 cp "{source}" "s3://{bucket_name}/{object_key}"'
            subprocess.check_output(cmd, shell=True)

        except Exception as e:
            print(e)
            raise Exception(e)
