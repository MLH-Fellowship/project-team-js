// Objects of all the form boxes and the enter button
const nameBox = document.getElementById('nameBox');
const emailBox = document.getElementById('emailBox');
const contentBox = document.getElementById('contentBox');
const enterButton = document.getElementById('enterButton');
const allBoxes = [nameBox, emailBox, contentBox];

/** 
 * Consists of sending a POST request and a GET request to the main database 
 */
async function update_timeline() {
    await POST_timeline_posts();
    await GET_timeline_posts();
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
async function POST_timeline_posts() {
    await fetch("/api/timeline_post", {
        method: "POST",
        headers:{
            'Content-Type': 'application/x-www-form-urlencoded'
        },    
        body: new URLSearchParams({
            'name': nameBox.value,
            'email': emailBox.value,
            'content': contentBox.value
        })
    });
}

/**
 * Updates the timeline and clears all text on the form
 */
async function enterAction() {    
    await update_timeline();
    allBoxes.map(function(e){e.value= "";});
}

async function main() {
    await GET_timeline_posts(); // In order for the page to initially show the timeline upon being opened for the first time, this is needed

    enterButton.addEventListener('click', (Event) => enterAction());
}

void main();