import asyncio
import os
from dotenv import load_dotenv
from edison_client import EdisonClient, JobNames

def main():
    load_dotenv()
    api_key = os.getenv("EDISON_API_KEY")
    client = EdisonClient(api_key=api_key.strip())

    # Task: Use the MOLECULES agent to do actual Engineering/Chemistry
    # This is something a Google Search cannot do (it requires computation and chemical logic)
    
    cortisol_smiles = "C[C@]12CCC(=O)C=C1CC[C@@H]3[C@@H]2[C@H](C[C@]4([C@H]3CC[C@@]4(C(=O)CO)O)C)O"
    
    query = (
        f"I am designing a biosensor for Cortisol (SMILES: {cortisol_smiles}). "
        "1. Calculate its exact LogP and Water Solubility to help me choose a sensor surface. "
        "2. Suggest 3 specific functional monomers that would form strong hydrogen bonds with Cortisol "
        "for creating a Molecularly Imprinted Polymer (MIP)."
    )

    print(f"Running Advanced Chemistry Task:\n{query}\n")
    print("-" * 50)

    task_data = {
        "name": JobNames.MOLECULES,
        "query": query,
    }

    # Run the task
    # Note: run_tasks_until_done might return a list if it detects a batch, or even for single.
    # The previous error showed it returned a list.
    responses = client.run_tasks_until_done(task_data)

    # Handle if it's a single object or list
    if isinstance(responses, list):
        response = responses[0]
    else:
        response = responses

    
    # Debug: Print the available attributes
    # print(f"DEBUG Response Type: {type(response)}")
    # print(f"DEBUG Response: {response}")

    # PhoenixTaskResponse might just have 'output' or 'answer' but not 'has_successful_answer'
    # Let's try to print the output directly.
    try:
        if hasattr(response, 'answer'):
            print(f"RESULT:\n{response.answer}")
        elif hasattr(response, 'result'):
            print(f"RESULT:\n{response.result}")
        else:
             print(f"RESULT (Raw):\n{response}")
             
    except Exception as e:
        print(f"Error parsing response: {e}")

if __name__ == "__main__":
    main()
