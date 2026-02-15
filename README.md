# Sophiie AI Agents Hackathon 2026

**Build the future of AI-human interaction.**

| | |
|---|---|
| **What** | A solo hackathon focused on AI agent interaction — voice, text, UX, and UI |
| **When** | February 14–15, 2026 (Saturday–Sunday) |
| **Where** | Virtual — participate from anywhere in Australia |
| **Prize** | **$5,000 AUD cash** (1st place) + job offers for top performers |
| **Format** | Solo only — show us what *you* can build |
| **Hacking Time** | 33 hours |

---

## The Challenge

**Design and build an AI agent with an exceptional interaction experience.**

We want to see how you think about the space between humans and AI. This is deliberately open-ended — you choose the problem, the modality, and the approach. What matters is the *interaction*.

Some directions to inspire you (not requirements):

- A voice agent that feels natural to talk to
- A text-based assistant with a thoughtful, intuitive UX
- A multi-modal agent that blends voice, text, and visual elements
- An agent that handles a complex workflow through conversation
- Something we haven't thought of yet

**You will be judged on innovation, technical execution, and how good the interaction feels** — not just whether the AI works, but whether a human would *want* to use it.

Use any tech stack. Use any AI provider. Use AI coding assistants. The only constraint is time.

---

## Schedule

All times are **AEST (Australian Eastern Standard Time, UTC+10 — Brisbane time)**.

### Saturday, February 14

| Time | Event |
|------|-------|
| **9:00 AM** | Kickoff — challenge explained, rules confirmed |
| **9:30 AM** | **Hacking begins** |
| 12:00 PM | Office hours / Q&A (optional, Discord) |
| 4:00 PM | Community check-in / progress sharing (optional, Discord) |

### Sunday, February 15

| Time | Event |
|------|-------|
| **6:00 PM** | **Submission deadline — hard cut-off, no exceptions** |

### After the Hackathon

| When | Event |
|------|-------|
| Feb 16 – Feb 28 | Judging period — judges review all submissions |
| ~Early March | Winners announced via livestream (details shared on Discord and Email) |

---

## Rules

### The Essentials

1. **Solo only** — one person per submission, no teams
2. **No pre-work** — all project code must be written during the hackathon window (after 9:30 AM AEST, Feb 14)
3. **Public GitHub repo** — your repository must be publicly visible at time of submission
4. **AI assistance is allowed** — Copilot, Claude, ChatGPT, Cursor, whatever you want. You still need to build it within the timeframe
5. **Must be functional** — your project must run and be demonstrable, not just a concept or slide deck
6. **One submission per person** — you may iterate, but submit one final project

### What You CAN Prepare Before Kickoff

- Research, planning, and brainstorming (on paper, in your head — just not in code)
- Setting up your development environment
- Reading documentation for tools/APIs you plan to use
- Creating accounts (GitHub, API providers, etc.)
- Watching tutorials

### What You CANNOT Do Before Kickoff

- Write any project code
- Create your project repository
- Fork/clone an existing project and modify it
- Build components, libraries, or templates specifically for your submission
- Start a project in a private repo then make it public later

### How We Verify

We will check:
- **Repository creation date** — must be after 9:30 AM AEST, Feb 14
- **Commit history** — should show natural progression, not a single massive commit
- **First commit timestamp** — must be after kickoff

**Red flags that will result in disqualification:**
- Repo created before the hackathon
- Single commit containing the entire project
- Commits timestamped before kickoff
- Evidence of code copied from a pre-existing private repo

---

## Submission Requirements

**Deadline: 6:00 PM AEST, Sunday February 15, 2026 — hard cut-off.**

To submit, you must complete **all** of the following:

