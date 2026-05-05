# Agent Message Simulation System

## What Is This Project?

This project simulates how agents in a workplace communicate with each other by sending and receiving messages. Each agent has a role — **Manager, Worker, or HR** — and automatically replies to messages based on that role.

Think of it like a virtual office where:
- The **Manager** gives tasks and makes decisions
- The **Workers** receive tasks and report back
- **HR** handles leave requests, salary issues, and staff welfare

This project was built for **CSC 309 — Artificial Intelligence**, covering the topic of **Agents and Message Passing in Multi-Agent Systems.**

---

## Project Details

| Field | Details |
|---|---|
| Course | CSC 309 — Artificial Intelligence |
| Project Number | Project 19 |
| Topic | Model for Simulating a Message Between Agents |
| Tools Used | Python / HTML, CSS, JavaScript |
| Author | Chidiebube |

---

## The Agents

| Name | Role | What They Do |
|---|---|---|
| Ebube | Manager | Assigns tasks, approves requests, makes decisions |
| Jude | Worker | Receives tasks, asks questions, reports progress |
| Emma | Worker | Submits reports, raises concerns |
| Adaeze | HR | Handles leave, payroll, and staff matters |
| Chikum | Worker | Prepares presentations, attends meetings |

---

## Project Files

```
agent-simulation/
│
├── agent_simulation.html    # Web version (runs in browser)
├── agent_simulation.py      # Python version (runs in terminal)
└── README.md                # Project documentation (this file)
```

---

## How to Run — Python Version

### Step 1 — Make sure Python is installed
```bash
python --version
```

### Step 2 — Run the program
```bash
python agent_simulation.py
```

### What You Will See
The program runs automatically in 4 rounds:

- **Round 1** — Manager (Ebube) assigns tasks to the Workers
- **Round 2** — Workers contact HR with leave and salary requests
- **Round 3** — HR reports back to the Manager
- **Round 4** — All agents read their messages and reply automatically
- At the end, a full message log and activity summary is printed

---

## How to Run — Web Version

### Option 1 — Open in Chrome directly
1. Download the `agent_simulation.html` file
2. Right-click the file
3. Select **Open with → Google Chrome**

### Option 2 — Live Server in VS Code
1. Open the file in VS Code
2. Right-click inside the code
3. Click **Open with Live Server**

### Option 3 — Put it online with GitHub Pages
1. Upload the file to a GitHub repository
2. Go to **Settings → Pages**
3. Set branch to `main` and save
4. Your project goes live at: `https://yourusername.github.io/agent-simulation`

---

## Web Version Features

- **5 Quick Scenario Buttons** — click any to watch agents send messages automatically
- **Live Message Feed** — every message appears on screen with an automatic reply from the receiver
- **Compose a Message** — manually pick a sender, a receiver, type a subject and message, then send
- **Stats Bar** — tracks how many messages have been sent and how many rounds have run
- **Clear Feed Button** — resets everything and starts fresh

---

## Key Concepts Explained Simply

### What is an Agent?
In Artificial Intelligence, an **agent** is any system that can perceive its environment and take actions. In this project, each person (Ebube, Jude, Emma etc.) is an agent. They receive messages (perceive) and reply to them (take action).

### What is a Multi-Agent System?
A **Multi-Agent System** is when multiple agents exist in the same environment and interact with each other. This office simulation is a multi-agent system because all 5 agents communicate and respond to one another.

### What is Message Passing?
**Message passing** is the way agents communicate in a multi-agent system. Instead of sharing memory directly, each agent sends structured messages to other agents. Each message has a sender, a receiver, a subject, and content — just like an email.

### How Do Agents Decide What to Reply?
Each agent has a set of pre-written responses based on their role. When a message arrives, the agent picks one of those responses randomly. This is a simple form of **rule-based behaviour** — the agent follows rules based on who they are.

---

## Example Conversation

```
[09:14:22]  Ebube (Manager)  →  Jude (Worker)
            Subject : New Project Assignment
            Message : Jude, please begin work on the client
                      database module. Deadline is Friday.

[09:14:22]  Jude replies:
            Got it! I will keep you updated on my progress.

─────────────────────────────────────────────
[09:14:23]  Jude (Worker)  →  Adaeze (HR)
            Subject : Leave Application
            Message : Hi Adaeze, I would like to apply for
                      3 days leave next week. Please advise.

[09:14:23]  Adaeze replies:
            This has been logged in our HR system.
            We will follow up within 24 hours.
```

---

## Limitations

- **Random replies** — agents pick responses randomly from a list. They do not truly understand the message content
- **No memory** — agents do not remember previous conversations. Each message is treated independently
- **Fixed agents** — you cannot add new agents without editing the code
- **No real AI decision making** — this is a rule-based simulation, not a learning AI

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Terminal version of the simulation |
| HTML | Structure of the web page |
| CSS | Design and styling of the website |
| JavaScript | Message logic and interactivity in the browser |

---

## References

- Multi-Agent Systems — [Wikipedia](https://en.wikipedia.org/wiki/Multi-agent_system)
- Intelligent Agents — [Wikipedia](https://en.wikipedia.org/wiki/Intelligent_agent)
- Message Passing — [Wikipedia](https://en.wikipedia.org/wiki/Message_passing)
