
# BEFORE RUNNING THE FILES EXECUTE THE FOLLOWING IN THE TERMINAL FROM THE WORKING FOLDER:
pip install -r requirements.txt

## main.py - HOW IT WORKS:

Select PDF: The user selects a PDF file using a file dialog.
Extract text: The text is extracted using PyPDF2.
Convert to speech: The extracted text is passed to pyttsx3 to generate the audio file and save it.

## main2.py - UPDATE:

No Threading: The code runs sequentially in the main thread without using threading.
UI Update: The cursor and button are updated before and after the long-running task using root.update(), ensuring the UI reflects the changes. The button is disabled and the cursor is set to "wait" before starting the process, and reset after.
reset_ui Function: A helper function resets the UI state (cursor and button) after the conversion process.

## main3.py - UPDATE 2 THAT USES PyMuPDF library instead of PyPDF2 to extract in chunks:

PyMuPDF for Paragraph Chunks:

    fitz.open(pdf_path) opens the PDF file.
    page.get_text("text") extracts the text from each page.
    The text is split into paragraph chunks using split("\n\n"), which is useful for speech synthesis.

Feeding Text Chunks to pyttsx3:

The pyttsx3.say(chunk) function is called for each paragraph chunk, converting it to speech.
After processing each chunk, engine.runAndWait() ensures it’s spoken before moving to the next chunk.

Cursor Handling:

The cursor is set to "wait" during processing, and root.update() is called to refresh the UI. This should work better since the tasks are processed in small chunks, giving Tkinter enough time to update the interface between chunks.

## main-with-threading.py - HOW IT WORKS:

Threading: The conversion task runs in a separate thread using Python's threading.Thread. This ensures that the Tkinter UI remains responsive during the process.

Hourglass Cursor: The cursor is changed to an hourglass (or "wait" cursor) while the conversion is happening:

    root.config(cursor="wait") sets the busy cursor.
    root.config(cursor="") resets the cursor to normal when the task is done.

Disabling the Button: The "Generate Audiobook" button is disabled during processing to prevent multiple conversions running simultaneously (select_button.config(state="disabled")).

## main-with-threading-2.py - UPDATE:

root.update(): After changing the cursor to "wait", I added root.update() to force the UI to refresh immediately, making the cursor change visible before the long-running task starts.

