Project Structure
The main Python script main.py defines a PyQt6 application and a QMainWindow for user interaction. The mem_gen_request.py file contains functions to interact with the apimeme.com API.

The important classes and methods are:

class Memgen(QDialog) - This class inherits from PyQt6's QDialog class and provides all functionality for user interaction.

generate_mem_image(self) - This method gets user inputs, requests the meme generation from the apimeme.com API, displays the generated meme in the GUI, and adjusts the size of the window to fit the meme.

clear(self) - This method clears the user inputs and hides the meme image.
Requirements
Python 3.8 or newer.
PyQt6 library.
You will need to install requests module.
Setup & Installation
To install and run the project, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/aburenin/MemeGen.git
Change into the cloned directory:
bash
Copy code
cd MemeGen
Install the required Python dependencies:
Copy code
pip install -r requirements.txt
Run the main.py script:
css
Copy code
python main.py
Usage
To use the MemeGen application:

Enter the top and bottom texts for your meme.
Select the meme template from the dropdown menu.
Click the "Generate" button to create and display your meme.
Click the "Clear" button to clear the text fields and hide the meme image.
Contributing
If you'd like to contribute to the project, please fork the project, make your changes, and submit a pull request. All contributions are welcome!
