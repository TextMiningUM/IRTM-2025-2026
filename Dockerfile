FROM jupyter/datascience-notebook:python-3.10

USER root
RUN apt-get update && apt-get install -y openjdk-11-jre-headless && apt-get clean

# 1. Maak een aparte map aan die niet wordt 'overruled' door de student-disk
RUN mkdir -p /opt/course-data

# 2. Kopieer de bestanden daarheen
COPY . /opt/course-data/

# 3. Zet de rechten goed
RUN chown -R ${NB_UID}:${NB_GID} /opt/course-data

USER ${NB_USER}
# (Pip installaties blijven hetzelfde)
RUN pip install --no-cache-dir nltk beautifulsoup4 langdetect python-terrier pyserini faiss-cpu sentence-transformers
RUN python -c "import nltk; nltk.download(['punkt', 'punkt_tab', 'stopwords', 'wordnet', 'omw-1.4', 'averaged_perceptron_tagger_eng'])"

WORKDIR /home/jovyan

RUN pip install --no-cache-dir nbgitpuller