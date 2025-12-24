import os
import asyncio
from dotenv import load_dotenv
from edison_client import EdisonClient, JobNames

# Load environment variables from .env file
load_dotenv()

# Get the API key
api_key = os.getenv("EDISON_API_KEY")

if not api_key or api_key == "put_your_api_key_here":
    print("Error: Please set your EDISON_API_KEY in the .env file.")
    exit(1)

async def main():
    print("Initializing Edison Client...")
    
    # Debug: Check key format
    if api_key:
        print(f"API Key loaded. Length: {len(api_key)}")
        print(f"Starts with: {api_key[:10]}...")
        print(f"Ends with: ...{api_key[-10:]}")
        if api_key.strip() != api_key:
            print("WARNING: API Key has leading/trailing whitespace!")
    
    client = EdisonClient(api_key=api_key.strip())

    # Try PRECEDENT task instead of DUMMY
    task_data = {
        "name": JobNames.PRECEDENT,
        "query": "Has anyone tested aspirin for headache?",
    }

    print(f"Submitting task: {task_data['name']}...")
    try:
        task_response = await client.arun_tasks_until_done(task_data)
        
        print("\n--- Task Completed ---")
        print(f"Success: {task_response.has_successful_answer}")
        print(f"Answer: {task_response.answer}")
        
    except Exception as e:
        print(f"\nError running task: {e}")

if __name__ == "__main__":
    asyncio.run(main())
