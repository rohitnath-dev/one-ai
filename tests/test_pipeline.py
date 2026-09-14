from app import should_search, generate_search_query, search_web, call_ai


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

    decision = should_search(prompt)
    print(f"Search required: {decision}")

    if decision:
        search_query = generate_search_query(prompt)
        print(f"Search query: {search_query}")

        search_results = search_web(search_query)

        if search_results:
            result_count = search_results.count("Title:")

            print(f"Results found: {result_count}")
            print("\n--- Search Results ---")
            print(search_results)
            print("--- End Search Results ---\n")

            response = call_ai(
                prompt,
                context=search_results
            )

        else:
            print("Results found: 0")
            response = call_ai(prompt)

    else:
        response = call_ai(prompt)

    print("\n--- Final Response ---")
    print(response)
    print("=" * 60)