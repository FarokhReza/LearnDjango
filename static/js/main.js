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