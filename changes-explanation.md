# Explanation of Changes

I've implemented changes to make the image in the main container bigger:

1. Created a new custom CSS file (`/static/css/custom.css`) with rules to increase the image size:
   - Set `max-width` to 130% to allow the image to be larger than its container
   - Applied a `transform: scale(1.3)` to make the image 30% bigger
   - Added responsive design for smaller screens to prevent overflow issues

2. Linked the custom CSS file in the header template (`header.html`) so it's loaded on all pages

These changes will make the image in the main container approximately 30% bigger than before, while maintaining responsiveness on smaller screens. The image will scale back to normal size on mobile devices to prevent layout issues.

You can adjust the scaling factor (1.3) in the custom CSS file if you want the image to be even larger or slightly smaller.