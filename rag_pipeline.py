from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

tokenizer = AutoTokenizer.from_pretrained(
    "flan-t5-base",
    local_files_only=True
)
model = AutoModelForSeq2SeqLM.from_pretrained(
    "flan-t5-base",
    local_files_only=True
)

llm = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1,          # CPU only
    max_new_tokens=200  # ✅ MOVE IT HERE
)

def generate_answer(query, retriever):
    # 1️⃣ Retrieve documents
    docs = retriever.invoke(query)

    if not docs:
        return "कोऽपि सन्दर्भः न प्राप्तः।"

    # 2️⃣ Limit context length (CRITICAL)
    context = "\n".join([doc.page_content for doc in docs[:2]])

    # 3️⃣ Strong, explicit prompt
    prompt = (
        "तुम् संस्कृत् विशेषज्ञः असि।\n"
        "अधोलिखितसन्दर्भस्य आधारेण प्रश्नस्य संक्षिप्तं स्पष्टं उत्तरं संस्कृतेन लिख।\n\n"
        f"सन्दर्भः:\n{context}\n\n"
        f"प्रश्नः: {query}\n"
        "उत्तरम्:"
    )

    # 4️⃣ Generate
    output = llm(prompt)

    # 5️⃣ SAFELY extract answer
    if isinstance(output, list) and "generated_text" in output[0]:
        answer = output[0]["generated_text"].strip()
        if answer:
            return answer

    return "उत्तरं जनयितुं असफलम्।"
