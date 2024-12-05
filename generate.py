import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

class SVGGenerator:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('VITE_GEMINI_API')
        
        if not self.api_key:
            raise ValueError("Gemini API key is required")
        
        self.llm = ChatGoogleGenerativeAI(
            model= 'gemini-1.5-pro',
            google_api_key=self.api_key,
            temperature=1,
            max_tokens=8192
        )
    
    def generate_svg(self, object_name):
        """
        Generate SVG for a specific object and print to terminal
        """
        prompt = f"""
        Create a valid SVG illustration of a {object_name}
        - Use clean, simple geometric shapes
        - Include xmlns attribute
        - Make it recognizable
        """
        
        svg_content = self.llm.invoke(prompt).content
        print("\n--- Generated SVG for", object_name, "---")
        print(svg_content)
        return svg_content

def main():
    generator = SVGGenerator()
    
    try:
        # Get object from user
        object_name = input("Enter the object you want as an SVG (e.g., truck, car, house): ")
        
        # Generate and print SVG
        generator.generate_svg(object_name)
    
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()