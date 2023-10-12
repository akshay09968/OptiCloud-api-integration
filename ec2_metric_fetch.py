# # import boto3

# # # Specify your AWS credentials and region
# # aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
# # aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# # aws_region = 'ap-south-1'  # Replace with your desired AWS region

# # # Initialize the CloudWatch client with your credentials and region
# # cloudwatch = boto3.client(
# #     'cloudwatch',
# #     aws_access_key_id=aws_access_key_id,
# #     aws_secret_access_key=aws_secret_access_key,
# #     region_name=aws_region
# # )

# # # Specify the tag key and value for filtering EC2 instances
# # tag_key = 'Environment'
# # tag_value = 'Production'

# # # Fetch EC2 instance IDs with the specified tag
# # ec2_client = boto3.client('ec2',
# #     aws_access_key_id=aws_access_key_id,
# #     aws_secret_access_key=aws_secret_access_key,
# #     region_name=aws_region
# # )

# # response = ec2_client.describe_instances(
# #     Filters=[
# #         {
# #             'Name': f'tag:{tag_key}',
# #             'Values': [tag_value],
# #         },
# #     ]
# # )

# # instance_ids = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

# # # Fetch CPU and memory utilization metrics for the instances with the specified tag
# # metric_names = ['CPUUtilization', 'MemoryUtilization']  # Replace with the desired metrics

# # for instance_id in instance_ids:
# #     for metric_name in metric_names:
# #         response = cloudwatch.get_metric_data(
# #             MetricDataQueries=[
# #                 {
# #                     'Id': 'm1',
# #                     'MetricStat': {
# #                         'Metric': {
# #                             'Namespace': 'AWS/EC2',
# #                             'MetricName': metric_name,
# #                             'Dimensions': [
# #                                 {
# #                                     'Name': 'InstanceId',
# #                                     'Value': instance_id
# #                                 },
# #                             ],
# #                         },
# #                         'Period': 60,  # Adjust the period as needed
# #                         'Stat': 'Minimum',  # You can change this to other statistics like 'Maximum', 'Minimum', etc.
# #                     },
# #                     'ReturnData': True,
# #                 },
# #             ],
# #             StartTime='2023-10-01T00:00:00Z',  # Adjust the start time as needed
# #             EndTime='2023-10-05T00:00:00Z',    # Adjust the end time as needed
# #         )
# #         print(f"Resource: {instance_id}, Metric: {metric_name}, Data: {response['MetricDataResults'][0]['Values']}")


# # ------------------------------------------------------------------------------------------------------------------------------------

# # import boto3
# # from datetime import datetime, timedelta

# # # Specify your AWS credentials and region
# # aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
# # aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# # aws_region = 'ap-south-1'  # Replace with your desired AWS region

# # # Initialize the CloudWatch client with your credentials and region
# # cloudwatch = boto3.client(
# #     'cloudwatch',
# #     aws_access_key_id=aws_access_key_id,
# #     aws_secret_access_key=aws_secret_access_key,
# #     region_name=aws_region
# # )

# # # Specify the tag key and value for filtering EC2 instances
# # tag_key = 'Environment'
# # tag_value = 'Production'

# # # Function to get EC2 instance IDs with the specified tag
# # def get_instance_ids_with_tag(tag_key, tag_value):
# #     ec2_client = boto3.client('ec2',
# #         aws_access_key_id=aws_access_key_id,
# #         aws_secret_access_key=aws_secret_access_key,
# #         region_name=aws_region
# #     )
# #     response = ec2_client.describe_instances(
# #         Filters=[
# #             {
# #                 'Name': f'tag:{tag_key}',
# #                 'Values': [tag_value],
# #             },
# #         ]
# #     )
# #     instance_ids = []
# #     for reservation in response['Reservations']:
# #         for instance in reservation['Instances']:
# #             instance_ids.append(instance['InstanceId'])
# #     return instance_ids

