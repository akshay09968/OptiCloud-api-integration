# # import boto3
# # import datetime

# # # Replace with your AWS credentials and region
# # aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
# # aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# # aws_region = 'ap-south-1'  # Replace with your AWS region

# # # Initialize the Cost Explorer client with your credentials and region
# # ce = boto3.client(
# #     'ce',
# #     aws_access_key_id=aws_access_key_id,
# #     aws_secret_access_key=aws_secret_access_key,
# #     region_name=aws_region
# # )

# # # Specify the time range for which you want to fetch cost data
# # start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
# # end_date = datetime.datetime.now().strftime('%Y-%m-%d')

# # # Define the granularity of the data (DAILY, MONTHLY, etc.)
# # time_period = {
# #     'Start': start_date,
# #     'End': end_date
# # }

# # # Define the metrics you want to retrieve (e.g., BlendedCost, UnblendedCost)
# # metrics = ['BlendedCost']

# # # Fetch cost and usage data
# # response = ce.get_cost_and_usage(
# #     TimePeriod=time_period,
# #     Granularity='DAILY',  # You can adjust the granularity as needed
# #     Metrics=metrics
# # )

# # # Print the cost data
# # for result in response['ResultsByTime']:
# #     start = result['TimePeriod']['Start']
# #     end = result['TimePeriod']['End']
# #     cost = result['Total']['BlendedCost']['Amount']
# #     currency = result['Total']['BlendedCost']['Unit']
# #     print(f"Time Period: {start} to {end}, Cost: {cost} {currency}")

# # ---------------------------------------------------------------------------------------------------------------------------

# # import boto3
# # import datetime

# # # Replace with your AWS credentials and region
# # aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
# # aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# # aws_region = 'ap-south-1'  # Replace with your desired AWS region

# # # Initialize the Cost Explorer client with your credentials and region
# # ce = boto3.client(
# #     'ce',
# #     aws_access_key_id=aws_access_key_id,
# #     aws_secret_access_key=aws_secret_access_key,
# #     region_name=aws_region
# # )

# # # Specify the time range for which you want to fetch cost data
# # start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
# # end_date = datetime.datetime.now().strftime('%Y-%m-%d')

# # # Define the granularity of the data (DAILY, MONTHLY, etc.)
# # time_period = {
# #     'Start': start_date,
# #     'End': end_date
# # }

# # # Define the metrics you want to retrieve (e.g., BlendedCost, UnblendedCost)
# # metrics = ['BlendedCost']

# # # Fetch cost and usage data
# # response = ce.get_cost_and_usage(
# #     TimePeriod=time_period,
# #     Granularity='DAILY',  # You can adjust the granularity as needed
# #     Metrics=metrics
# # )

# # # Print the cost data in a formatted table
# # print(f"{'Time Period':<30}{'Cost':<20}")

# # for result in response['ResultsByTime']:
# #     start = result['TimePeriod']['Start']
# #     end = result['TimePeriod']['End']
# #     cost = float(result['Total']['BlendedCost']['Amount'])
# #     currency = result['Total']['BlendedCost']['Unit']
# #     formatted_cost = f"{cost:.2f} {currency}"
# #     print(f"{start} to {end:<12}{formatted_cost:>20}")

# # ----------------------------------------------------------------------------------------------------------------------

# # import boto3
# # import datetime

# # # Replace with your AWS credentials and region
# # aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
# # aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# # aws_region = 'ap-south-1'  # Replace with your desired AWS region

# # # Initialize the Cost Explorer client with your credentials and region
# # ce = boto3.client(
# #     'ce',
# #     aws_access_key_id=aws_access_key_id,
# #     aws_secret_access_key=aws_secret_access_key,
# #     region_name=aws_region
# # )

# # # Specify the time range for which you want to fetch cost data
# # start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
# # end_date = datetime.datetime.now().strftime('%Y-%m-%d')

# # # Define the granularity of the data (DAILY, MONTHLY, etc.)
# # time_period = {
# #     'Start': start_date,
# #     'End': end_date
# # }

