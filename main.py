from __future__ import annotations
from typing import List, Optional, Union
from pydantic import BaseModel

import requests


class WebUrlItem(BaseModel):
    url_main_page: str
    url_main_page_tag: str
    url_loging_page: Optional[str] = None
    url_loging_page_tag: Optional[str] = None
    url_client_page: Optional[str] = None
    url_client_page_tag: Optional[str] = None


class WebUrlModel(BaseModel):
    web_url: List[WebUrlItem]


scrapy_url_dict = {
    "web_url": [
        {
            "url_main_page": "https://easytenders.co.za/tenders",
            "url_main_page_tag": "tenders-table",
            "url_loging_page": "",
            "url_loging_page_tag": "",
            "url_client_page": "",
            "url_client_page_tag": "",
        }
    ]
}


#####################################################
#       API function: create_session
#####################################################


def create_session(
    app_header_access_token_name: Optional(str) = None,
    api_token: Optional(str) = None,
    content_type: Optional(str) = None,
) -> session:
    """Creates api sesstion

    Parameters:
    -----------

         - app_header_access_token_name:
             - type: Optional(str)
             - description: App hearder access token name.

        - api_token:
             - type: Optional(str)
             - description: App api token key

        - content_type :
             - type: Optional(str)
             - description: App headers content type if content_type is not set (default="application/json")

    Return:
    -------
       - session:
             - type: requests.Session
             - description: web session
    """

    if content_type is None:
        content_type = "application/json"

    # request web session.
    session = requests.Session()

    # update headers with app header settings.
    session.headers.update(
        {"{app_header_access_token_name}": api_token, "Content-Type": content_type}
    )

    return session


#####################################################
#       API function main
#####################################################


def main():

    # web url model
    web_model = WebUrlModel(**scrapy_url_dict)

    # create session
    session = create_session(
        app_header_access_token_name="", api_token="", content_type=""
    )

    # get request from url
    for url_key in web_model.web_url:

        print(url_key.url_main_page)
        url_request_response = session.get(url_key.url_main_page)

        print(url_request_response)


if __name__ == "__main__":
    main()
