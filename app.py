from llm import analyze_email


print("=" * 60)
print("       AI GMAIL EMAIL SECURITY SYSTEM")
print("=" * 60)


email = input("\nEnter your email/message:\n")


print("\nAnalyzing email using LLM...\n")


result = analyze_email(email)


print("=" * 60)
print("                 AI RESULT")
print("=" * 60)

print(result)

print("=" * 60)