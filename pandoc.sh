#!/bin/bash

# Source Markdown file
SOURCE="SOURCE.md"

# Destination HTML file
DESTINATION="HTML.html"

# CSS file
CSS="style.css"

# Begin of style tag
echo '<style>' > temp_style.css

# Append CSS content
cat "$CSS" >> temp_style.css

# End of style tag
echo '</style>' >> temp_style.css

# Use Pandoc to generate HTML with embedded CSS
pandoc "$SOURCE" -s --metadata title="Your Document Title" -H temp_style.css -o "$DESTINATION"

# Cleanup temporary CSS file
rm temp_style.css


# Alternatively, just run this command: 
# pandoc SOURCE.md -s -o HTML.html -c style.css