import tkinter as tk

class MCQGame:
    def __init__(self, master):
        self.master = master
        self.question_index = 0
        self.score = 0

        self.questions = [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "correct_answer": "Jupiter"
            },
            {
                "question": "What is 2+2?",
                "options": ["2", "4", "22","3"],
                "correct_answer":"22"
            }
        
        ]
        self.total_questions = len(self.questions)
        self.current_question = self.questions[self.question_index]
        self.question_label = tk.Label(master, text=self.current_question["question"])
        self.question_label.pack()
        self.radio_var = tk.StringVar()
        self.radio_var.set(None)
        self.radio_buttons = []

        for option in self.current_question["options"]:
            radio_button = tk.Radiobutton(master, text=option, variable=self.radio_var, value=option)
            radio_button.pack()
            self.radio_buttons.append(radio_button)

        self.submit_button = tk.Button(master, text="Submit", command=self.process_answer)
        self.submit_button.pack()

        self.feedback_label = tk.Label(master, text="")
        self.feedback_label.pack()

    def process_answer(self):
        selected_answer = self.radio_var.get()
        correct_answer = self.current_question["correct_answer"]

        if selected_answer == correct_answer:
            self.score += 1

        if self.question_index < self.total_questions - 1: 
            self.question_index += 1
            self.display_next_question()
        else:
            self.display_final_score()


                   
    def display_next_question(self):
        self.current_question = self.questions[self.question_index]
        self.question_label.config(text=self.current_question["question"])
        self.radio_var.set(None)

        for i, radio_button in enumerate(self.radio_buttons):
            if i < len(self.current_question["options"]):
                radio_button.config(text=self.current_question["options"][i])
                radio_button.pack()  
            else:
                radio_button.pack_forget()

        self.feedback_label.config(text="")

    def display_final_score(self):
        selected_answer = self.radio_var.get()
        correct_answer = self.current_question["correct_answer"]

        if selected_answer == correct_answer:
            self.score += 1
            
        for widget in self.master.winfo_children():
            widget.pack_forget()

        self.feedback_label.config(text=f"Quiz ended. Your score is: {self.score}/{self.total_questions}")
        self.feedback_label.pack()

def main():
    root = tk.Tk()
    root.title("MCQs Game")
    game = MCQGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()