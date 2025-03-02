import os
from dotenv import load_dotenv

from openai import OpenAI
from httpx import Timeout

import requests
from mix_eval.models.base_api import APIModelBase
from mix_eval.api.registry import register_model

@register_model("vllm")
class VLLM(APIModelBase):
    def __init__(self, args):
        super().__init__(args)
        self.args = args
        print(args)
        self.model_name = os.getenv('MODEL')

        # Get API key and base URL from environment variables
        base_url = os.getenv('OPENAI_BASE_URL', 'http://localhost:8000/v1')
        api_key = os.getenv('OPENAI_API_KEY', 'x')
        
        # uh this will use the judge url...
        # If URL is provided, override base_url
        # if hasattr(args, 'api_base_url') and args.api_base_url:
        #     base_url = args.api_base_url

        # print(base_url)
        # print(api_key)
        # import sys
        # sys.exit()

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )
