from langchain_core.prompts import ChatPromptTemplate

writer_prompt= ChatPromptTemplate.from_messages([
    ("system", "You are a senior technical research assistant."),
    ("human", """
        Question: { questions }
        
        Research notes: { research_notes }
        
        Write a clear, structured, accurate answer.
    
    """)
])

critic_prompt= ChatPromptTemplate.from_messages([
    ("system", "You are a strict reviewer focused on correctness."),
    ("human", """
        Answer: { draft }
        
        
        Return JSON:
        
        {{
            "critique: "...",
            "verdict": true | false
        }}
    """)
])