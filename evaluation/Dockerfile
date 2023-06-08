FROM python:3.6-slim

RUN groupadd -r evaluator && useradd -m --no-log-init -r -g evaluator evaluator

RUN mkdir -p /opt/evaluation /ground-truth /predicted /output \
    && chown evaluator:evaluator /opt/evaluation /ground-truth /predicted /output

USER evaluator
WORKDIR /opt/evaluation

ENV PATH="/home/evaluator/.local/bin:${PATH}"

RUN python -m pip install --user -U pip


COPY --chown=evaluator:evaluator ground_truth.pkl /opt/evaluation/
COPY --chown=evaluator:evaluator jsonloader.py /opt/evaluation/
COPY --chown=evaluator:evaluator requirements.txt /opt/evaluation/
RUN python -m pip install --user -rrequirements.txt

COPY --chown=evaluator:evaluator evaluation.py /opt/evaluation/

ENTRYPOINT "python" "-m" "evaluation"