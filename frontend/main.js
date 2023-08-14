// let loginBtn = document.getElementById('login-btn')
// let logoutBtn = document.getElementById('logout-btn')

// let token = localStorage.getItem('token')

// if (token) {
//     loginBtn.remove()
// } 
// else {
//     logoutBtn.remove()
// }

// loginBtn.addEventListener('click', (e) => {
//     e.preventDefault()
//     localStorage.removeItem('token')
//     window.location = 'file:///home/reza/Desktop/django/frontend/login.html'
// })

let projectsUrl = 'http://127.0.0.1:8000/api/projects/'
let getProjects = () => {
    // token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxOTI0MDcwLCJpYXQiOjE2OTE4Mzc2NzAsImp0aSI6ImM4NGRhNTI3YmYwNDRiMjE4ZDQ1ZDg1ZmI4ZWZmN2IyIiwidXNlcl9pZCI6MX0.nKTegWnLysQPJkuveY3wb27QHE94nCLLPk3FS1hn9jw'
    let token = localStorage.getItem('token')
    fetch(projectsUrl, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        buildProjects(data)
    })
}


let buildProjects = (projects) => {

    let projectsWrapper = document.getElementById('projects--wrapper')
    projectsWrapper.innerHTML = ''
    // console.log('projectsWrapper:', projectsWrapper)


    for (let i = 0;projects.length > i; i++) {
        let project = projects[i]
        // console.log(project)
        let projectCard = `
            <div class="project--card" >
                <img src="http://127.0.0.1:8000${project.featured_image}" />
                <div>
                    <div class="card--header">
                        <h3>${project.title}</h3>
                        <strong class="vote--option" data-vote="up" data-project="${project.id}" >&#43;</strong>
                        <strong class="vote--option" data-vote="down" data-project="${project.id}" >&#8722;</strong>
                    </div>
                    <i>${project.vote_ratio}% Positive feedback</i>
                    <p>${project.description.substring(0, 150)}</p>
                </div>
            </div>
        `

        projectsWrapper.innerHTML += projectCard
    }

    // add an listener

    addVoteEvents()
    
}

let addVoteEvents = () => {
    let voteBtns = document.getElementsByClassName('vote--option')
    console.log('Vote buttons: ', voteBtns)

    for (let i = 0; voteBtns.length > i;i++) {

        voteBtns[i].addEventListener('click', (e)=> {
            // token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxOTI0MDcwLCJpYXQiOjE2OTE4Mzc2NzAsImp0aSI6ImM4NGRhNTI3YmYwNDRiMjE4ZDQ1ZDg1ZmI4ZWZmN2IyIiwidXNlcl9pZCI6MX0.nKTegWnLysQPJkuveY3wb27QHE94nCLLPk3FS1hn9jw'
            token = localStorage.getItem('token')
            let vote = e.target.dataset.vote
            let project = e.target.dataset.project
            console.log('PROJECT:', project, 'VOTE: ', vote)

            fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {
                method: 'POST', 
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`
                },
                body:JSON.stringify({'value': vote})

            })
            .then(response => response.json())
            .then(data => {
                console.log('SUCCESS: ', data)
                getProjects()
            })

        })
    }
}


getProjects()