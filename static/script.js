async function check() {
    const url = document.getElementById('urlIn').value;
    const out = document.getElementById('out');
    
    const response = await fetch('/classify-url/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ url: url })
    });
    
    const data = await response.json();
    out.innerText = "Classification: " + data.classification;
    out.className = data.classification === "SAFE" ? "safe-box" : "danger-box";
}