# ============================================================
#   Agent Message Simulation System
#   Project 19: Model for Simulating a Message Between Agents
#   Agents: Manager, Worker, HR
# ============================================================
#
# What this program does:
#   It creates a workplace with different types of agents.
#   Each agent has a role (Manager, Worker, HR).
#   Agents can send messages to each other.
#   Each agent reads the message and responds based on their role.
#   All messages are logged so you can see the full conversation.
#

import random
import time
from datetime import datetime


# ──────────────────────────────────────────────────────────
# STEP 1: CREATE THE AGENT CLASS
#
# A "class" is like a blueprint.
# Every agent we create will be built from this blueprint.
# Each agent has:
#   - A name (e.g. "Ebube")
#   - A role (e.g. "Manager")
#   - An inbox to store received messages
#   - A log of all messages it has sent
# ──────────────────────────────────────────────────────────

class Agent:

    def __init__(self, name, role):
        # Store the agent's basic details
        self.name   = name
        self.role   = role
        self.inbox  = []   # Messages this agent has received
        self.outbox = []   # Messages this agent has sent

    def send_message(self, receiver, subject, content):
        """
        This function lets an agent send a message to another agent.
        It creates a message dictionary and delivers it to the receiver's inbox.
        """

        # Build the message as a dictionary (like a sealed envelope)
        message = {
            'from':      self.name,
            'from_role': self.role,
            'to':        receiver.name,
            'to_role':   receiver.role,
            'subject':   subject,
            'content':   content,
            'time':      datetime.now().strftime('%H:%M:%S'),
            'read':      False
        }

        # Put the message in the receiver's inbox
        receiver.inbox.append(message)

        # Keep a copy in the sender's outbox
        self.outbox.append(message)

        print(f"  [{message['time']}] 📨  {self.name} ({self.role})  →  {receiver.name} ({receiver.role})")
        print(f"           Subject : {subject}")
        print(f"           Message : {content}")
        print()

    def read_messages(self):
        """
        This function makes the agent read all unread messages
        and automatically generate a response based on their role.
        """

        # Find messages that haven't been read yet
        unread = [msg for msg in self.inbox if not msg['read']]

        if not unread:
            print(f"  {self.name} has no new messages.\n")
            return

        print(f"  📬  {self.name} ({self.role}) is reading {len(unread)} new message(s)...\n")

        for message in unread:
            # Mark message as read
            message['read'] = True

            print(f"  ┌─ From    : {message['from']} ({message['from_role']})")
            print(f"  │  Subject : {message['subject']}")
            print(f"  │  Content : {message['content']}")

            # Generate a reply based on this agent's role
            reply = self.generate_reply(message)
            print(f"  └─ Reply   : {reply}\n")

    def generate_reply(self, message):
        """
        Each agent replies differently depending on their role.
        This is what makes each agent unique and intelligent.
        """

        # Manager replies
        if self.role == 'Manager':
            manager_replies = [
                f"Thank you for the update, {message['from']}. I will review this and get back to you.",
                f"Noted, {message['from']}. Please ensure this is completed by end of day.",
                f"Good work, {message['from']}. I will escalate this to the board if necessary.",
                f"Understood. I will schedule a meeting to discuss this further.",
                f"This has been acknowledged. Please proceed as planned and report back."
            ]
            return random.choice(manager_replies)

        # Worker replies
        elif self.role == 'Worker':
            worker_replies = [
                f"Understood, {message['from']}. I will get started on this right away.",
                f"Thank you for letting me know. I will complete this task as soon as possible.",
                f"Received. I have a few questions — can we discuss this briefly?",
                f"Got it! I will keep you updated on my progress.",
                f"Message received. I will handle this and report back once done."
            ]
            return random.choice(worker_replies)

        # HR replies
        elif self.role == 'HR':
            hr_replies = [
                f"Thank you, {message['from']}. I will check our policy and respond formally.",
                f"This has been logged in our HR system. We will follow up within 24 hours.",
                f"Noted. Please fill out the necessary forms and submit them to HR.",
                f"Your concern has been received. HR will investigate and respond accordingly.",
                f"Thank you for reaching out. This will be handled with full confidentiality."
            ]
            return random.choice(hr_replies)

        else:
            return "Message received. Thank you."

    def show_summary(self):
        """Show a summary of all messages sent and received by this agent."""
        print(f"  Agent   : {self.name} ({self.role})")
        print(f"  Sent    : {len(self.outbox)} message(s)")
        print(f"  Received: {len(self.inbox)} message(s)")
        print()


# ──────────────────────────────────────────────────────────
# STEP 2: CREATE THE MESSAGE LOG
#
# This keeps a record of every message sent in the simulation.
# It's like a company email server that records everything.
# ──────────────────────────────────────────────────────────