1. **Public GitHub repo** — created after kickoff, with a clear commit history
2. **This README** — fill out the [Your Submission](#your-submission) section below
3. **Demo video** (2–5 minutes) — show your agent in action, explain your approach
4. **Working project** — judges must be able to understand and evaluate your agent from the repo + video

### How to Submit

1. Fork this repository
2. Build your project in the fork
3. Fill out the [Your Submission](#your-submission) section below
4. Record your demo video and add the link to your submission
5. Ensure your repo is **public** before 6:00 PM AEST Sunday
6. Submit your repo link via the submission form (link will be shared at kickoff)

---

## Judging Criteria

| Criteria | Weight | What We're Looking For |
|----------|--------|----------------------|
| **Interaction Design** | 30% | How intuitive, natural, and delightful is the human-AI interaction? Does it feel good to use? |
| **Innovation** | 25% | Novel approach, creative problem-solving, or a fresh take on agent interaction |
| **Technical Execution** | 25% | Code quality, architecture, reliability, completeness |
| **Presentation** | 20% | Demo quality, clarity of communication, ability to convey your vision |

### Judges

Sophiie senior engineers and CTO. Judging will take place over a 2-week period following the submission deadline.

---

## Prizes

| Place | Prize |
|-------|-------|
| **1st Place** | **$5,000 AUD cash** |
| **Top Performers** | Job offers or interview fast-tracks at Sophiie* |
| **All Finalists** | Consideration for current and future roles |

*\*Job offers and interview fast-tracks are entirely at the discretion of Sophiie and are not guaranteed.*

> Participants retain full ownership and IP of their submissions. Sophiie receives a non-exclusive license to review and evaluate submissions for judging purposes only.

---

## Your Submission

> **Instructions:** Fill out this section in your forked repo. This is what judges will see first.

### Participant

| Field | Your Answer |
|-------|-------------|
| **Name** | Phanikiran Pisipati|
| **University / Employer** |NSW Department of Customer Service |

### Project

| Field | Your Answer |
|-------|-------------|
| **Project Name** | DocuBot: AI Powered UiPath Documentation Assistant |
| **One-Line Description** | The proposed UiPath chatbot will be an AI-powered system that will be trained on a 
massive dataset of UiPath documentation and forum posts. It will be able to: 
• Answer questions about UiPath: The chatbot will be able to answer a wide 
range of questions about UiPath, including questions about the platform, the 
various components of the platform, and how to use the platform to automate 
various tasks. 
• Generate code snippets: The chatbot will be able to generate code snippets in 
UiPath's programming language, UiPath Robot Language (UIR). This will 
make it easier for users to automate tasks without having to write code from 
scratch. 
• Provide step-by-step instructions: The chatbot will be able to provide step-by- 
step instructions on how to automate various tasks using UiPath. This will 
make it easier for users to learn how to use UiPath, even if they have no prior 
experience with automation. 
The chatbot will be integrated with the UiPath platform so that users can easily 
access it from within the UiPath environment. It will also be available as a standalone 
application, so that users can access it from anywhere. 
Here is a detailed description of how the chatbot will work: 
1. The user will ask a question or give a command to the chatbot. 
2. The chatbot will use Retravel Augmentation Generation (RAG) from Pinecone 
vector DB to retrieve top K chunks based on cosine similarity measure 
between the embeddings present in the DB and the user requested question. 
3. Vector DB search result, the context and prompt engineering will be used by 
the LLM to generate a response to the user's request. The response may be a 
simple answer, a code snippet, or step-by-step instructions. 
The chatbot will be trained using a variety technique, including: 
• Reinforcement learning with human feedback (RLHF): The chatbot will be 
trained on a simulated environment where it can interact with UiPath and 
receive feedback on its performance. This feedback will help the chatbot to 
learn how to generate better responses to user requests. 
The chatbot will be deployed on a cloud platform so that it can be accessed by users 
from anywhere. The chatbot will also be designed to be scalable so that it can 
handle a large number of concurrent users. 
We believe that the proposed UiPath chatbot has the potential to be a valuable tool 
for UiPath users of all levels of experience. It will help users to automate their tasks 
more quickly and efficiently, and it will make UiPath more accessible to a wider 
range of users.|
| **Demo Video Link** | |
| **Tech Stack** | UiPath Forms.GPT-4: Large Language Model (LLM) •  RAG: To answer questions about the documentation using the vector DB 
• Langchain: A framework to interact with LLM 
• Pinecone vector DB: To store and retrieve the numerical vector embeddings.

 |
| **AI Provider(s) Used** |GPT-4: Large Language Model (LLM) •  RAG: To answer questions about the documentation using the vector DB 
• Langchain: A framework to interact with LLM  |

### About Your Project
1. Problem Statement 
UiPath documentation is vast and complex, making it difficult for users to find the 
information they need. This can lead to decreased productivity, increased errors, and 
frustration for users. 
Opportunity 
An AI-powered UiPath Documentation Assistant can help to solve this problem by 
providing users with a single, easy-to-use interface for accessing all of the UiPath 
documentation. This Assistant uses Generative AI to understand the user's query and 
provide them with the most relevant information. 
Proposed Solution 
We propose to develop an AI-powered UiPath Documentation Assistant using the 
following technologies: 
• Gen API: To generate documentation from scratch or update existing 
documentation. 
• GPT-4: Large Language Model (LLM) 
• RAG: To answer questions about the documentation using the vector DB 
• Langchain: A framework to interact with LLM 
• Pinecode vector DB: To store and retrieve the numerical vector embeddings. 
Our solution will be integrated with the UiPath platform, so that users can easily access 
it from within the UiPath environment. 
Benefits 
An AI-powered UiPath Documentation Assistant can provide a number of benefits to 
users, including: 
• Increased productivity: Users can spend less time searching for and trying to 
understand UiPath documentation. 
• Reduced errors: Users are less likely to make mistakes when they are using 
the Assistant to access accurate and up-to-date documentation. 
• Improved user experience: The Assistant will provide a more user-friendly and 
interactive way to access UiPath documentation. 
We believe that the AI-powered UiPath Documentation Assistant will be a valuable 
tool for UiPath users of all levels of experience. It will help users to automate their 
tasks more quickly and efficiently, and it will make UiPath more accessible to a wider 
range of users. 
How our solution addresses the hackathon theme of "AI at Work" 
Our solution addresses the hackathon theme of "AI at Work" by enabling Generative 
AI with LLMs to be used to improve the productivity and efficiency of UiPath users. 
The Assistant will help users to find the information they need quickly and easily, which 
will allow them to automate their tasks more quickly and efficiently. This can lead to 
significant productivity gains for businesses of all sizes. 
We believe that our solution has the potential to make a real difference in the way that 
UiPath is used. We are excited to participate in the hackathon and to demonstrate the 
value of our solution to the UiPath community. 
2. Detailed description of Solution proposed 
The proposed UiPath chatbot will be an AI-powered system that will be trained on a 
massive dataset of UiPath documentation and forum posts. It will be able to: 
• Answer questions about UiPath: The chatbot will be able to answer a wide 
range of questions about UiPath, including questions about the platform, the 
various components of the platform, and how to use the platform to automate 
various tasks. 
• Generate code snippets: The chatbot will be able to generate code snippets in 
UiPath's programming language, UiPath Robot Language (UIR). This will 
make it easier for users to automate tasks without having to write code from 
scratch. 
• Provide step-by-step instructions: The chatbot will be able to provide step-by- 
step instructions on how to automate various tasks using UiPath. This will 
make it easier for users to learn how to use UiPath, even if they have no prior 
experience with automation. 
The chatbot will be integrated with the UiPath platform so that users can easily 
access it from within the UiPath environment. It will also be available as a standalone 
application, so that users can access it from anywhere. 
Here is a detailed description of how the chatbot will work: 
1. The user will ask a question or give a command to the chatbot. 
2. The chatbot will use Retravel Augmentation Generation (RAG) from Pinecone 
vector DB to retrieve top K chunks based on cosine similarity measure 
between the embeddings present in the DB and the user requested question. 
3. Vector DB search result, the context and prompt engineering will be used by 
the LLM to generate a response to the user's request. The response may be a 
simple answer, a code snippet, or step-by-step instructions. 
The chatbot will be trained using a variety technique, including: 
• Reinforcement learning with human feedback (RLHF): The chatbot will be 
trained on a simulated environment where it can interact with UiPath and 
receive feedback on its performance. This feedback will help the chatbot to 
learn how to generate better responses to user requests. 
The chatbot will be deployed on a cloud platform so that it can be accessed by users 
from anywhere. The chatbot will also be designed to be scalable so that it can 
handle a large number of concurrent users. 
We believe that the proposed UiPath chatbot has the potential to be a valuable tool 
for UiPath users of all levels of experience. It will help users to automate their tasks 
more quickly and efficiently, and it will make UiPath more accessible to a wider 
range of users.
#### What does it do?

Our solution will be integrated with the UiPath platform, so that users can easily access 
it from within the UiPath environment. 
Benefits 
An AI-powered UiPath Documentation Assistant can provide a number of benefits to 
users, including: 
• Increased productivity: Users can spend less time searching for and trying to 
understand UiPath documentation. 
• Reduced errors: Users are less likely to make mistakes when they are using 
the Assistant to access accurate and up-to-date documentation. 
• Improved user experience: The Assistant will provide a more user-friendly and 
interactive way to access UiPath documentation. 
We believe that the AI-powered UiPath Documentation Assistant will be a valuable 
tool for UiPath users of all levels of experience. It will help users to automate their 
tasks more quickly and efficiently, and it will make UiPath more accessible to a wider 
range of users.

#### How does the interaction work?

<!-- Describe the user experience — what does a user see, hear, or do when using your agent? -->

#### What makes it special?

The chatbot will be integrated with the UiPath platform so that users can easily 
access it from within the UiPath environment. It will also be available as a standalone 
application, so that users can access it from anywhere. 
Here is a detailed description of how the chatbot will work: 
1. The user will ask a question or give a command to the chatbot. 
2. The chatbot will use Retravel Augmentation Generation (RAG) from Pinecone 
vector DB to retrieve top K chunks based on cosine similarity measure 
between the embeddings present in the DB and the user requested question. 
3. Vector DB search result, the context and prompt engineering will be used by 
the LLM to generate a response to the user's request. The response may be a 
simple answer, a code snippet, or step-by-step instructions. 
The chatbot will be trained using a variety technique, including: 
• Reinforcement learning with human feedback (RLHF): The chatbot will be 
trained on a simulated environment where it can interact with UiPath and 
receive feedback on its performance. This feedback will help the chatbot to 
learn how to generate better responses to user requests. 
The chatbot will be deployed on a cloud platform so that it can be accessed by users 
from anywhere. The chatbot will also be designed to be scalable so that it can 
handle a large number of concurrent users. 
We believe that the proposed UiPath chatbot has the potential to be a valuable tool 
for UiPath users of all levels of experience. It will help users to automate their tasks 
more quickly and efficiently, and it will make UiPath more accessible to a wider 
range of users.

#### How to run it
Have include in repo the runbook : LLM Framework - Documentation
```

#### Architecture / Technical Notes

<!-- Optional: describe your architecture, key technical decisions, or interesting implementation details -->

---<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/2399ea85-f201-4e09-8a34-f64a9a350344" />


## Code of Conduct

All participants must adhere to a standard of respectful, professional behavior. Harassment, discrimination, or disruptive behavior of any kind will result in immediate disqualification.

By participating, you agree to:
- Treat all participants, judges, and organizers with respect
- Submit only your own original work created during the hackathon
- Not interfere with other participants' work
- Follow the rules outlined in this document

---

## Communication & Support

- **Discord** — join the hackathon Discord server for announcements, Q&A, and community chat (link provided upon registration)
- **Office hours** — available during the event for technical questions

---

## FAQ

**Q: Can I use boilerplate / starter templates?**
A: You can use publicly available boilerplate (e.g., `create-react-app`, `Next.js` starter) as a starting point. You cannot use custom templates you built specifically for this hackathon before kickoff.

**Q: Can I use existing open-source libraries and APIs?**
A: Yes. You can use any publicly available libraries, frameworks, APIs, and services. The code *you* write must be created during the hackathon.

**Q: Do I need to be in Australia?**
A: Preferred but not strictly required. The hackathon is primarily targeted at Australian residents and students, but we won't turn away great talent.

**Q: Can I use AI coding tools like Copilot or Claude?**
A: Absolutely. Use whatever tools you want. The 33-hour time constraint is the great equalizer.

**Q: What if I can't finish?**
A: Submit what you have. A well-thought-out partial project with a great demo video can still score well. We're evaluating your thinking and skill, not just completion.

**Q: How will I know if I won?**
A: Winners will be announced via livestream approximately 2 weeks after the hackathon. All participants will be notified.

**Q: Can I keep working on my project after the deadline?**
A: You can continue developing after the hackathon, but **only the state of your repo at 6:00 PM AEST Sunday Feb 15 will be judged**. We will check commit timestamps.

---

## About Sophiie

Sophiie is an AI office manager for trades businesses — helping plumbers, electricians, builders, and other trade professionals run their operations with intelligent automation. We're a team that cares deeply about how humans interact with AI, and we're looking for people who think the same way.

[sophiie.com](https://sophiie.com)

---

**Good luck. Build something that makes us say "wow."**