# # # Define the metrics you want to retrieve (e.g., BlendedCost, NormalizedUsageAmount)
# # metrics = ['NormalizedUsageAmount']

# # # Fetch cost and usage data
# # response = ce.get_cost_and_usage(
# #     TimePeriod=time_period,
# #     Granularity='DAILY',  # You can adjust the granularity as needed
# #     Metrics=metrics,
# #     GroupBy=[
# #         {
# #             'Type': 'DIMENSION',
# #             'Key': 'SERVICE'  # Group by AWS service
# #         }
# #     ]
# # )

# # # Print the cost breakdown by AWS service
# # print(f"{'AWS Service':<40}{'Usage Amount':<20}")

# # for result in response['ResultsByTime']:
# #     for group in result['Groups']:
# #         service = group['Keys'][0]
# #         usage_amount = float(group['Metrics']['NormalizedUsageAmount']['Amount'])
# #         currency = group['Metrics']['NormalizedUsageAmount']['Unit']
# #         formatted_usage_amount = f"{usage_amount:.2f} {currency}"
# #         print(f"{service:<40}{formatted_usage_amount:>20}")

# # ----------------------------------------------------------------------------------------------------------------------------

# import boto3
# import datetime
# from tabulate import tabulate

# # Replace with your AWS credentials and region
# aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
# aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# aws_region = 'ap-south-1'  # Replace with your desired AWS region

# # Initialize the Cost Explorer client with your credentials and region
# ce = boto3.client(
#     'ce',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# # Specify the time range for which you want to fetch cost data
# start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
# end_date = datetime.datetime.now().strftime('%Y-%m-%d')

# # Define the granularity of the data (DAILY, MONTHLY, etc.)
# time_period = {
#     'Start': start_date,
#     'End': end_date
# }

# # Define the metrics you want to retrieve (e.g., BlendedCost, NormalizedUsageAmount)
# metrics = ['NormalizedUsageAmount']

# # Fetch cost and usage data
# response = ce.get_cost_and_usage(
#     TimePeriod=time_period,
#     Granularity='MONTHLY',  # You can adjust the granularity as needed
#     Metrics=metrics,
#     GroupBy=[
#         {
#             'Type': 'DIMENSION',
#             'Key': 'SERVICE'  # Group by AWS service
#         }
#     ]
# )

# # Prepare data for tabulate
# table_data = []
# for result in response['ResultsByTime']:
#     for group in result['Groups']:
#         service = group['Keys'][0]
#         usage_amount = float(group['Metrics']['NormalizedUsageAmount']['Amount'])
#         currency = group['Metrics']['NormalizedUsageAmount']['Unit']
#         formatted_usage_amount = f"{usage_amount:.2f} {currency}"
#         table_data.append([service, formatted_usage_amount])

# # Create and print the table
# headers = ['AWS Service', 'Usage Amount']
# table = tabulate(table_data, headers, tablefmt='pretty')
# print(table)

# -----------------------------------------------------------------------------------------------------------------

# import boto3
# from datetime import datetime, timedelta

# # Replace with your AWS credentials and region
# aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
# aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
# aws_region = 'ap-south-1'  # Replace with your AWS region

# # Initialize the AWS Cost Explorer client with your credentials and region
# ce = boto3.client(
#     'ce',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# # Define a function to get AWS Cost Explorer cost data
# def get_cost_explorer_cost_data():
#     # Set the time period for AWS Cost Explorer
#     end_time_ce = datetime.utcnow()
#     start_time_ce = end_time_ce - timedelta(weeks=20)  # Adjust the time range as needed

#     # Fetch the AWS Cost Explorer cost data
#     response_ce = ce.get_cost_and_usage(
#         TimePeriod={
#             'Start': start_time_ce.strftime('%Y-%m-%d'),
#             'End': end_time_ce.strftime('%Y-%m-%d'),
#         },
#         Granularity='MONTHLY',  # You can change this to other granularities like 'MONTHLY'
#         Metrics=['BlendedCost'],  # You can specify other cost metrics here
#     )

