document.addEventListener('DOMContentLoaded', () => {
    const imageInput = document.getElementById('imageInput');
    const analyzeButton = document.getElementById('analyzeButton');
    const imagePreview = document.getElementById('imagePreview');
    const previewContainer = document.getElementById('previewContainer');
    const resultsContainer = document.getElementById('resultsContainer');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const titleResult = document.getElementById('titleResult');
    const descriptionResult = document.getElementById('descriptionResult');
    const tagsResult = document.getElementById('tagsResult');

    // Handle image selection
    imageInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.src = e.target.result;
                previewContainer.style.display = 'block';
                analyzeButton.disabled = false;
            };
            reader.readAsDataURL(file);
        }
    });

    // Handle analyze button click
    analyzeButton.addEventListener('click', async () => {
        const file = imageInput.files[0];
        if (!file) return;

        // Show loading indicator
        loadingIndicator.style.display = 'block';
        resultsContainer.style.display = 'none';

        // Create form data
        const formData = new FormData();
        formData.append('file', file);

        try {
            // Send request to backend
            const response = await fetch('/analyze-image', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('Failed to analyze image');
            }

            const data = await response.json();

            // Display results
            titleResult.textContent = data.title;
            descriptionResult.textContent = data.description;
            
            // Clear and add tags
            tagsResult.innerHTML = '';
            data.tags.forEach(tag => {
                const tagElement = document.createElement('span');
                tagElement.className = 'tag';
                tagElement.textContent = tag;
                tagsResult.appendChild(tagElement);
            });

            // Show results
            resultsContainer.style.display = 'grid';
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to analyze image. Please try again.');
        } finally {
            // Hide loading indicator
            loadingIndicator.style.display = 'none';
        }
    });
}); 