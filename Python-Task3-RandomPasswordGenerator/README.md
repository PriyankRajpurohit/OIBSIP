# Task 3 — Random Password Generator

A beginner-friendly Python command-line program that generates a password using the requested length and character types.

## Requirements

- Python 3.10 or newer
- No third-party packages

## Run

From this folder, run:

    python main.py

On Windows, use py main.py if the python command is unavailable. Choose a length of at least 8, then select at least two character types. Answer y to generate another password without restarting.

## Security notes

- The program uses Python's secrets module for cryptographically strong random choices.
- It guarantees at least one character from every selected type, then shuffles the result.
- Generated passwords are displayed in the terminal only. The program does not save them to a file or clipboard.
- Never publish a real generated password in a screenshot, video, README, or output file. Shared evidence must redact the password value.

## Learning notes

- CHARACTER_GROUPS defines the available character sets.
- read_password_length validates the minimum length.
- choose_character_groups enforces the two-type minimum.
- generate_password ensures every selected type appears and uses secrets to choose and shuffle characters.
- main connects the prompts and repeat option.

## Evidence

evidence/run_output.txt contains a real sample run with the generated password redacted before publication. Keep real generated passwords out of public screenshots, videos, and repository files.

This is the Beginner-tier command-line version. It does not retain generated passwords or provide account-security advice.
