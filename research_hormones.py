import asyncio
import os
from dotenv import load_dotenv
from edison_client import EdisonClient, JobNames

def main():
    load_dotenv()
    api_key = os.getenv("EDISON_API_KEY")
    if not api_key:
        print("Error: EDISON_API_KEY not found in .env")
        return

    client = EdisonClient(api_key=api_key.strip())

    # Define two research tasks:
    # 1. Broad literature search for technologies
    # 2. Specific precedent check for a concrete application (wearables)
    tasks = [
        {
            "name": JobNames.LITERATURE,
            "query": "What are the most promising emerging technologies for continuous, non-invasive hormone monitoring (e.g., cortisol, sex hormones) in sweat or interstitial fluid?",
        },
        {
            "name": JobNames.PRECEDENT,
            "query": "Has anyone successfully developed a wearable aptamer-based sensor for real-time cortisol monitoring in humans?",
        }
    ]

    print(f"Submitting {len(tasks)} research tasks to Edison...")
    
    # Run tasks (this might take a few minutes)
    responses = client.run_tasks_until_done(tasks)

    print("\n" + "="*50)
    for i, response in enumerate(responses):
        task_name = tasks[i]['name']
        print(f"TASK {i+1}: {task_name}")
        print("-" * 20)
        if response.has_successful_answer:
            print(f"ANSWER:\n{response.answer}\n")
        else:
            print("No good answer found.\n")
        print("="*50)

if __name__ == "__main__":
    main()
