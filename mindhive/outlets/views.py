from django.http import JsonResponse
from .mongo_utils import db, fetch_all_outlets  
from django.conf import settings
import openai
import re

def outlet_list(request):
    outlets = fetch_all_outlets()  
    # Manually serialize the MongoDB documents to JSON
    outlets_json = [{key: (str(value) if key == '_id' else value) for key, value in outlet.items()} for outlet in outlets]
    return JsonResponse(outlets_json, safe=False)  

def serialize_outlets_for_gpt(outlets):
    # Create a summary string for each outlet for GPT to process
    summaries = []
    for index, outlet in enumerate(outlets):
        summary = f"Index {index}: {outlet['name']}, Address: {outlet['address']}, Hours: {outlet['operating_hours']}."
        summaries.append(summary)
    return summaries

def parse_gpt_response_to_indices(gpt_response):
    # Use regular expression to find all occurrences of "Index" followed by a number
    pattern = r"Index\s+(\d+)"
    matches = re.findall(pattern, gpt_response)
    
    # Convert all found matches to integers
    indices = [int(match) for match in matches]
    
    return indices

def search_outlets(request):
    query = request.GET.get('query', '')
    outlets = fetch_all_outlets()
    outlets_summaries = serialize_outlets_for_gpt(outlets)

    # Combine summaries into a single string for GPT
    combined_summaries = "\n".join(outlets_summaries)

    # Prepare the message for GPT
    search_message = f"""
    I am looking for outlets based on the query '{query}'. The search should consider the outlet's name, address, or operating hours. Please identify the outlets that match the query by mentioning their index and name. The query might relate to the outlet's specific location (like 'Bangsar'), its operating hours (like 'open until 9 PM'), or other details mentioned in the name, address, or operating hours.

    Here are the outlets:
    {combined_summaries}

    Example queries and responses:
    - If the query was 'Bangsar', outlets with 'Bangsar' in their name or address would be considered a match.
    - If the query was 'open until 10 PM', outlets that operate until 10 PM or later should be identified.
    """
    
    openai.api_key = settings.OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": search_message}
        ]
    )

    gpt_response = response.choices[0].message['content']
    print(gpt_response)
    extracted_indices = parse_gpt_response_to_indices(gpt_response)

    # Fetch the specific outlets using the parsed indices
    matching_outlets = [outlets[i] for i in extracted_indices]

    # Serialize matching outlets for JsonResponse
    matching_outlets_json = [{key: (str(value) if key == '_id' else value) for key, value in outlet.items()} for outlet in matching_outlets]
    return JsonResponse(matching_outlets_json, safe=False)