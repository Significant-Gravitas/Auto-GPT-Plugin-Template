import commercetools
from commercetools.platform.client import Client
from commercetools.platform.models.graph_ql import GraphQLRequest
import random
import os

# Authorization credentials

project_key = os.environ["CTP_PROJECT_KEY"]
client_id = os.environ["CTP_CLIENT_ID"]
client_secret = os.environ["CTP_CLIENT_SECRET"]

# SDK settings
auth_url = os.environ["CTP_AUTH_URL"]
api_url = os.environ["CTP_API_URL"]
scope = os.environ["CTP_SCOPES"]

client = Client(
        client_id=client_id,
        client_secret=client_secret,
        scope=scope,
        url=api_url,
        token_url=auth_url,
    )

def ct_execute_graph_ql(query):

    body = GraphQLRequest(query=query)

    result = client.with_project_key(project_key=project_key).graphql().post(body=body)
    return result

def ct_get_products_info(skus, currency):
    sku_array = str(skus).replace("'", '"')

    query = f"""
        query {{
            products(skus: {sku_array}) {{
                results {{
                    masterData {{
                        current {{
                            name(locale: "en-US")
                            masterVariant {{
                              sku
                            }}
                        }}
                    }}
                }}
            }}
        }}
        """
    body = GraphQLRequest(query=query)

    result = client.with_project_key(project_key=project_key).graphql().post(body=body)
    return result

def ct_get_all_orders():
    query = """
        query {
            orders {
                results {
                    lineItems {
                        quantity
                        totalPrice {
                            centAmount
                        }
                        variant {
                            sku
                        }
                    }
                }
            }
        }
        """
    body = GraphQLRequest(query=query)

    result = client.with_project_key(project_key=project_key).graphql().post(body=body)
    return result

def ct_create_product_discount(name, percentValue, skus):
    sku_str = ','.join(f'"{sku}"' for sku in skus)
    r = random.random()

    query = f"""
        mutation {{
            createProductDiscount(draft: {{name: {{locale: "en-US", value: "{name}"}}, value: {{relative: {{permyriad: {percentValue}}}}}, predicate: "sku in ({sku_str})", sortOrder: "{r}"}}) {{
                predicate
                name(locale: "en-US")
            }}
        }}
        """
    body = GraphQLRequest(query=query)

    result = client.with_project_key(project_key=project_key).graphql().post(body=body)
    return result