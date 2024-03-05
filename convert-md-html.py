import markdown
import os

with open('AWS-DX-RTP-LAB.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open('AWS-DX-RTP-LAB.md', 'w') as f:
    f.write(html)
    f.close()

    