class MessageLog:

    def __init__(self):
        self.all_messages = []

    def record(self, sender, receiver, subject, content):
        """Record a message in the central log."""
        entry = {
            'sender':   f"{sender.name} ({sender.role})",
            'receiver': f"{receiver.name} ({receiver.role})",
            'subject':  subject,
            'content':  content,
            'time':     datetime.now().strftime('%H:%M:%S')
        }
        self.all_messages.append(entry)

    def display_log(self):
        """Print out all recorded messages."""
        print("=" * 60)
        print("         FULL MESSAGE LOG")
        print("=" * 60)
        for i, entry in enumerate(self.all_messages, start=1):
            print(f"  {i}. [{entry['time']}] {entry['sender']}  →  {entry['receiver']}")
            print(f"     Subject : {entry['subject']}")
            print(f"     Content : {entry['content']}")
            print()


# ──────────────────────────────────────────────────────────
# STEP 3: CREATE THE WORKPLACE (THE ENVIRONMENT)
#
# The workplace holds all agents and manages the simulation.
# Think of it as the office building where everything happens.
# ──────────────────────────────────────────────────────────

class Workplace:

    def __init__(self, company_name):
        self.company_name = company_name
        self.agents       = {}
        self.log          = MessageLog()

    def hire_agent(self, name, role):
        """Add a new agent to the workplace."""
        new_agent = Agent(name, role)
        self.agents[name] = new_agent
        print(f"  ✅  {name} has joined as {role}")
        return new_agent

    def send(self, sender_name, receiver_name, subject, content):
        """
        Send a message from one agent to another.
        Also records the message in the central log.
        """
        sender   = self.agents[sender_name]
        receiver = self.agents[receiver_name]
        sender.send_message(receiver, subject, content)
        self.log.record(sender, receiver, subject, content)

    def all_agents_read_messages(self):
        """Make every agent in the workplace read their messages."""
        print("=" * 60)
        print("         AGENTS READING THEIR MESSAGES")
        print("=" * 60)
        for agent in self.agents.values():
            agent.read_messages()

    def show_all_summaries(self):
        """Show a summary for every agent."""
        print("=" * 60)
        print("         AGENT ACTIVITY SUMMARY")
        print("=" * 60)
        for agent in self.agents.values():
            agent.show_summary()


# ──────────────────────────────────────────────────────────
# STEP 4: RUN THE SIMULATION
# ──────────────────────────────────────────────────────────

print("=" * 60)
print("     AGENT MESSAGE SIMULATION SYSTEM")
print("     Workplace: TechCorp Nigeria Ltd.")
print("=" * 60)
print()

# Create the workplace
office = Workplace("TechCorp Nigeria Ltd.")

# Hire the agents (create all the characters)
print("── Hiring Agents ──────────────────────────────────────")
manager = office.hire_agent("Ebube",  "Manager")
worker1 = office.hire_agent("Jude",   "Worker")
worker2 = office.hire_agent("Emma",   "Worker")
hr      = office.hire_agent("Adaeze", "HR")
worker3 = office.hire_agent("Chikum", "Worker")
print()

# ── ROUND 1: Manager sends tasks to workers ──
print("=" * 60)
print("         ROUND 1: MANAGER ASSIGNS TASKS")
print("=" * 60)
office.send("Ebube", "Jude",
    subject = "New Project Assignment",
    content = "Jude, please begin work on the client database module. Deadline is Friday."
)

office.send("Ebube", "Emma",
    subject = "Report Submission",
    content = "Emma, I need the Q3 progress report submitted by 3pm today."
)

office.send("Ebube", "Chikum",
    subject = "Team Meeting",
    content = "Chikum, please prepare a presentation for the team meeting on Thursday."
)

# ── ROUND 2: Worker raises a complaint to HR ──
print("=" * 60)
print("         ROUND 2: WORKER CONTACTS HR")
print("=" * 60)
office.send("Jude", "Adaeze",
    subject = "Leave Application",
    content = "Hi Adaeze, I would like to apply for 3 days annual leave next week. Please advise."
)

office.send("Emma", "Adaeze",
    subject = "Salary Enquiry",
    content = "Good morning Adaeze. I noticed a discrepancy in this month's salary. Can you look into it?"
)

# ── ROUND 3: HR reports back to Manager ──
print("=" * 60)
print("         ROUND 3: HR REPORTS TO MANAGER")
print("=" * 60)
office.send("Adaeze", "Ebube",
    subject = "Leave Request — Jude",
    content = "Hello Ebube, Jude has applied for leave. Kindly approve or decline at your earliest convenience."
)

office.send("Adaeze", "Ebube",
    subject = "Payroll Issue — Emma",
    content = "There was a system error in this month's payroll. Emma's case has been flagged for correction."
)

# ── ROUND 4: All agents read their messages and reply ──
office.all_agents_read_messages()

# ── ROUND 5: Full message log ──
office.log.display_log()

# ── ROUND 6: Activity summary ──
office.show_all_summaries()

print("=" * 60)
print("         SIMULATION COMPLETE")
print("=" * 60)
