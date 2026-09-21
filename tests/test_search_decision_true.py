from ai import should_search


test_cases = [
    "What is today's weather in Delhi?",
    "What happened in AI today?",
    "What are the latest changes in Python 3.14?",
    "What did Google release this week?",
    "Who is the current Prime Minister of India?",
    "What is the latest OpenAI model?",
    "What are the latest AI news today?",
    "Who won today's IPL match?",
    "What is Bitcoin's price right now?",

    "Search the web for the latest OpenAI news.",

    "bhai abhi Python ka latest version kya hai?",
    "aaj news kya hai?",
    "bhai aaj IPL me kaun jeeta?",
    "abhi kya chal raha hai AI me?",
    "Python ka latest version check karke bata",

    "I heard Python 3.14 has been released. Verify it.",
    "Someone told me OpenAI released a new model. Is that true?",
    "I heard this company launched a new AI product. Check it.",

    "What changed in Python 3.14?",
    "What's Bitcoin worth right now?",
    "What has OpenAI released recently?",
    "Who won today's IPL match?",
]


def run_tests():
    correct = 0
    total = len(test_cases)

    print("\n" + "=" * 70)
    print("SEARCH DECISION — TRUE TEST")
    print("=" * 70)

    for query in test_cases:
        result = should_search(query)
        passed = result is True

        if passed:
            correct += 1

        status = "PASS" if passed else "FAIL"

        print(f"\n[{status}]")
        print(f"Query: {query}")
        print(f"Expected: True")
        print(f"Got: {result}")

    recall = (correct / total) * 100

    print("\n" + "=" * 70)
    print(f"SEARCH RECALL: {correct}/{total} ({recall:.1f}%)")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
