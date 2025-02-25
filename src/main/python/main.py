
from anthropic import HUMAN_PROMPT, AI_PROMPT
from anthropic import AsyncAnthropic
import instructor
from pydantic import BaseModel
from typing import List, Optional
import anthropic
import pandas as pd
import os
from prompt_store import get_prompt

anthropic_client = instructor.from_anthropic(anthropic.Anthropic())


class Response(BaseModel):
    match: str
    reason: str
    reformulated_query: Optional[str]


# Sample function to call Claude API
def get_response(query, product_title, product_description, product_bullet_point, product_brand, product_color):
    response = anthropic_client.chat.completions.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        temperature=0.8,
        messages=get_prompt(query, product_title, product_description, product_bullet_point, product_brand, product_color),
        response_model=Response,
    )

    return response



data = pd.read_csv('src/main/data/filtered_shopping_queries.csv')


# Process each row and apply the model
results = []
for index, row in data.iterrows():
    query = row['query']
    product_title = row['product_title']
    product_description = row['product_description']
    product_bullet_point = row['product_bullet_point']
    product_brand = row['product_brand']
    product_color = row['product_color']
    
    # Call the LLM
    result = get_response(query, product_title, product_description, product_bullet_point, product_brand, product_color)
    
    print("result", result)
    
    # Store the result
    results.append({
        'query_id': row['query_id'],
        'product_id': row['product_id'],
        'is_exact_match': result.match,
        'reason': result.reason,
        'reformulated_query': result.reformulated_query
    })

# Create a DataFrame for the results
df_results = pd.DataFrame(results)

# Save the results to CSV
output_path = "src/main/data/output/query_accuracy_results.csv"
df_results.to_csv(output_path, index=False)

print(f"Results saved to: {output_path}")
