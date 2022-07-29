const enterButton = document.getElementById('enterButton');
const errorMsg = document.getElementById('errorMsg');

// Functions that check if the form boxes are valid
function validName(name){
    return name.length !== 0;
}
function validEmail(email) {
    return email.match(/\S+@\S+\.\S+/);
};
function validContent(content){
    return content.length !== 0;
}

// Handling errors
function createErrorMsg(msg){
    if(errorMsg.innerHTML.length === 0){
        errorMsg.innerHTML = "Error(s): " + msg;
    } else {
        errorMsg.innerHTML += " " + msg;
    }
}
function clearErrorMsg(){
    errorMsg.innerHTML = "";
}

/**
 * Retrieves all post data from the database using a GET request, and updates the 
 * main table with that data. Each row is a seperate post.
 */
async function GET_timeline_posts() {
    await fetch("/api/timeline_post")
    .then(response => response.json()) // converting response data to JSON
    .then(json => {
        let table_content = '<tr><th>Name</th><th>Email</th><th>Created At</th><th>Content</th></tr>';
        const timeline_posts = json["timeline_posts"];

        // Loop through each post and adding a row to the table
        timeline_posts.forEach(post => {
            table_content += `<tr>
                <td>${post.name} </td>
                <td>${post.email}</td>
                <td>${post.created_at}</td>
                <td>${post.content}</td>        
            </tr>`;
        });

        document.getElementById("mainTable").innerHTML = table_content; // update the main table
    });
}

/**
 * Saves the current form to the database via a POST request.
 */
async function POST_timeline_posts(name, email, content) {
    await fetch("/api/timeline_post", {
        method: "POST",
        headers:{
            'Content-Type': 'application/x-www-form-urlencoded'
        },    
        body: new URLSearchParams({
            'name': name,
            'email': email,
            'content': content
        })
    }).then( res => {
          if(res.status == 429) {
              createErrorMsg("No post spamming. Please wait 1 minute to produce another post.")
          }
        }
    );
}

/**
 * Updates the timeline and clears all text on the form
 */
async function enterAction() {
    const nameValue = document.getElementById('nameBox').value;
    const emailValue = document.getElementById('emailBox').value;
    const contentValue = document.getElementById('contentBox').value;
    const allValues = [nameValue, emailValue, contentValue];

    clearErrorMsg();
    let valid = true;

    if(!validName(nameValue)){
        createErrorMsg("Name cannot be empty.");
        valid = false;
    }
    if(!validEmail(emailValue)){
        createErrorMsg("Email has an invalid format.");
        valid = false;
    }
    if(!validContent(contentValue)) {
        createErrorMsg("Content cannot be empty.");
        valid = false;
    }

    if(valid){
        await POST_timeline_posts(nameValue, emailValue, contentValue);
        await GET_timeline_posts();

        allValues.map(function(e){e="";});
    }
}

async function main() {
    await GET_timeline_posts(); // In order for the page to initially show the timeline upon being opened for the first time, this is needed

    enterButton.addEventListener('click', (Event) => enterAction());
}

void main();