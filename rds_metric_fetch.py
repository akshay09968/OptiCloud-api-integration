# import boto3
# from datetime import datetime, timedelta

# # Replace with your AWS credentials and region
# aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
# aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# aws_region = 'ap-south-1'  # Replace with your AWS region

# # Initialize the CloudWatch client with your credentials and region
# cloudwatch = boto3.client(
#     'cloudwatch',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# # Initialize the RDS client with your credentials and region
# rds = boto3.client(
#     'rds',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# # Fetch the DB instance identifier
# def get_db_instance_identifier():
#     response = rds.describe_db_instances()
#     if 'DBInstances' in response:
#         # Assuming you want the first DB instance found
#         if len(response['DBInstances']) > 0:
#             return response['DBInstances'][0]['DBInstanceIdentifier']
#     return None

# # Get the DB instance identifier
# db_instance_identifier = get_db_instance_identifier()

# if db_instance_identifier:
#     # Specify the metric name and namespace for the RDS metric you want to fetch
#     metric_name = 'CPUUtilization'  # Replace with the desired metric name
#     namespace = 'AWS/RDS'  # The namespace for RDS metrics

#     # Set the time range for the metric data retrieval
#     end_time = datetime.utcnow()
#     start_time = end_time - timedelta(hours=1)  # Adjust the time range as needed

#     # Fetch the metric data
#     response = cloudwatch.get_metric_data(
#         MetricDataQueries=[
#             {
#                 'Id': 'm1',
#                 'MetricStat': {
#                     'Metric': {
#                         'Namespace': namespace,
#                         'MetricName': metric_name,
#                         'Dimensions': [
#                             {
#                                 'Name': 'DBInstanceIdentifier',
#                                 'Value': db_instance_identifier
#                             },
#                         ],
#                     },
#                     'Period': 300,  # Adjust the period as needed (e.g., 5 minutes)
#                     'Stat': 'Average',  # You can change this to other statistics like 'Maximum', 'Minimum', etc.
#                 },
#                 'ReturnData': True,
#             },
#         ],
#         StartTime=start_time,
#         EndTime=end_time,
#     )

#     # Print the metric data
#     print(f"Metric: {metric_name} for DB Instance: {db_instance_identifier}")
#     for result in response['MetricDataResults']:
#         timestamps = result['Timestamps']
#         values = result['Values']
#         for timestamp, value in zip(timestamps, values):
#             print(f"Timestamp: {timestamp}, Value: {value}")
# else:
#     print("No RDS DB instances found.")

# -----------------------------------------------------------------------------------------------------------------------------

# import boto3
# from datetime import datetime, timedelta

# # Replace with your AWS credentials and region
# aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
# aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# aws_region = 'ap-south-1'  # Replace with your AWS region

# # Initialize the CloudWatch client with your credentials and region
# cloudwatch = boto3.client(
#     'cloudwatch',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# # Initialize the RDS client with your credentials and region
# rds = boto3.client(
#     'rds',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# # Fetch the DB instance identifier
# def get_db_instance_identifier():
#     response = rds.describe_db_instances()
#     if 'DBInstances' in response:
#         # Assuming you want the first DB instance found
#         if len(response['DBInstances']) > 0:
#             return response['DBInstances'][0]['DBInstanceIdentifier']
#     return None

# # Get the DB instance identifier
# db_instance_identifier = get_db_instance_identifier()

# if db_instance_identifier:
#     # Specify the metric name and namespace for the RDS metric you want to fetch
#     metric_name_rds = 'CPUUtilization'  # Replace with the desired RDS metric name
#     namespace_rds = 'AWS/RDS'  # The namespace for RDS metrics

#     # Set the time range for the RDS metric data retrieval
#     end_time_rds = datetime.utcnow()
#     start_time_rds = end_time_rds - timedelta(hours=1)  # Adjust the time range as needed

