from transformers import BartForConditionalGeneration, BartTokenizer
from transformers import pipeline


class SummarizerBart:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        # Cargar el modelo y el tokenizador de BART
        self.model_name = model_name
        self.model = BartForConditionalGeneration.from_pretrained(model_name)
        self.tokenizer = BartTokenizer.from_pretrained(model_name)

    def resume(self, text):
        inputs = self.tokenizer.encode(
            "summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = self.model.generate(
            inputs, max_length=300, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

        # Decodificar y mostrar el resumen
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)


class SummarizerBartScientific:
    def __init__(self, model_name="sambydlo/bart-large-scientific-lay-summarisation"):
        # Cargar el modelo y el tokenizador de BART
        self.model_name = model_name
        self.summarizer = pipeline("summarization", model=model_name)

    def resume(self, text):
        # Decodificar y mostrar el resumen
        return self.summarizer(text[:2048])


if __name__ == "__main__":
    summarizer = SummarizerBart()
    print(summarizer.resume(
        'Apple is using deep learning to train the most advanced model in Artificial Intelligence.'))

    summarizer = SummarizerBartScientific()
    print(summarizer.resume(
        'Apple is using deep learning to train the most advanced model in Artificial Intelligence.'))
