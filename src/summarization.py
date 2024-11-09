from transformers import pipeline


def summarize(text, min, max):

    summarizer = pipeline("summarization", model="t5-base")
    summary = summarizer(text, max_length=max, min_length=min, do_sample=False)
    print(summary[0]['summary_text'])
    return summary[0]['summary_text']