import google.generativeai as genai
import json

class InterviewBot:
    def __init__(self, system_prompt, tech_prompt_first, tech_prompt_followup, api_key):
        self.system_prompt = system_prompt
        self.tech_prompt_first = tech_prompt_first
        self.tech_prompt_followup = tech_prompt_followup
        self.state = "collect_name"
        self.candidate = {}
        self.questions = []
        self.current_q = 0

        # Configure Gemini with API key
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def ask_llm(self, text):
        response = self.model.generate_content(text)
        return response.text.strip()

    def save_candidate(self):
        with open("candidate_data.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(self.candidate, ensure_ascii=False) + "\n")

    def start(self):
        return "Let's get started. Please tell me your full name."

    def step(self, user_input):
        if not user_input.strip():
            return "If you'd like to stop, type 'exit'. Otherwise, please answer."
        if user_input.strip().lower() in ["exit", "quit"]:
            self.save_candidate()
            return "Thank you for your time. Have a great day!"

        # === candidate info collection ===
        if self.state == "collect_name":
            self.candidate["name"] = user_input
            self.state = "collect_email"
            return "Please provide your email address."

        elif self.state == "collect_email":
            self.candidate["email"] = user_input
            self.state = "collect_phone"
            return "Please provide your phone number."

        elif self.state == "collect_phone":
            self.candidate["phone"] = user_input
            self.state = "collect_experience"
            return "How many years of experience do you have?"

        elif self.state == "collect_experience":
            self.candidate["experience"] = user_input
            self.state = "collect_position"
            return f"Thanks! With {user_input} years of experience, which position are you applying for?"

        elif self.state == "collect_position":
            self.candidate["position"] = user_input
            self.state = "collect_location"
            return f"Okay, aiming for {user_input}. What is your preferred work location?"

        elif self.state == "collect_location":
            self.candidate["location"] = user_input
            self.state = "collect_techstack"
            return "Great! Please tell me your primary tech stack (e.g., Python, React, SQL)."

        # === technical Q&A ===
        elif self.state == "collect_techstack":
            self.candidate["techstack"] = user_input
            self.state = "technical_qna"
            self.questions = []
            self.current_q = 0

            # First technical question
            tech_prompt = self.tech_prompt_first.format(stack=user_input)
            question = self.ask_llm(tech_prompt)
            self.questions.append(question)
            return f"Let's begin the technical round.\n{question}"

        elif self.state == "technical_qna":
            # Save candidate’s answer
            q_key = f"q{self.current_q+1}"
            self.candidate[q_key] = {
                "question": self.questions[self.current_q],
                "answer": user_input
            }

            self.current_q += 1
            if self.current_q < 5:
                asked_str = "; ".join(self.questions)
                tech_prompt = self.tech_prompt_followup.format(
                    stack=self.candidate["techstack"],
                    answer=user_input,
                    asked=asked_str
                )
                next_q = self.ask_llm(tech_prompt)
                self.questions.append(next_q)
                return next_q
            else:
                self.state = "done"
                self.save_candidate()
                return "That concludes the technical round. Thank you for your answers!"

        elif self.state == "done":
            return "Thank you! The interview is complete."

        return "Sorry, I didn’t understand that."
