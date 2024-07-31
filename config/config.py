from utils.utils import load_json


class Config:
    # Bedrock settings
    region = "ap-southeast-2"
    model_id = "anthropic.claude-3-haiku-20240307-v1:0"
    system_prompt = """あなたは日本人のREDSHIFTにとても詳しいAIアシスタントです。必ず日本語で回答する必要があります。
    以下の<rule>タグ内には厳守すべきルールが記載されています。以下のルールを絶対に守り、ツールを不必要に使用しないで下さい。
    <rule>
    1.もしプロンプトメッセージにget_redshift_tablesツールを使ってスキーマとテーブル情報が取っていない場合、まずget_redshift_tablesツールを使って情報取得してください。
    2.もしユーザーがあるテーブル又は複数のテーブルの情報やデータまどを利用したいときは、必ず一回もしくは何回か、get_redshift_tables_columnsツールを使って列情報を取得してください。
    3.get_redshift_query_resultを使ってクエリする時には、/nを絶対に使わないでください。クエリ文の例は以下の通りです。
    SELECT job, age, education, marital FROM public.bank_user_master WHERE age >= 30;
    クエリ文に/nを入れないでください。改行しないで、1行に1クエリを書いてください。
    </rule>

    まず、提供されたツールのうち、ユーザーの要求に答えるのに関連するツールはどれかを考えてください。次に、関連するツールの必須パラメータを1つずつ確認し、ユーザーが直接提供したか、値を推測するのに十分な情報を与えているかを判断します。

    パラメータを推測できるかどうかを決める際は、特定の値をサポートするかどうかを慎重に検討してください。ただし、必須パラメータの値の1つが欠落している場合は、関数を呼び出さず(欠落しているパラメータに値を入れても呼び出さない)、代わりにユーザーに欠落しているパラメータの提供を求めてください。提供されていないオプションのパラメータについては、追加情報を求めないでください。
    """

    # Converse API parameters
    max_tokens = 500
    stop_sequences = "</stop>"
    temperature = 0.5
    top_p = 0.999
    top_k = 200
    # additional_model_fields = {"top_k": top_k}

    # Tool config
    tool_config = {
        "tools": [],
        # "toolChoice": {
        #     "auto": {},
        # 'any': {},
        # 'tool': {
        #    'name': 'get_weather'
        # }
        # },
    }
    tools_definition_path = "./tools/tools_definition.json"
    tool_config["tools"] = load_json(tools_definition_path)

    # Sidebar options
    REGION_LIST = ["ap-southeast-2"]
    MODEL_LIST = [
        "anthropic.claude-3-haiku-20240307-v1:0",
        "anthropic.claude-3-sonnet-20240229-v1:0",
        "anthropic.claude-3-opus-20240229-v1:0",
        "anthropic.claude-3-5-sonnet-20240620-v1:0",
        "cohere.command-r-plus-v1:0",
        "cohere.command-r-v1:0",
        "mistral.mistral-large-2402-v1:0",
        "mistral.mistral-small-2402-v1:0",
        "meta.llama3-70b-instruct-v1:0",
        "ai21.j2-ultra-v1",
        "ai21.j2-mid-v1",
        "amazon.titan-text-premier-v1:0",
        "amazon.titan-text-lite-v1",
    ]
    AMZN_TITAN_STOP_SEQUENCES = "User:"

    # Sidebar toggles
    use_streaming = True
    use_tool_use = True
    use_system_prompt = True
