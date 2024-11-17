# Image generation model
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
from PIL import Image

img_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
img_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Image to Text Captioning
def image_to_text(image):
  inputs = img_processor(images=image, return_tensors="pt")
  out = img_model.generate(**inputs)
  return img_processor.decode(out[0], skip_special_tokens=True)


# --------------------Translation of text-------------------------------------------------------


import torch
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
)
from IndicTransToolkit import IndicProcessor


model_name = "ai4bharat/indictrans2-en-indic-1B"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True)

ip = IndicProcessor(inference=True)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
src_lang, tgt_lang = "eng_Latn", "hin_Deva"

def text_translation(text, tgt_lang, src_lang="eng_Latn"):
  batch = ip.preprocess_batch(
    [text],
    src_lang=src_lang,
    tgt_lang=tgt_lang,
  )

  # Tokenize the sentences and generate input encodings
  inputs = tokenizer(
    batch,
    truncation=True,
    padding="longest",
    return_tensors="pt",
    return_attention_mask=True,
  ).to(DEVICE)

  # Generate translations using the model
  with torch.no_grad():
    generated_tokens = model.to(DEVICE).generate(
        **inputs,
        use_cache=True,
        min_length=0,
        max_length=256,
        num_beams=5,
        num_return_sequences=1,
    )

  # Decode the generated tokens into text
  with tokenizer.as_target_tokenizer():
    generated_tokens = tokenizer.batch_decode(
        generated_tokens.detach().cpu().tolist(),
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True,
    )

  # Postprocess the translations, including entity replacement
  translations = ip.postprocess_batch(generated_tokens, lang=tgt_lang)
  return translations[0]


#  ------------------------


from gtts import gTTS
from IPython.display import Audio, display

def speak(text, language='en'):
  tts = gTTS(text=text, lang=language, slow=False)
  tts.save("./audio/output.mp3")
  return 'output.mp3'


import gtts

# Get a dictionary of languages supported by gtts
languages = gtts.lang.tts_langs()

# languages supported by IndicTrans2
flores_codes = {
    "asm_Beng": "as",
    "awa_Deva": "hi",
    "ben_Beng": "bn",
    "bho_Deva": "hi",
    "brx_Deva": "hi",
    "doi_Deva": "hi",
    "eng_Latn": "en",
    "gom_Deva": "kK",
    "guj_Gujr": "gu",
    "hin_Deva": "hi",
    "hne_Deva": "hi",
    "kan_Knda": "kn",
    "kas_Arab": "ur",
    "kas_Deva": "hi",
    "kha_Latn": "en",
    "lus_Latn": "en",
    "mag_Deva": "hi",
    "mai_Deva": "hi",
    "mal_Mlym": "ml",
    "mar_Deva": "mr",
    "mni_Beng": "bn",
    "mni_Mtei": "hi",
    "npi_Deva": "ne",
    "ory_Orya": "or",
    "pan_Guru": "pa",
    "san_Deva": "hi",
    "sat_Olck": "or",
    "snd_Arab": "ur",
    "snd_Deva": "hi",
    "tam_Taml": "ta",
    "tel_Telu": "te",
    "urd_Arab": "ur",
}

# Create a dictionary to store supported languages and their codes which are common supported by both gtts and IndicTrans2
supported_lang = {}

# Iterate through the languages dictionary and check for matching codes
for key, value in languages.items():
  for key1, value1 in flores_codes.items():
    if key == value1:
      supported_lang[value] = [key, key1]
      break

# get the code of lang supported by gtts
def get_item_by_value(target_value, dictionary=supported_lang):
    for key, values in dictionary.items():
        if target_value in values:
            return values[0]
    return None  # Return None if not found


import io

# image to audio pipeline
def image_to_text_to_audio(image, lang="eng_Latn"):
  img = Image.open(io.BytesIO(image.read()))
  tts_lang = get_item_by_value(lang)
  if tts_lang is None:
    print("Language not supported")
    return
  # get the caption
  text = image_to_text(img)
  print(f"Image Caption: {text}")

  # translate the caption to the target language
  if lang == 'eng_Latn':
      return text
  translated_text = text_translation(text, lang)
  print(f"Translated Text: {translated_text}")

  # convert the text to speech
  audio = speak(translated_text, tts_lang)
  return translated_text
#   display(audio)

