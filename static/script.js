function showUploadSection() {
    document.getElementById('home-section').style.display = 'none';
    document.getElementById('upload-section').style.display = 'block';
}

function showHomeSection() {
    document.getElementById('upload-section').style.display = 'none';
    document.getElementById('home-section').style.display = 'block';
}


async function submitUserUserInput() {

    const formData = new FormData();
    const fileInput = document.getElementById('cv-file');
    const file = fileInput.files[0];
    if (!file) {
        alert('please select a file to upload');
        return;
    }
    const userText = document.getElementById('cv-text').value;
    formData.append('file', file);
    formData.append('text', userText);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    console.log(result.message);
    
}
/*
async function submitUserTextInput() {
    const userText = document.getElementById('cv-text').value;
    const response = await fetch('/upload', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json' 
    },
    body: JSON.stringify(userText)
}); 
  const result = await response.json();
  console.log(result.message);
}
*/
