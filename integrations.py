# import boto3
# import datetime
# from tabulate import tabulate

# # AWS credentials and region
# aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
# aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# aws_region = 'ap-south-1'  # Replace with your desired AWS region

# # Initialize AWS clients
# ce = boto3.client(
#     'ce',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# cloudwatch = boto3.client(
#     'cloudwatch',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# # Specify the time period for cost data
# start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
# end_date = datetime.datetime.now().strftime('%Y-%m-%d')

# time_period = {
#     'Start': start_date,
#     'End': end_date
# }

# # Define metrics for cost data
# cost_metrics = ['NormalizedUsageAmount']

# # Fetch cost and usage data
# cost_response = ce.get_cost_and_usage(
#     TimePeriod=time_period,
#     Granularity='MONTHLY',  # Change granularity as needed
#     Metrics=cost_metrics,
#     GroupBy=[
#         {
#             'Type': 'DIMENSION',
#             'Key': 'SERVICE'
#         }
#     ]
# )

# # Fetch EC2 instance IDs with a specific tag (modify as needed)
# ec2_tag_key = 'Environment'
# ec2_tag_value = 'Production'

# ec2_client = boto3.client(
#     'ec2',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# ec2_response = ec2_client.describe_instances(
#     Filters=[
#         {
#             'Name': f'tag:{ec2_tag_key}',
#             'Values': [ec2_tag_value],
#         },
#     ]
# )

# ec2_instance_ids = [instance['InstanceId'] for reservation in ec2_response['Reservations'] for instance in reservation['Instances']]

# # Fetch CPU utilization metrics for EC2 instances
# ec2_metric_names = ['CPUUtilization']
# ec2_metrics_data = {}

# for instance_id in ec2_instance_ids:
#     ec2_metrics_data[instance_id] = {}
#     for metric_name in ec2_metric_names:
#         response = cloudwatch.get_metric_data(
#             MetricDataQueries=[
#                 {
#                     'Id': 'm1',
#                     'MetricStat': {
#                         'Metric': {
#                             'Namespace': 'AWS/EC2',
#                             'MetricName': metric_name,
#                             'Dimensions': [
#                                 {
#                                     'Name': 'InstanceId',
#                                     'Value': instance_id
#                                 },
#                             ],
#                         },
#                         'Period': 300,
#                         'Stat': 'Average',
#                     },
#                     'ReturnData': True,
#                 },
#             ],
#             StartTime=start_date,
#             EndTime=end_date,
#         )
#         if 'MetricDataResults' in response and response['MetricDataResults']:
#             ec2_metrics_data[instance_id][metric_name] = response['MetricDataResults'][0]['Values']

# # Fetch RDS DB instance identifier (modify as needed)
# rds_instance_identifier = 'YOUR_RDS_INSTANCE_IDENTIFIER'

# rds_client = boto3.client(
#     'rds',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# # Fetch CPU utilization metrics for RDS DB instance
# rds_metric_names = ['CPUUtilization']
# rds_metrics_data = {}

# for metric_name in rds_metric_names:
#     response = cloudwatch.get_metric_data(
#         MetricDataQueries=[
#             {
#                 'Id': 'm1',
#                 'MetricStat': {
#                     'Metric': {
#                         'Namespace': 'AWS/RDS',
#                         'MetricName': metric_name,
#                         'Dimensions': [
#                             {
#                                 'Name': 'DBInstanceIdentifier',
#                                 'Value': rds_instance_identifier
#                             },
#                         ],
#                     },
#                     'Period': 300,
#                     'Stat': 'Average',
#                 },
#                 'ReturnData': True,
#             },
#         ],
#         StartTime=start_date,
#         EndTime=end_date,
#     )
#     if 'MetricDataResults' in response and response['MetricDataResults']:
#         rds_metrics_data[metric_name] = response['MetricDataResults'][0]['Values']

# # Print cost data
# print("Cost Explorer Data:")
# print(f"{'AWS Service':<40}{'Usage Amount':<20}")
# cost_table_data = []

# for result in cost_response['ResultsByTime']:
#     for group in result['Groups']:
#         service = group['Keys'][0]
#         usage_amount = float(group['Metrics']['NormalizedUsageAmount']['Amount'])
#         currency = group['Metrics']['NormalizedUsageAmount']['Unit']
#         formatted_usage_amount = f"{usage_amount:.2f} {currency}"
#         cost_table_data.append([service, formatted_usage_amount])

# cost_table = tabulate(cost_table_data, headers=['AWS Service', 'Usage Amount'], tablefmt='pretty')
# print(cost_table)

# # Print EC2 CPU utilization data
# print("\nEC2 CPU Utilization Data:")
# for instance_id, metrics in ec2_metrics_data.items():
#     print(f"Instance ID: {instance_id}")
#     for metric_name, data in metrics.items():
#         if data:
#             print(f"Metric: {metric_name}, Data: {data}")
#         else:
#             print(f"Metric: {metric_name}, Data: []")

