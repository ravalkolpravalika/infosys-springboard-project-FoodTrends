import pandas as pd
from textblob import TextBlob

# Load dataset
df = pd.read_excel(r"C:\Users\raval\OneDrive\Desktop\final_project_dataset.xlsx")

# Ensure all text is string
df["text"] = df["text"].astype(str)

# Function to get sentiment
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.05:
        label = "POSITIVE"
    elif polarity < -0.05:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"
    return pd.Series([label, polarity])

# Apply to all rows
df[["sentiment_label", "sentiment_score"]] = df["text"].apply(get_sentiment)

# Save results
df.to_excel(r"C:\Users\raval\OneDrive\Desktop\final_project_sentiment_output.xlsx", index=False)

print("Done! Output saved at 'final_project_sentiment_output.xlsx'")
