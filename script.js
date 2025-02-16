document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('text');
    const questionInput = document.getElementById('question');
    const askButton = document.getElementById('askButton');
    const answerBox = document.getElementById('answer');

    askButton.addEventListener('click', askQuestion);

    async function askQuestion() {
        const text = textInput.value.trim();
        const question = questionInput.value.trim();

        if (!text || !question) {
            answerBox.textContent = 'Please enter both text/URL and a question.';
            return;
        }

        answerBox.textContent = 'Thinking...';
        askButton.disabled = true;

        try {
            const response = await fetch(`http://localhost:8000/ask-question/?url=${encodeURIComponent(text)}&question=${encodeURIComponent(question)}`);
            const data = await response.json();
            
            if (data.status === 'success') {
                answerBox.textContent = data.answer;
            } else {
                answerBox.textContent = 'Error: ' + data.message;
            }
        } catch (error) {
            answerBox.textContent = 'An error occurred while fetching the answer.';
            console.error('Error:', error);
        } finally {
            askButton.disabled = false;
        }
    }
});