# # # Function to fetch CPU and Memory utilization metrics
# # def get_metrics_for_instances(instance_ids):
# #     metric_names = ['CPUUtilization', 'MemoryUtilization']
# #     end_time = datetime.utcnow()
# #     start_time = end_time - timedelta(hours=1)  # Adjust the time range as needed

# #     for instance_id in instance_ids:
# #         for metric_name in metric_names:
# #             response = cloudwatch.get_metric_data(
# #                 MetricDataQueries=[
# #                     {
# #                         'Id': 'm1',
# #                         'MetricStat': {
# #                             'Metric': {
# #                                 'Namespace': 'AWS/EC2',
# #                                 'MetricName': metric_name,
# #                                 'Dimensions': [
# #                                     {
# #                                         'Name': 'InstanceId',
# #                                         'Value': instance_id
# #                                     },
# #                                 ],
# #                             },
# #                             'Period': 300,  # Adjust the period as needed
# #                             'Stat': 'Average',  # You can change this to other statistics like 'Maximum', 'Minimum', etc.
# #                         },
# #                         'ReturnData': True,
# #                     },
# #                 ],
# #                 StartTime=start_time,
# #                 EndTime=end_time,
# #             )
# #             print(f"Resource: {instance_id}, Metric: {metric_name}, Data: {response['MetricDataResults'][0]['Values']}")

# # # Get EC2 instance IDs with the specified tag
# # instance_ids_with_tag = get_instance_ids_with_tag(tag_key, tag_value)

# # # Fetch metrics for the instances with the specified tag
# # get_metrics_for_instances(instance_ids_with_tag)

# # ------------------------------------------------------------------------------------------------------------------------------------

# import boto3
# from datetime import datetime, timedelta
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Specify your AWS credentials and region
# aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
# aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# aws_region = 'ap-south-1'  # Replace with your desired AWS region

# # Initialize the CloudWatch client with your credentials and region
# cloudwatch = boto3.client(
#     'cloudwatch',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# # Specify the tag key and value for filtering EC2 instances
# tag_key = 'Environment'
# tag_value = 'Production'

# # Function to get EC2 instance IDs with the specified tag
# def get_instance_ids_with_tag(tag_key, tag_value):
#     ec2_client = boto3.client('ec2',
#         aws_access_key_id=aws_access_key_id,
#         aws_secret_access_key=aws_secret_access_key,
#         region_name=aws_region
#     )
#     response = ec2_client.describe_instances(
#         Filters=[
#             {
#                 'Name': f'tag:{tag_key}',
#                 'Values': [tag_value],
#             },
#         ]
#     )
#     instance_ids = []
#     for reservation in response['Reservations']:
#         for instance in reservation['Instances']:
#             instance_ids.append(instance['InstanceId'])
#     return instance_ids

# # Function to fetch CPU and Memory utilization metrics
# def get_metrics_for_instances(instance_ids, start_time, end_time):
#     metric_names = ['CPUUtilization', 'MemoryUtilization']

#     for instance_id in instance_ids:
#         for metric_name in metric_names:
#             try:
#                 response = cloudwatch.get_metric_data(
#                     MetricDataQueries=[
#                         {
#                             'Id': 'm1',
#                             'MetricStat': {
#                                 'Metric': {
#                                     'Namespace': 'AWS/EC2',
#                                     'MetricName': metric_name,
#                                     'Dimensions': [
#                                         {
#                                             'Name': 'InstanceId',
#                                             'Value': instance_id
#                                         },
#                                     ],
#                                 },
#                                 'Period': 300,  # Adjust the period as needed
#                                 'Stat': 'Average',  # You can change this to other statistics like 'Maximum', 'Minimum', etc.
#                             },
#                             'ReturnData': True,
#                         },
#                     ],
#                     StartTime=start_time,
#                     EndTime=end_time,
#                 )
#                 logger.info(f"Resource: {instance_id}, Metric: {metric_name}, Data: {response['MetricDataResults'][0]['Values']}")
#             except Exception as e:
#                 logger.error(f"Error fetching metric for Resource: {instance_id}, Metric: {metric_name}: {str(e)}")

