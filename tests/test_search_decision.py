from ai import should_search


test_cases = [
    # =========================
    # SHOULD NOT SEARCH
    # =========================

    ("25 ka 18% kitna hoga?", False),
    ("Explain Newton's first law.", False),
    ("What is photosynthesis?", False),
    ("Translate 'good morning' to Hindi.", False),
    ("Who was the first Prime Minister of India?", False),
    ("How does Python work?", False),
    ("What is a binary tree?", False),
    ("Make me a 5-day study plan for my exam.", False),
    ("Write a short sci-fi story.", False),
    ("Explain the difference between RAM and ROM.", False),

    # =========================
    # SHOULD SEARCH
    # =========================

    ("What is today's weather in Delhi?", True),
    ("What happened in AI today?", True),
    ("What are the latest changes in Python 3.14?", True),
    ("What did Google release this week?", True),
    ("Who is the current Prime Minister of India?", True),
    ("What is the latest OpenAI model?", True),
    ("What are the latest AI news today?", True),
    ("Who won today's IPL match?", True),
    ("What is Bitcoin's price right now?", True),
    ("Search the web for the latest OpenAI news.", True),

    # =========================
    # HINGLISH / INFORMAL
    # =========================

    ("bhai abhi Python ka latest version kya hai?", True),
    ("aaj news kya hai?", True),
    ("bhai aaj IPL me kaun jeeta?", True),
    ("abhi kya chal raha hai AI me?", True),
    ("Python ka latest version check karke bata", True),

    # =========================
    # VERIFICATION
    # =========================

    ("I heard Python 3.14 has been released. Verify it.", True),
    ("Someone told me OpenAI released a new model. Is that true?", True),
    ("I heard this company launched a new AI product. Check it.", True),

    # =========================
    # IMPORTANT BOUNDARIES
    # =========================

    ("Explain Python 3.14.", False),
    ("What changed in Python 3.14?", True),

    ("Tell me about Bitcoin.", False),
    ("What's Bitcoin worth right now?", True),

    ("Tell me about OpenAI.", False),
    ("What has OpenAI released recently?", True),

    ("Who was the Prime Minister of India in 2010?", False),
    ("Who is the current Prime Minister of India?", True),

    ("Explain IPL.", False),
    ("Who won today's IPL match?", True),
]


def run_tests():
    correct = 0
    total = len(test_cases)

    print("\n" + "=" * 70)
    print("SEARCH DECISION TEST")
    print("=" * 70)

    for query, expected in test_cases:
        result = should_search(query)

        passed = result == expected

        if passed:
            correct += 1

        status = "PASS" if passed else "FAIL"

        print(f"\n[{status}]")
        print(f"Query:    {query}")
        print(f"Expected: {expected}")
        print(f"Got:      {result}")

    accuracy = (correct / total) * 100

    print("\n" + "=" * 70)
    print(f"RESULT: {correct}/{total} correct ({accuracy:.1f}%)")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
