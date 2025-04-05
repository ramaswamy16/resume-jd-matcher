import difflib

def compare_texts(resume_text, jd_text):
    sequence = difflib.SequenceMatcher(None, resume_text, jd_text)
    similarity = sequence.ratio()
    return similarity

# Example usage
if __name__ == "__main__":
    resume = "Experienced Product Manager with automation, AI, and analytics skills..."
    jd = "Looking for a Product Manager with experience in AI, automation, and agile..."
    similarity_score = compare_texts(resume, jd)
    print(f"Resume-JD Similarity: {similarity_score * 100:.2f}%")