#     # Fetch the RDS metric data
#     response_rds = cloudwatch.get_metric_data(
#         MetricDataQueries=[
#             {
#                 'Id': 'm1',
#                 'MetricStat': {
#                     'Metric': {
#                         'Namespace': namespace_rds,
#                         'MetricName': metric_name_rds,
#                         'Dimensions': [
#                             {
#                                 'Name': 'DBInstanceIdentifier',
#                                 'Value': db_instance_identifier
#                             },
#                         ],
#                     },
#                     'Period': 300,  # Adjust the period as needed (e.g., 5 minutes)
#                     'Stat': 'Average',  # You can change this to other statistics like 'Maximum', 'Minimum', etc.
#                 },
#                 'ReturnData': True,
#             },
#         ],
#         StartTime=start_time_rds,
#         EndTime=end_time_rds,
#     )

#     # Print the RDS metric data
#     print(f"RDS CPU Utilization Data:")
#     print(f"Metric: {metric_name_rds}, Data: {response_rds['MetricDataResults'][0]['Values']}")

# else:
#     print("No RDS DB instances found.")

#--------------------------------------------------------------------------------------------------------------------------

# import os
# import boto3
# from datetime import datetime, timedelta

# # Set your AWS credentials as environment variables
# # os.environ['AWS_ACCESS_KEY_ID'] = 'AKIA34REAOZJ5WNWQHTS'
# # os.environ['AWS_SECRET_ACCESS_KEY'] = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# # os.environ['AWS_REGION'] = 'ap-south-1'

# aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
# aws_secret_access_key = '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'
# aws_region = 'ap-south-1'

# def get_rds_instances_by_tags(tag_key, tag_value):
#     # Create an RDS client
#     rds_client = boto3.client('rds',
#         aws_access_key_id=aws_access_key_id,
#         aws_secret_access_key=aws_secret_access_key,
#         region_name=aws_region)

#     # Describe all RDS instances
#     response = rds_client.describe_db_instances()

#     instances = []

#     for instance in response['DBInstances']:
#         # Fetch tags for the instance
#         instance_tags = rds_client.list_tags_for_resource(ResourceName=instance['DBInstanceArn'])['TagList']

#         # Check if the specified tag key and value exist for the instance
#         if any(tag['Key'] == tag_key and tag['Value'] == tag_value for tag in instance_tags):
#             instance_info = {
#                 'DBInstanceIdentifier': instance['DBInstanceIdentifier'],
#                 'DBInstanceClass': instance['DBInstanceClass'],
#                 'DBInstanceStatus': instance['DBInstanceStatus'],
#                 'Tags': instance_tags
#             }
#             instances.append(instance_info)

#     return instances

# def get_rds_cpu_utilization(db_instance_identifier, start_time, end_time):
#     cloudwatch_client = boto3.client('cloudwatch',
#         aws_access_key_id=aws_access_key_id,
#         aws_secret_access_key=aws_secret_access_key,
#         region_name=aws_region)

#     # Get CPU utilization metrics data
#     response = cloudwatch_client.get_metric_statistics(
#         Namespace='AWS/RDS',
#         MetricName='CPUUtilization',
#         Dimensions=[
#             {
#                 'Name': 'DBInstanceIdentifier',
#                 'Value': db_instance_identifier
#             },
#         ],
#         StartTime=start_time,
#         EndTime=end_time,
#         Period=300,  # 5-minute intervals
#         Statistics=['Average'],
#         Unit='Percent'
#     )

#     return response['Datapoints']

# def get_rds_cost(db_instance_class, start_time, end_time):
#     # Create a Cost Explorer client
#     ce_client = boto3.client('ce',
#         aws_access_key_id=aws_access_key_id,
#         aws_secret_access_key=aws_secret_access_key,
#         region_name=aws_region)

#     # Get cost data
#     response = ce_client.get_cost_and_usage(
#         TimePeriod={
#             'Start': start_time.strftime('%Y-%m-%d'),
#             'End': end_time.strftime('%Y-%m-%d')
#         },
#         Granularity='DAILY',
#         Metrics=['UnblendedCost'],
#         # Filter={
#         #     'Dimensions': {
#         #         'Key': 'RDS_DB_INSTANCE_CLASS',
#         #         'Values': [db_instance_class]
#         #     }
#         # }
#     )

