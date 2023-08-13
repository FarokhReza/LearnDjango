let form = document.getElementById('login-form')

form.addEventListener('submit', (e) => {
    e.preventDefault() // if this line dose not exist it refresh after submit
    // console.log('Form was submited')

    let formData = {
        'username':form.username.value,
        'password':form.password.value
    }

    // console.log('Form Data', formData)

    fetch('http://127.0.0.1:8000/api/users/token/' , {
        method:'POST',
        headers: {
            'Content-Type': 'application/json', 
            
        },
        body:JSON.stringify(formData)
    })
    // console.log('DATA:', data)
        .then(response => response.json())
        .then(data => {
            console.log('DATA:', data.access)
            if (data.access) {
                localStorage.setItem('token', data.access)
                window.location = 'file:///home/reza/Desktop/django/frontend/projects-list.html'
            } else {
                alert('Username or password did not work')
            }
        })
})