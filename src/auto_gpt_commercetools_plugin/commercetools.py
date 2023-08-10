import commercetools
from commercetools.platform.client import Client
from commercetools.platform.models.graph_ql import GraphQLRequest

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

def ct_get_products_info(skus, currency):
    query = """
        query {
            products(skus: [%s]) {
                results {
                    masterData {
                        current{
                            allVariants {
                                price(currency:"%d") {
                                    value {
                                        centAmount
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        """ % (skus, currency)
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

