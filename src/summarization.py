from transformers import pipeline


def summarize(text, min, max):

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max, min_length=min, do_sample=False)
    return summary[0]['summary_text']