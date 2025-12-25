from graph import app

result= app.invoke({
    "question": "What are the tradeoffs between vector database and graph database?",
    "research_notes": [],
    "draft": "",
    "critique": "",
    "is_good": False,
    "max_iteration": 0
})

print("\nFinal Answer: \n")
print(result["draft"])