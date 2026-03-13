import re

with open('notary-showcase/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the sticky nav
content = re.sub(r'\s*<!-- Sticky Sub-Navigation -->\s*<nav class="sticky-subnav.*?</nav>', '', content, flags=re.DOTALL)

# Remove Option 2, Option 3, and their booking forms
content = re.sub(r'\s*<!-- Option 2: The Classic Heritage -->.*?</main>', '\n    </main>', content, flags=re.DOTALL)

# Remove the script block completely (animations for removed options / unused parallax)
content = re.sub(r'\s*<script>.*?</script>', '', content, flags=re.DOTALL)

with open('notary-showcase/index.html', 'w', encoding='utf-8') as f:
    f.write(content)