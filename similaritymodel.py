# similaritymodel.py
# Semantic similarity using Sentence-BERT embeddings

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load a small, fast semantic model (only once)
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(job_text: str, resume_text: str) -> float:
    """
    Uses semantic embeddings to compute meaning-based similarity between
    job description and resume text. Returns a 0–100% match score.
    """
    if not job_text.strip() or not resume_text.strip():
        return 0.0
  
    # Create sentence embeddings (vector representations)
    job_vec = model.encode([job_text])
    resume_vec = model.encode([resume_text])

    # Cosine similarity of the two meaning vectors
    score = cosine_similarity(job_vec, resume_vec)[0][0]

    # Convert cosine (0–1) to percentage scale
    score_percent = round(float(score) * 100, 2)
    return score_percent
