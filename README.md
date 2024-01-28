# CodeMap AI
Have you ever struggled to understand the codebase for a project? Too many files to go through and digest? CodeMap AI tackles this very issue by streamlining file connections for rapid comprehension!
## Access code:
Download and use our project package at: https://pypi.org/project/codemapai/

See our demo at: https://devpost.com/software/codemap-ai
## Inspiration
Onboarding at a new company with a complex codebase can be very daunting, and the sheer number of files in a project can be too much to digest in a reasonable timeframe. This can lead to time being wasted or inefficiently utilized on simply trying to catch up with what has been done by former and existing developers, rather than being able to contribute meaningful work immediately. Eliminating this major time commitment in the early stages can greatly enhance new-member productivity in anywhere from academia to the workforce.
## What it does
CodeMap AI is a powerful visualization developer tool designed to instantaneously improve the productivity of developers by allowing them to skip the tedious process of reading code documentation and attempting to comprehend file connections, component relationships, dependencies, etc. By simply providing a target directory with an easy-to-use command line argument, CodeMap AI will rapidly generate a visual ASCII diagram that draws connections between file dependencies and relations in the **File Diagram** mode, as well as high-level, broader contextualization diagrams in the **System Diagram** mode. These diagrams are printed directly to the terminal for developer convenience and ease of use, able to be regenerated at any time. The developer would be able to ask CodeMap AI any questions about the project. Additionally, the diagrams will be accompanied by a part-by-part breakdown of major system components as well as an overarching summary regarding the interplay between files as well as their functionalities.
## How we built it
CodeMap AI was created through the use of a variety of Python libraries such as os, sys, and time to efficiently iterate through user-specified directories as well as to filter out undesired files to produce the diagrams. Upon creating an aggregated list of all files that are desired in the diagram, the data is then forwarded to OpenAI’s GPT-4 LLM, which then generates detailed yet concise visual ASCII diagrams, component breakdowns, and code component summaries. The generation of ASCII diagrams and summaries was able to be achieved through strategic prompt engineering. CodeMap AI is neatly compiled on a PyPi Python package for convenient local use and terminal integration for all developers to utilize.
## Challenges we ran into
Prompt engineering was a major challenge. It was difficult to ensure that the prompts were specific and robust enough to produce diagrams that would provide meaningful assistance to developers. Another main challenge was integrating our file content reading functionality with our AI’s prompt reception; namely the ability of our AI to interpret the file content and turn them into diagrams (ties back to our prompt engineering difficulties as well). 
## Accomplishments that we're proud of
CodeMap AI can efficiently produce very easy-to-understand and concise diagrams that would help developers with a major pitfall in the onboarding process. We are particularly proud of having created effective prompts that essentially allow our AI to generate these practical diagrams as well as the fact that this is a tool we intend to use ourselves.
## What we learned
The process of creating CodeMap AI greatly enhanced our understanding of the capabilities of generative AI. We have garnered a greater appreciation for the boundless potential of generative AI in enhancing the efficiency of developers, eliminating the need to engage in time-consuming, mundane tasks. It is also the first Python package that all members of the team have ever created and released publicly.
## What's next for CodeMap AI
Our next step is to integrate CodeMap AI with Visual Studio Code as an extension to allow for even greater ease of access. We would also like to make CodeMap AI scalable through distributed systems, allowing for the generation of larger-scale diagrams on larger codebases. 

**Created at SpartaHack 9**