#     return response['ResultsByTime']

# if __name__ == '__main__':
#     # Replace 'YourTagKey' and 'YourTagValue' with the actual key and value of the tags
#     tag_key = 'mc'
#     tag_value = 'stan'

#     rds_instances = get_rds_instances_by_tags(tag_key, tag_value)


#     if rds_instances:
#         print("RDS Instances:")
#         for rds_instance in rds_instances:
#             print(f"DB Instance Identifier: {rds_instance['DBInstanceIdentifier']}")
#             print(f"DB Instance Class: {rds_instance['DBInstanceClass']}")
#             print(f"DB Instance Status: {rds_instance['DBInstanceStatus']}")
#             print(f"Tags: {rds_instance['Tags']}")

#             # Get CPU Utilization metrics
#             print("\nCPU Utilization Metrics:")
#             start_time1 = datetime.utcnow() - timedelta(minutes=10)  # Last 6 hours
#             end_time1 = datetime.utcnow()
#             metrics_data = get_rds_cpu_utilization(rds_instance['DBInstanceIdentifier'], start_time1, end_time1)

#             for datapoint in metrics_data:
#                 timestamp = datapoint['Timestamp'].strftime('%Y-%m-%d %H:%M:%S')
#                 value = datapoint['Average']
#                 print(f"{timestamp} - CPU Utilization: {value}%")

#             print("-----")

#             end_time = datetime.utcnow()
#             start_time = end_time - timedelta(days=1)

#             # Get and print cost data
#             cost_data = get_rds_cost(rds_instance['DBInstanceClass'], start_time, end_time)

#             print(f"Cost data for DB instance {rds_instance['DBInstanceIdentifier']} from {start_time} to {end_time}:")

#             for result in cost_data:
#                 timestamp = result['TimePeriod']['Start']
#                 value = result['Total']['UnblendedCost']['Amount']
#                 print(f"{rds_instance['DBInstanceIdentifier']} - {timestamp} - Cost: ${value}")

#             print("-----")
#     else:
#         print("No RDS instances found with the specified tags.")

# ----------------------------------------------------------------------------------------------------------

# import os
# import boto3
# from datetime import datetime, timedelta

# # Set your AWS credentials as environment variables
# # os.environ['AWS_ACCESS_KEY_ID'] = 'AKIARWCTPADXXM6BOGUA'
# # os.environ['AWS_SECRET_ACCESS_KEY'] = 'BO+7r0vPZ5igYAS/Ybt+Owvx/DPA304x7oNtdeOs'
# # os.environ['AWS_REGION'] = 'ap-south-1'

# aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
# aws_secret_access_key = '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'
# aws_region = 'ap-south-1' 

# def get_rds_instances_by_tags(tag_key, tag_value):
#     # Create an RDS client
#     rds_client = boto3.client('rds',
#         aws_access_key_id=aws_access_key_id,
#         aws_secret_access_key=aws_secret_access_key,
#         region_name=aws_region)

#     # Describe all RDS instances
#     response = rds_client.describe_db_instances()

#     instances = []

#     for instance in response['DBInstances']:
#         # Fetch tags for the instance
#         instance_tags = rds_client.list_tags_for_resource(ResourceName=instance['DBInstanceArn'])['TagList']

#         # Check if the specified tag key and value exist for the instance
#         if any(tag['Key'] == tag_key and tag['Value'] == tag_value for tag in instance_tags):
#             instance_info = {
#                 'DBInstanceIdentifier': instance['DBInstanceIdentifier'],
#                 'DBInstanceClass': instance['DBInstanceClass'],
#                 'DBInstanceStatus': instance['DBInstanceStatus'],
#                 'Tags': instance_tags
#             }
#             instances.append(instance_info)

#     return instances

