function filterFunction() {
    let isInputAvail = false;
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toLowerCase();
    if (filter.length > 0) {
        document.getElementById("myDropdown").classList.add("show");
    } else {
        document.getElementById("myDropdown").classList.remove("show");
    }
    div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        txtValue = a[i].innerText;
        if (txtValue.toLowerCase().indexOf(filter) > -1) {
            isInputAvail = true;
            a[i].style.display = "block";
        } else {
            a[i].style.display = "none";
        }
    }
    if (!isInputAvail) {
        document.getElementById("noMatches").classList.add('show');
    } else {
        document.getElementById("noMatches").classList.remove('show');
    }
}
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

const searchBox = document.querySelector(".search-box");
const searchBtn = document.querySelector(".search-icon");
const cancelBtn = document.querySelector(".cancel-icon");
const searchInput = document.querySelector("input");
const searchData = document.querySelector(".search-data");
const mydropdown = document.querySelector(".dropdown-content");
searchBtn.onclick = () => {
    searchBox.classList.add("active");
    searchBtn.classList.add("active");
    searchInput.classList.add("active");
    cancelBtn.classList.add("active");
    searchInput.focus();
    if (searchInput.value !== "") {
        var values = searchInput.value;
        searchData.classList.remove("active");
        searchData.innerHTML = "You just typed " + "<span style='font-weight: 500;'>" + values + "</span>";
    } else {
        searchData.textContent = "";
    }
}
cancelBtn.onclick = () => {
    searchBox.classList.remove("active");
    searchBtn.classList.remove("active");
    searchInput.classList.remove("active");
    cancelBtn.classList.remove("active");
    mydropdown.classList.remove("active");
    searchData.classList.toggle("active");
    searchInput.value = "";

}