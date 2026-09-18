from ai import should_search, generate_search_query, call_ai
from web_search import search_web
import time


test_cases = [
    "25 ka 18% kitna hoga?",
    "bhai Modi abhi PM hai na?",
    "bhai mai abhi coding kar raha tha aur mujhe yaad aaya ki Python ka latest version kya hai, tu ek baar internet pe check karke bata sakta hai?",
    "Explain Newton's first law.",
    'Translate "good morning" to Hindi.',
    "Who was the first Prime Minister of India?",
    "I have 500 rupees. What can I buy for 200?",
    "Search the web for the latest OpenAI news.",
    "What are the latest changes in Python 3.14?",
    "What did Google release this week?",
    "bhai plz ek baar check krna na ki aajkal python ka konsa ver chal rha h 😭",
    "photosynthesis?",
    "aaj news?",
    "maine suna hai ki Python 3.14 aa gaya hai, verify karke bata",
    "aaj IPL me kaun jeeta?",
    "Mera exam 20 September ko hai. Mujhe 5 din ka study plan bana de.",
    "aaj ka kya scene hai",
    "bhai abhi kya chal raha hai?"
]


for prompt in test_cases:

    print("\n" + "=" * 60)
    print(f"Query: {prompt}")

    total_start = time.perf_counter()

    # Search decision
    start = time.perf_counter()
    decision = should_search(prompt)
    decision_time = time.perf_counter() - start

    print(f"Search required: {decision}")
    print(f"Decision time: {decision_time:.2f}s")

    if decision:

        # Generate search query
        start = time.perf_counter()
        search_query = generate_search_query(prompt)
        query_time = time.perf_counter() - start

        print(f"Search query: {search_query}")
        print(f"Query generation time: {query_time:.2f}s")

        # Web search
        start = time.perf_counter()
        search_results = search_web(search_query)
        search_time = time.perf_counter() - start

        if search_results:
            result_count = search_results.count("Title:")

            print(f"Results found: {result_count}")
            print(f"Web search time: {search_time:.2f}s")

            print("\n--- Search Results ---")
            print(search_results)
            print("--- End Search Results ---\n")

            # Final AI response
            start = time.perf_counter()
            response = call_ai(
                prompt,
                context=search_results
            )
            ai_time = time.perf_counter() - start

        else:
            print("Results found: 0")
            print(f"Web search time: {search_time:.2f}s")

            start = time.perf_counter()
            response = call_ai(prompt)
            ai_time = time.perf_counter() - start

    else:

        # Final AI response
        start = time.perf_counter()
        response = call_ai(prompt)
        ai_time = time.perf_counter() - start

    print(f"Final AI time: {ai_time:.2f}s")

    total_time = time.perf_counter() - total_start
    print(f"Total time: {total_time:.2f}s")

    print("\n--- Final Response ---")
    print(response)

    print("=" * 60)