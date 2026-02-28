function showUploadSection() {
    document.getElementById('home-section').style.display = 'none';
    document.getElementById('upload-section').style.display = 'block';
}

function showHomeSection() {
    document.getElementById('upload-section').style.display = 'none';
    document.getElementById('home-section').style.display = 'block';
}

function d() {
    //Async Function을 사용하여 내용들을 보내고 그걸 서버측으로 전달
}

async function submitData() {
    document.getElementById('cv-text').value
    const response = await fetch('/upload', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json' 
    },
    body: JSON.stringify({ name: '새 아이템', price: 1000 })
}); 
  const result = await response.json();
  console.log(result.message);


    // 일단 File submit은 보류 document.getElementById(cv-file).value
}
