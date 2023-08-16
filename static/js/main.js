console.log("Hello world");

// GET SEARCH FORM AND PAGE LINKS
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

// ENSURE SEARCH FOR IS EXIST

if (searchForm) {
  for (let i = 0; i < pageLinks; i++){
    pageLinks[i].addEventListener('click', function (e) {
      e.preventDefault()
      
      // GET THE DATA ATTRIBUTE

      let page = this.dataset.page
      // console.log('PAGE: ', page)

      // ADD HIDDEN SEARCH INPUT TO FORM
      searchForm.innerHTML += `<input value=${page} name="page" hidden/>`
      

      // SUBMIT FORM
      searchForm.submit()
    })
  }
}



// let tags = document.getElementsByClassName('project-tag')

//     for (let i = 0;i < tags.length; i++) {
//         tags[i].addEventListener('click', (e)=>{
//             let tagId = e.target.dataset.tag
//             let projectId = e.target.dataset.project

//             // console.log(tagId, projectId)

//             fetch('http://127.0.0.1:8000/api/remove-tag/', {
//                 method: 'DELETE',
//                 headers: {
//                     'Content-Type': 'application/json'
//                 },
//                 body: JSON.stringify({'project': projectId, 'tag': tagId})
//             })
//             .then(response => response.json())
//             .then(data => {
//                 e.target.remove()
//             })
//         })
//     }

let tags = document.getElementsByClassName('project-tag')

for (let i = 0; i < tags.length; i++) {
    tags[i].addEventListener('click', (e) => {
        let tagId = e.target.dataset.tag
        let projectId = e.target.dataset.project

        fetch('http://127.0.0.1:8000/api/remove-tag/', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'project': projectId, 'tag': tagId })
        })
        .then(response => response.json())
        .then(data => {
            e.target.remove()
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
}
 