# def get_rds_cpu_utilization(db_instance_identifier, start_time, end_time):
#     cloudwatch_client = boto3.client('cloudwatch',
#         aws_access_key_id=aws_access_key_id,
#         aws_secret_access_key=aws_secret_access_key,
#         region_name=aws_region)

#     # Get CPU utilization metrics data
#     response = cloudwatch_client.get_metric_statistics(
#         Namespace='AWS/RDS',
#         MetricName='CPUUtilization',
#         Dimensions=[
#             {
#                 'Name': 'DBInstanceIdentifier',
#                 'Value': db_instance_identifier
#             },
#         ],
#         StartTime=start_time,
#         EndTime=end_time,
#         Period=300,  # 5-minute intervals
#         Statistics=['Average'],
#         Unit='Percent'
#     )

#     return response['Datapoints']

# def get_rds_cost(db_instance_identifier, start_time, end_time):
#     # Create a Cost Explorer client
#     ce_client = boto3.client('ce',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region)
#     rds_client = boto3.client('rds',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region)
#     instance_tags = rds_client.list_tags_for_resource(ResourceName=f"arn:aws:rds:ap-south-1:116139163887:db:{db_instance_identifier}")['TagList']

#     # Get cost data
#     response = ce_client.get_cost_and_usage(
#         TimePeriod={
#             'Start': start_time.strftime('%Y-%m-%d'),
#             'End': end_time.strftime('%Y-%m-%d')
#         },
#         Granularity='DAILY',
#         Metrics=['UnblendedCost'],
#         Filter={
#             'Dimensions': {
#                 'Key': 'INSTANCE_TYPE',
#                 'Values': [f'{tag["Value"]}' for tag in instance_tags if tag["Key"] == tag_key]
#             }
#         }
#     )

#     return response['ResultsByTime']

# if __name__ == '__main__':
#     # Replace 'YourTagKey' and 'YourTagValue' with the actual key and value of the tags
#     tag_key = 'mc'
#     tag_value = 'stan'

#     rds_instances = get_rds_instances_by_tags(tag_key, tag_value)


#     if rds_instances:
#         print("RDS Instances:")
#         for rds_instance in rds_instances:
#             print(f"DB Instance Identifier: {rds_instance['DBInstanceIdentifier']}")
#             print(f"DB Instance Class: {rds_instance['DBInstanceClass']}")
#             print(f"DB Instance Status: {rds_instance['DBInstanceStatus']}")
#             print(f"Tags: {rds_instance['Tags']}")

#             # Get CPU Utilization metrics
#             print("\nCPU Utilization Metrics:")
#             start_time1 = datetime.utcnow() - timedelta(hours=6)  # Last 6 hours
#             end_time1 = datetime.utcnow()
#             metrics_data = get_rds_cpu_utilization(rds_instance['DBInstanceIdentifier'], start_time1, end_time1)

#             for datapoint in metrics_data:
#                 timestamp = datapoint['Timestamp'].strftime('%Y-%m-%d %H:%M:%S')
#                 value = datapoint['Average']
#                 print(f"{timestamp} - CPU Utilization: {value}%")

#             print("-----")

#             end_time = datetime.utcnow()
#             start_time = end_time - timedelta(days=1)

#             # Get and print cost data
#             cost_data = get_rds_cost(rds_instance['DBInstanceIdentifier'], start_time, end_time)

#             print(f"Cost data for DB instance {rds_instance['DBInstanceIdentifier']} from {start_time} to {end_time}:")
#             print(cost_data)
#             for result in cost_data:
#                 timestamp = result['TimePeriod']['Start']
#                 value = result['Total']['UnblendedCost']['Amount']
#                 print(f"{rds_instance['DBInstanceIdentifier']} - {timestamp} - Cost: ${value}")

#             print("-----")
#     else:
#         print("No RDS instances found with the specified tags.")


# ---------------------------------------------------------------------------------------------------------------------

import os
import boto3
from datetime import datetime, timedelta

# Set your AWS credentials as environment variables
# os.environ['AWS_ACCESS_KEY_ID'] = 'AKIA34REAOZJ5WNWQHTS'
# os.environ['AWS_SECRET_ACCESS_KEY'] = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# os.environ['AWS_REGION'] = 'ap-south-1'

aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
aws_secret_access_key = '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'
aws_region = 'ap-south-1' 

def get_rds_instances_by_tags(tag_key, tag_value):
    # Create an RDS client
    rds_client = boto3.client('rds',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region)

    # Describe all RDS instances
    response = rds_client.describe_db_instances()

    instances = []

    for instance in response['DBInstances']:
        # Fetch tags for the instance
        instance_tags = rds_client.list_tags_for_resource(ResourceName=instance['DBInstanceArn'])['TagList']

        # Check if the specified tag key and value exist for the instance
        if any(tag['Key'] == tag_key and tag['Value'] == tag_value for tag in instance_tags):
            instance_info = {
                'DBInstanceIdentifier': instance['DBInstanceIdentifier'],
                'DBInstanceClass': instance['DBInstanceClass'],
                'DBInstanceStatus': instance['DBInstanceStatus'],
                'Tags': instance_tags
            }
            instances.append(instance_info)

    return instances

def get_rds_cpu_utilization(db_instance_identifier, start_time, end_time):
    cloudwatch_client = boto3.client('cloudwatch',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region)

    # Get CPU utilization metrics data
    response = cloudwatch_client.get_metric_statistics(
        Namespace='AWS/RDS',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'DBInstanceIdentifier',
                'Value': db_instance_identifier
            },
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,  # 5-minute intervals
        Statistics=['Average'],
        Unit='Percent'
    )

    return response['Datapoints']

def get_rds_cost(db_instance_identifier, start_time, end_time):
    # Create a Cost Explorer client
    ce_client = boto3.client('ce',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region)
    
    rds_client = boto3.client('rds',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region)
    instance_tags = rds_client.list_tags_for_resource(ResourceName=f"arn:aws:rds:ap-south-1:817193055827:db:{db_instance_identifier}")['TagList']

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
                'Values': [f'{tag["Value"]}' for tag in instance_tags if tag["Key"] == tag_key]
            }
        }
    )

    return response['ResultsByTime']

if __name__ == '__main__':
    # Replace 'YourTagKey' and 'YourTagValue' with the actual key and value of the tags
    tag_key = 'mc'
    tag_value = 'stan'

    rds_instances = get_rds_instances_by_tags(tag_key, tag_value)


    if rds_instances:
        print("RDS Instances:")
        for rds_instance in rds_instances:
            print(f"DB Instance Identifier: {rds_instance['DBInstanceIdentifier']}")
            print(f"DB Instance Class: {rds_instance['DBInstanceClass']}")
            print(f"DB Instance Status: {rds_instance['DBInstanceStatus']}")
            print(f"Tags: {rds_instance['Tags']}")

            # Get CPU Utilization metrics
            print("\nCPU Utilization Metrics:")
            start_time1 = datetime.utcnow() - timedelta(hours=6)  # Last 6 hours
            end_time1 = datetime.utcnow()
            metrics_data = get_rds_cpu_utilization(rds_instance['DBInstanceIdentifier'], start_time1, end_time1)

            for datapoint in metrics_data:
                timestamp = datapoint['Timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                value = datapoint['Average']
                print(f"{timestamp} - CPU Utilization: {value}%")

            print("-----")

            end_time = datetime.utcnow()
            start_time = end_time - timedelta(days=5)

            # Get and print cost data
            cost_data = get_rds_cost(rds_instance['DBInstanceIdentifier'], start_time, end_time)

            print(f"Cost data for DB instance {rds_instance['DBInstanceIdentifier']} from {start_time} to {end_time}:")
            print(cost_data)
            for result in cost_data:
                timestamp = result['TimePeriod']['Start']
                value = result['Total']['UnblendedCost']['Amount']
                print(f"{rds_instance['DBInstanceIdentifier']} - {timestamp} - Cost: ${value}")

            print("-----")
    else:
        print("No RDS instances found with the specified tags.")