# # Print RDS CPU utilization data
# print("\nRDS CPU Utilization Data:")
# for metric_name, data in rds_metrics_data.items():
#     if data:
#         print(f"Metric: {metric_name}, Data: {data}")
#     else:
#         print(f"Metric: {metric_name}, Data: []")

# ---------------------------------------------------------------------------------------------------------------------

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

# # Initialize the RDS client with your credentials and region
# rds = boto3.client(
#     'rds',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# # Initialize the AWS Cost Explorer client with your credentials and region
# ce = boto3.client(
#     'ce',
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

# # Function to fetch CPU and Memory utilization metrics for EC2 instances
# def get_ec2_metrics(instance_ids, start_time, end_time):
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
#                 logger.info(f"EC2 - Resource: {instance_id}, Metric: {metric_name}, Data: {response['MetricDataResults'][0]['Values']}")
#             except Exception as e:
#                 logger.error(f"Error fetching EC2 metric for Resource: {instance_id}, Metric: {metric_name}: {str(e)}")

# # Function to fetch CPU utilization metrics for RDS instances
# def get_rds_metrics(db_instance_identifier, start_time, end_time):
#     metric_name = 'CPUUtilization'

#     try:
#         response = cloudwatch.get_metric_data(
#             MetricDataQueries=[
#                 {
#                     'Id': 'm1',
#                     'MetricStat': {
#                         'Metric': {
#                             'Namespace': 'AWS/RDS',
#                             'MetricName': metric_name,
#                             'Dimensions': [
#                                 {
#                                     'Name': 'DBInstanceIdentifier',
#                                     'Value': db_instance_identifier
#                                 },
#                             ],
#                         },
#                         'Period': 300,  # Adjust the period as needed
#                         'Stat': 'Average',  # You can change this to other statistics like 'Maximum', 'Minimum', etc.
#                     },
#                     'ReturnData': True,
#                 },
#             ],
#             StartTime=start_time,
#             EndTime=end_time,
#         )
#         logger.info(f"RDS - Metric: {metric_name} for DB Instance: {db_instance_identifier}, Data: {response['MetricDataResults'][0]['Values']}")
#     except Exception as e:
#         logger.error(f"Error fetching RDS metric for DB Instance: {db_instance_identifier}, Metric: {metric_name}: {str(e)}")

# # Function to fetch AWS Cost Explorer data
# def get_cost_explorer_data(start_time, end_time):
#     try:
#         response = ce.get_cost_and_usage(
#             TimePeriod={
#                 'Start': start_time.strftime('%Y-%m-%d'),
#                 'End': end_time.strftime('%Y-%m-%d')
#             },
#             Granularity='DAILY',
#             Metrics=['UnblendedCost'],  # You can modify the metrics as needed
#         )

#         for result in response['ResultsByTime']:
#             time_period = result['TimePeriod']['Start'] + ' to ' + result['TimePeriod']['End']
#             cost = result['Total']['UnblendedCost']['Amount']
#             logger.info(f"Time Period: {time_period}, Cost: {cost} USD")
#     except Exception as e:
#         logger.error(f"Error fetching AWS Cost Explorer data: {str(e)}")

# # Get EC2 instance IDs with the specified tag
# instance_ids_with_tag = get_instance_ids_with_tag(tag_key, tag_value)

# # Fetch metrics for the instances with the specified tag for the last hour
# print("EC2")
# end_time = datetime.utcnow()
# start_time = end_time - timedelta(hours=1)
# get_ec2_metrics(instance_ids_with_tag, start_time, end_time)

# # Fetch CPU utilization metrics for RDS instances
# print("RDS")
# rds_db_instance_identifier = 'YOUR_DB_INSTANCE_IDENTIFIER'
# get_rds_metrics(rds_db_instance_identifier, start_time, end_time)

# # Fetch AWS Cost Explorer data for the current month
# print("Cost Explorer")
# end_time = datetime.utcnow()
# start_time = end_time.replace(day=1)  # Start of the current month
# get_cost_explorer_data(start_time, end_time)


# -------------------------------------------------------------------------------------------------------------------------

import boto3
from datetime import datetime, timedelta

# Replace with your AWS credentials and region
aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
aws_region = 'ap-south-1'  # Replace with your AWS region