#     # Print the AWS Cost Explorer cost data
#     print("AWS Cost Explorer Cost Data:")
#     for result in response_ce['ResultsByTime']:
#         print(f"Time Period: {result['TimePeriod']['Start']} to {result['TimePeriod']['End']}, Cost: {result['Total']['BlendedCost']['Amount']} {result['Total']['BlendedCost']['Unit']}")
#     print()

# # Fetch AWS Cost Explorer cost data
# get_cost_explorer_cost_data()

# ----------------------------------------------------------------------------------------------------------

# import boto3
# from datetime import datetime, timedelta

# # Replace with your AWS credentials and region
# aws_access_key_id = 'AKIARWCTPADXXM6BOGUA'
# aws_secret_access_key = 'BO+7r0vPZ5igYAS/Ybt+Owvx/DPA304x7oNtdeOs'
# aws_region = 'ap-south-1'  # Replace with your AWS region

# # Initialize the AWS Cost Explorer client with your credentials and region
# ce = boto3.client(
#     'ce',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=aws_region
# )

# # Define a function to get AWS Cost Explorer cost data
# def get_cost_explorer_cost_data():
#     # Set the time period for AWS Cost Explorer
#     end_time_ce = datetime.utcnow()
#     start_time_ce = end_time_ce - timedelta(weeks=8)  # Adjust the time range as needed

#     # Fetch the AWS Cost Explorer cost data
#     response_ce = ce.get_cost_and_usage(
#         TimePeriod={
#             'Start': start_time_ce.strftime('%Y-%m-%d'),
#             'End': end_time_ce.strftime('%Y-%m-%d'),
#         },
#         Granularity='MONTHLY',  # You can change this to other granularities like 'MONTHLY'
#         Metrics=['BlendedCost'],  # You can specify other cost metrics here
#     )

#     # Print the AWS Cost Explorer cost data
#     print("AWS Cost Explorer Cost Data:")
#     for result in response_ce['ResultsByTime']:
#         print(f"Time Period: {result['TimePeriod']['Start']} to {result['TimePeriod']['End']}, Cost: {result['Total']['BlendedCost']['Amount']} {result['Total']['BlendedCost']['Unit']}")
#     print()

# # Fetch AWS Cost Explorer cost data
# get_cost_explorer_cost_data()

import boto3
from datetime import datetime, timedelta

# Replace with your AWS credentials and region
aws_access_key_id = 'AKIA34REAOZJ5WNWQHTS'
aws_secret_access_key = 'iiGHaOVZ4A3ZM8fLPvdMVhoIBHNz4YMDAv0/AMJj'
aws_region = 'ap-south-1'  # Replace with your AWS region

# Initialize the AWS Cost Explorer client with your credentials and region
ce = boto3.client(
    'ce',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Define a function to get AWS Cost Explorer cost data for a specific month
def get_monthly_cost(start_date, end_date):
    response_ce = ce.get_cost_and_usage(
        TimePeriod={
            'Start': start_date.strftime('%Y-%m-%d'),
            'End': end_date.strftime('%Y-%m-%d'),
        },
        Granularity='MONTHLY',
        Metrics=['BlendedCost'],
    )

    for result in response_ce['ResultsByTime']:
        print(f"Time Period: {result['TimePeriod']['Start']} to {result['TimePeriod']['End']}, Cost: {result['Total']['BlendedCost']['Amount']} {result['Total']['BlendedCost']['Unit']}")

# Fetch AWS Cost Explorer cost data for the current month
today = datetime.utcnow()
start_of_month = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
get_monthly_cost(start_of_month, today)

# Define the number of previous months to fetch data for
num_previous_months = 3  # You can change this to the desired number of previous months

# Fetch AWS Cost Explorer cost data for the previous months using a loop
for i in range(1, num_previous_months + 1):
    start_date = (start_of_month - timedelta(days=1)).replace(day=1)
    end_date = start_of_month - timedelta(days=1)
    get_monthly_cost(start_date, end_date)
    start_of_month = start_date