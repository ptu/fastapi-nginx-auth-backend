import logging


class EndpointCheckFilter(logging.Filter):
    def filter(self, record):
        # remote_address = record.args[0]
        request_method = record.args[1]

        # complete query string (so parameter and other value included)
        query_string = record.args[2]

        # html_version = record.args[3]
        # satuts_code = record.args[4]

        return request_method == "GET" and not query_string in ["/health", "/metrics"]