# Initialize the CloudWatch client with your credentials and region
cloudwatch = boto3.client(
    'cloudwatch',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Initialize the EC2 client with your credentials and region
ec2 = boto3.client(
    'ec2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Initialize the RDS client with your credentials and region
rds = boto3.client(
    'rds',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Initialize the AWS Cost Explorer client with your credentials and region
ce = boto3.client(
    'ce',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Fetch the DB instance identifier
def get_db_instance_identifier():
    response = rds.describe_db_instances()
    if 'DBInstances' in response:
        # Assuming you want the first DB instance found
        if len(response['DBInstances']) > 0:
            return response['DBInstances'][0]['DBInstanceIdentifier']
    return None

# Get the EC2 instance IDs with a specific tag
def get_ec2_instance_ids_with_tag(tag_key, tag_value):
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': f'tag:{tag_key}',
                'Values': [tag_value],
            },
        ]
    )
    instance_ids = [] 
    print(response)
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    return instance_ids

# Get the DB instance identifier
db_instance_identifier = get_db_instance_identifier()

if db_instance_identifier:
    # Specify the metric name and namespace for the RDS metric you want to fetch
    metric_name_rds = 'CPUUtilization'  # Replace with the desired RDS metric name
    namespace_rds = 'AWS/RDS'  # The namespace for RDS metrics

    # Set the time range for the RDS metric data retrieval
    end_time_rds = datetime.utcnow()
    start_time_rds = end_time_rds - timedelta(hours=1)  # Adjust the time range as needed

    # Fetch the RDS metric data
    response_rds = cloudwatch.get_metric_data(
        MetricDataQueries=[
            {
                'Id': 'm1',
                'MetricStat': {
                    'Metric': {
                        'Namespace': namespace_rds,
                        'MetricName': metric_name_rds,
                        'Dimensions': [
                            {
                                'Name': 'DBInstanceIdentifier',
                                'Value': db_instance_identifier
                            },
                        ],
                    },
                    'Period': 300,  # Adjust the period as needed (e.g., 5 minutes)
                    'Stat': 'Average',  # You can change this to other statistics like 'Maximum', 'Minimum', etc.
                },
                'ReturnData': True,
            },
        ],
        StartTime=start_time_rds,
        EndTime=end_time_rds,
    )

    # Print the RDS metric data
    print(f"RDS CPU Utilization Data:")
    print(f"Metric: {metric_name_rds}, Data: {response_rds['MetricDataResults'][0]['Values']}")

else:
    print("No RDS DB instances found.")

# Get EC2 instance IDs with a specific tag
tag_key_ec2 = 'Environment'
tag_value_ec2 = 'Production'
instance_ids_with_tag_ec2 = get_ec2_instance_ids_with_tag(tag_key_ec2, tag_value_ec2)

# Fetch CPU utilization metric for EC2 instances with the specified tag
def get_ec2_cpu_utilization(instance_ids):
    metric_name_ec2 = 'CPUUtilization'  # Replace with the desired EC2 metric name
    namespace_ec2 = 'AWS/EC2'  # The namespace for EC2 metrics

    # Set the time range for the EC2 metric data retrieval
    end_time_ec2 = datetime.utcnow()
    start_time_ec2 = end_time_ec2 - timedelta(hours=1)  # Adjust the time range as needed

    for instance_id in instance_ids:
        response_ec2 = cloudwatch.get_metric_data(
            MetricDataQueries=[
                {
                    'Id': 'm1',
                    'MetricStat': {
                        'Metric': {
                            'Namespace': namespace_ec2,
                            'MetricName': metric_name_ec2,
                            'Dimensions': [
                                {
                                    'Name': 'InstanceId',
                                    'Value': instance_id
                                },
                            ],
                        },
                        'Period': 300,  # Adjust the period as needed (e.g., 5 minutes)
                        'Stat': 'Average',  # You can change this to other statistics like 'Maximum', 'Minimum', etc.
                    },
                    'ReturnData': True,
                },
            ],
            StartTime=start_time_ec2,
            EndTime=end_time_ec2,
        )

        # Print the EC2 metric data
        print(f"EC2 CPU Utilization Data:")
        print(f"Instance ID: {instance_id}")
        print(f"Metric: {metric_name_ec2}, Data: {response_ec2['MetricDataResults'][0]['Values']}")
        print()

# Fetch metrics for EC2 instances with the specified tag
get_ec2_cpu_utilization(instance_ids_with_tag_ec2)

# Get AWS Cost Explorer cost data
def get_cost_explorer_cost_data():
    # Set the time period for AWS Cost Explorer
    end_time_ce = datetime.utcnow()
    start_time_ce = end_time_ce - timedelta(days=30)  # Adjust the time range as needed

    # Fetch the AWS Cost Explorer cost data
    response_ce = ce.get_cost_and_usage(
        TimePeriod={
            'Start': start_time_ce.strftime('%Y-%m-%d'),
            'End': end_time_ce.strftime('%Y-%m-%d'),
        },
        Granularity='DAILY',  # You can change this to other granularities like 'MONTHLY'
        Metrics=['BlendedCost'],  # You can specify other cost metrics here
    )

    # Print the AWS Cost Explorer cost data
    print("AWS Cost Explorer Cost Data:")
    for result in response_ce['ResultsByTime']:
        print(f"Time Period: {result['TimePeriod']['Start']} to {result['TimePeriod']['End']}, Cost: {result['Total']['BlendedCost']['Amount']} {result['Total']['BlendedCost']['Unit']}")
    print()
# Fetch AWS Cost Explorer cost data
get_cost_explorer_cost_data()