# # Get EC2 instance IDs with the specified tag
# instance_ids_with_tag = get_instance_ids_with_tag(tag_key, tag_value)

# # Fetch metrics for the instances with the specified tag for the last hour
# end_time = datetime.utcnow()
# start_time = end_time - timedelta(hours=1)
# get_metrics_for_instances(instance_ids_with_tag, start_time, end_time)

# -------------------------------------------------------------------------------------------------------------------------

import os
import boto3
from datetime import datetime, timedelta

# Set your AWS credentials as environment variables
# os.environ['AWS_ACCESS_KEY_ID'] = 'AKIA34REAOZJ5WNWQHTS'
# os.environ['AWS_SECRET_ACCESS_KEY'] = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# os.environ['AWS_REGION'] = 'ap-south-1'

aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
aws_region = 'ap-south-1'  # Replace with your desired AWS region

def get_instances_by_tags(tag_key, tag_value):
    # Create an EC2 client
    ec2_client = boto3.client('ec2',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region)
    
    # Describe instances based on tags
    response = ec2_client.describe_instances(
        Filters=[
            {
                'Name': f'tag:{tag_key}',
                'Values': [tag_value]
            }
        ]
    )

    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_info = {
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name'],
                'Tags': instance.get('Tags', [])
            }
            instances.append(instance_info)

    return instances

def get_ec2_metrics(instance_id, metric_name, start_time, end_time):
    cloudwatch_client = boto3.client('cloudwatch',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region)  

    # Get metrics data
    response = cloudwatch_client.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName=metric_name,
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': instance_id
            },
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,  # 5-minute intervals
        Statistics=['Average'],
        Unit='Percent'  # Or other units based on the metric
    )

    return response['Datapoints']

def get_cost_for_instance(instance_type, start_time, end_time):
    # Create a Cost Explorer client
    ce_client = boto3.client('ce',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region)

    # Get cost data
    response = ce_client.get_cost_and_usage(
        TimePeriod={
            'Start': start_time.strftime('%Y-%m-%d'),
            'End': end_time.strftime('%Y-%m-%d')
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost'],
        Filter={
            'Dimensions': {
                'Key': 'INSTANCE_TYPE',
                'Values': [instance_type]
            }
        }
    )

    return response['ResultsByTime']

if __name__ == '__main__':
    # Replace 'YourTagKey' and 'YourTagValue' with the actual key and value of the tags
    tag_key = 'Environment'
    tag_value = 'Production'

    instances = get_instances_by_tags(tag_key, tag_value)

    if instances:
        print("Instances:")
        for instance in instances:
            print(f"Instance ID: {instance['InstanceId']}")
            print(f"Instance Type: {instance['InstanceType']}")
            print(f"State: {instance['State']}")
            print(f"Tags: {instance['Tags']}")

            # Get CPU Utilization metrics
            print("\nCPU Utilization Metrics:")
            start_time1 = datetime.utcnow() - timedelta(hours=6)  # Last 6 hours
            end_time1 = datetime.utcnow()
            metrics_data = get_ec2_metrics(instance['InstanceId'], 'CPUUtilization', start_time1, end_time1)

            for datapoint in metrics_data:
                timestamp = datapoint['Timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                value = datapoint['Average']
                print(f"{timestamp} - CPU Utilization: {value}%")

            print("-----")

            end_time = datetime.utcnow()
            start_time = end_time - timedelta(days=7)

            # Get and print cost data
            cost_data = get_cost_for_instance(instance['InstanceType'], start_time, end_time)

            print(f"Cost data for instance {instance['InstanceId']} fro{start_time} to {end_time}:")

            for result in cost_data:
                timestamp = result['TimePeriod']['Start']
                value = result['Total']['UnblendedCost']['Amount']
                print(f"{instance['InstanceId']} - {timestamp} - Cost: ${value}")

            print("-----")
    else:
        print("No instances found with the specified tags.")
