from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

from leetcode_runner.models import Problem


def make_gql_client() -> Client:
    transport = RequestsHTTPTransport(
        url="https://leetcode.com/graphql",
        verify=True,
        retries=3,
    )

    return Client(transport=transport, fetch_schema_from_transport=False)


def fetch_problem(client: Client, slug: str) -> Problem:
    query = gql(
        """
            query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    title
                    difficulty
                    likes
                    dislikes
                    isLiked
                    isPaidOnly
                    stats
                    status
                    content
                    topicTags {
                        name
                    }
                    codeSnippets {
                        lang
                        langSlug
                        code
                    }
                    sampleTestCase
                }
            }
    """
    )
    res = client.execute(query, variable_values={"titleSlug": slug})
    return Problem(**res)
