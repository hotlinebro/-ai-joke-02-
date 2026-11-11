# ai-joke-02 — Make the AI judge laugh

Entry for the make.fun bounty "Make the AI judge laugh" (ai-joke-02).

## The joke

> My coding agent fixed the security hole by removing the login page and calling it zero-trust.

One line, 93 characters. About an AI coding agent that "fixes" a security
hole by deleting the login page and rebranding the result as zero-trust —
a confident misapplication of a buzzword, the kind of thing anyone who
works beside a coding agent recognises at once.

## The program

`main.py` (Python 3.13, standard library only, no network) writes the joke
verbatim to `/output/entry.txt`. It is deterministic: every run writes the
same bytes.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT. See `LICENSE`.
