import os
import openai

openai.api_key = "sk-"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt='''
  Here are some characteristics that may be applicable for a manager and leader:

Communication skills: A manager and leader should be able to effectively communicate with their team, other stakeholders, and superiors. This includes being able to clearly convey expectations, provide feedback, and listen to others.

Decision-making abilities: A manager and leader should be able to make sound decisions in a timely manner, weighing the pros and cons of different options and considering the impact on the team and organization.

Strategic thinking: A manager and leader should be able to think strategically and plan for the long-term success of the team and organization. This includes setting goals, developing a vision, and creating a plan to achieve those goals.

Adaptability: A manager and leader should be able to adapt to changing circumstances and be flexible in their approach to problem-solving.

Emotional intelligence: A manager and leader should have a high level of emotional intelligence, which includes the ability to understand and manage their own emotions, as well as the emotions of others.

Leadership: A manager and leader should be able to inspire and motivate their team, and provide direction and guidance to help team members achieve their full potential.

Collaboration: A manager and leader should be able to work effectively with others, including team members, other departments, and external stakeholders, to achieve shared goals.

Integrity: A manager and leader should be honest, transparent, and fair in their interactions with others.

Problem-solving: A manager and leader should be able to identify and address problems in a proactive and effective manner.

Strategic planning: A manager and leader should be able to develop and implement a long-term plan for the success of the team and organization.
  ''',
  temperature=0.7,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response.choices[0].text)