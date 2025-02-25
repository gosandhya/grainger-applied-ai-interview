prompt = """You are tasked with evaluating whether a product correctly matches a given query according to the KDD Cup 2022 competition labeling definition.
    The label E is reserved for situations where the item is relevant for the query and satisfies all the query specifications. 
    Your job is to determine if this label is correctly applied and, if not, to reformulate the query to match the product.
    
    Here is the query:
    <query>
    {query}
    </query>

    Here is the product information:
    <product_info>
    Product Title: {product_title}
    Product Description: {product_description}
    Product Bullet Points: {product_bullet_point}
    Product Brand: {product_brand}
    Product Color: {product_color}
    </product_info>
    


    Please follow these steps:

    1. Analyze the query and product information thoroughly.
    2. Determine if the product satisfies all specifications in the query, keeping in mind that an "E" label can be applied even if the match is not perfectly exact.
    3. If the product does not match the query, identify which specifications are not met.


    In your analysis, consider the following nuances:
    - If the product information doesn't contain all the specifications from the query but still seems like an appropriate match overall, it may still qualify for an "E" label. For example, if the query mentions a specific quantity but the product information doesn't, it could still be a match.
    - If a product has additional features or specifications beyond what the query specifies (but still matches in other ways), it might still qualify for an "E" label because it captures the relevant product. For example, if the query doesn't mention a warranty but the product information does, it could still be a match.


    Before providing your final output, show your evaluation process in <evaluation_process> tags. Break down the query and product information, and explain your reasoning for considering it a match or not. Follow these steps:

    a. List out the key specifications from the query
    b. For each specification, quote the relevant part of the product information that matches or doesn't match
    c. Summarize whether each specification is met or not
    d. Consider any additional features in the product not mentioned in the query
    e. Make a final judgment based on the overall match

    It's okay for this section to be quite long, as we want a thorough analysis.

    After your evaluation process, provide your final output in JSON format with the following structure:
    {{
        "match": "Yes/No",
        "reason": "Your justification here",
        "reformulated_query": "Reformulated query if match is No, or null if match is Yes"
    }}


    Remember:
    - The "match" field should be either "Yes" or "No".
    - The "reason" field should clearly explain why the product does or does not match the query, taking into account the nuances mentioned above.
    - The "reformulated_query" field should contain a modified query that would make this an "E" match if the original match is "No". If the match is "Yes", this field should be null.


    Your goal is to ensure that the "E" label is applied when the product truly satisfies all query specifications, allowing for some flexibility as described. Be thorough in your analysis and clear in your explanation.
    
    """

def get_prompt(query, product_title, product_description, product_bullet_point, product_brand, product_color):
    _prompt = prompt.format(query=query, 
                  product_title=product_title, 
                  product_description=product_description, 
                  product_bullet_point=product_bullet_point,
                  product_brand=product_brand,
                  product_color=product_color)
    
    prompt_message =[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": _prompt
                    }
                ]
            }
        ]
    return prompt_message