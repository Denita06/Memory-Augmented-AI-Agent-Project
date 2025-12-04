from fileinput import filename

from reader import read_file
from agent import study_helper_agent
from utils import save_output

def main():
    while True:
        file_path = input("Enter the path to your PDF or DOCX file: ").strip()
        if not file_path:
            print("No file path provided. Exiting...")
            break

        try:
            file_content = read_file(file_path)
        except Exception as e:
            print("Error reading file:", e)
            return

        print("\nGenerating document preview...\n")

        # Generate a preview of the document without calling OpenAI API
        preview = study_helper_agent(file_content, use_api=False)
        print("\n---Document Preview---\n")
        print(preview['content'])

        print("\n---Summary---\n")
        print(preview['summary'])

        print("\n--- Key Concepts ---\n")
        for idx, point in enumerate(preview['key_concepts'], 1):
            print(f"{idx}.{point}")

        print("\n--- Suggested Study Schedule ---\n")
        print(preview['mock_schedule'])


        save_preview = input("\nSave preview to file (y/n): ").strip().lower()
        if save_preview == "y":
            save_output(preview['content'], filename="study_preview.txt")

        generate_full_studyguide = input("\nGenerate full study guide using AI? (y/n): ").strip().lower()
        if generate_full_studyguide == "y":
            response = study_helper_agent(file_content, use_api=True)

            print("\n---Study Guide Output---\n")
            if "content" in response:
                print(response['content'])
                save_full = input("\nSvae full study guide to file (y/n): ").strip().lower()
                if save_full == "y":
                    save_output(response['content'], filename="study_guide.txt")
            else:
                print("Cannot generate study guide:", response.get("error"))

        other_files = input("\nProcess another file? (y/n): ").strip().lower()
        if other_files != "y":
            break

if __name__ == "__main__":
    main()