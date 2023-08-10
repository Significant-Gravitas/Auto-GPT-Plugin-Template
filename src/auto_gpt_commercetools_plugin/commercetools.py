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

def ct_execute_graph_ql(query):

    body = GraphQLRequest(query=query)

    result = client.with_project_key(project_key=project_key).graphql().post(body=body)
    return result

def ct_get_graph_ql_schema():
    query = "\n  query IntrospectionQuery {\n    __schema {\n      queryType { name }\n      mutationType { name }\n      subscriptionType { name }\n      types {\n        ...FullType\n      }\n      directives {\n        name\n        description\n        locations\n        args {\n          ...InputValue\n        }\n      }\n    }\n  }\n\n  fragment FullType on __Type {\n    kind\n    name\n    description\n    fields(includeDeprecated: true) {\n      name\n      description\n      args {\n        ...InputValue\n      }\n      type {\n        ...TypeRef\n      }\n      isDeprecated\n      deprecationReason\n    }\n    inputFields {\n      ...InputValue\n    }\n    interfaces {\n      ...TypeRef\n    }\n    enumValues(includeDeprecated: true) {\n      name\n      description\n      isDeprecated\n      deprecationReason\n    }\n    possibleTypes {\n      ...TypeRef\n    }\n  }\n\n  fragment InputValue on __InputValue {\n    name\n    description\n    type { ...TypeRef }\n    defaultValue\n  }\n\n  fragment TypeRef on __Type {\n    kind\n    name\n    ofType {\n      kind\n      name\n      ofType {\n        kind\n        name\n        ofType {\n          kind\n          name\n          ofType {\n            kind\n            name\n            ofType {\n              kind\n              name\n              ofType {\n                kind\n                name\n                ofType {\n                  kind\n                  name\n                }\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n"
    body = GraphQLRequest(query=query)

    result = client.with_project_key(project_key=project_key).graphql().post(body=body)
    return result

def ct_get_products_info(skus, currency):
    query = f"""
        query {{
            products(skus: {skus}) {{
                results {{
                    masterData {{
                        current {{
                            allVariants {{
                                price(currency:"{currency}") {{
                                    value {{
                                        centAmount
                                    }}
                                }}
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

