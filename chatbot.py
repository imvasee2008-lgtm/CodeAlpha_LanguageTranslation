faqs = {
    "college timing": "College timing is 9 AM to 4 PM.",
    "library timing": "Library timing is 8 AM to 6 PM.",
    "principal name": "The principal name is Dr. Kumar.",
    "placement cell": "Placement cell is located on the second floor."
}

question = input("Ask your question: ").lower()

if question in faqs:
    print("Answer:", faqs[question])
else:
    print("Sorry, answer not available.")