def main():
    import os
    from dotenv import load_dotenv
    from google import genai
    import sys

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(args) 

    res = client.models.generate_content(model="gemini-2.0-flash-001", contents=user_prompt)
    print(res.text)
    print("Prompt tokens:", res.usage_metadata.prompt_token_count)
    print("Response tokens:", res.usage_metadata.candidates_token_count)



if __name__ == "__main__":
    main()
