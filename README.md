# Deep Learning Week 2022 - Hackathon

**Team**: semaphores 

**Solution:** see-maphores

**Description:** a realtime webcam that detects and analyses an object, generates descriptions of the surrounding objects, reads the generated outputs and speaks out them in the language users prefer.


## Inspiration
Technologies and AIs have always been marketed as the magical cure for all, bringing convenience and efficiency to all aspects of our daily lives. As magical as it might sound, this only applies to the mainstream users, leaving behind the visually impaired, the elderlies, the mentally disabled, etc. How might we make technologies more accessible and inclusive to them? How might we use technologies to target their specific needs? How might we include them in our race toward the Smart Nation and minimize any marginalizing effects created by the current mainstream technologies?

Out of all the marginalized groups, we identified the visually impaired population as our target audience. This is not only because of the scale and magnitude of visual impairment in Singapore and worldwide, but also because of how impacts of visual impairments directly extend all walks of life.

## What it does
We developed a realtime webcam that detects and analyses an object, generates descriptions of the surrounding objects, reads the generated outputs and speaks out them in the language users prefer.

## How we built it
We integrated the following to build our solution:
- YOLOv5 (You Only Look Once) object-detection model 
- Tesseract ocr / EasyOCR: optical character recognition engine 
- gTTS (Google Text To Speech) 
- Google Translate API 

## Challenges we ran into
We had difficulty incorporating different functions.

## Accomplishments that we're proud of
We incorporated different functions.

## What we learned
We learned how to incorporate different functions and we also learned how to use different AI models. 

## What's next for see-maphores
- Use a better dataset for detecting objects
- Use a better ocr for better accuracy
- Incorporate a location tracker to tell the user where he/she is located
- Incorporate into hardware, such as AR glasses
