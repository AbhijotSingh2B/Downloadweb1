// Pre-loaded links with title, description, and URL
const links = [
    { title: "Google", description: "Search the web with Google.", url: "https://www.google.com" },
    { title: "GitHub", description: "Browse open-source projects on GitHub.", url: "https://www.github.com" },
    { title: "StackOverflow", description: "Ask questions and find answers on StackOverflow.", url: "https://www.stackoverflow.com" },
    { title: "Python", description: "Official website for Python programming language.", url: "https://www.python.org" },
    { title: "Vercel", description: "Deploy your projects with Vercel.", url: "https://vercel.com" }
];

// Function to render the links on the page
function renderLinks() {
    const container = document.getElementById('links-container');

    links.forEach((link, index) => {
        const linkItem = document.createElement('div');
        linkItem.classList.add('link-item');
        linkItem.style.animationDelay = `${index * 0.3}s`; // Add delay for sequential animation

        linkItem.innerHTML = `
            <h2><a href="${link.url}" target="_blank">${link.title}</a></h2>
            <p>${link.description}</p>
        `;

        container.appendChild(linkItem);
    });
}

// Call the function to render the links
document.addEventListener("DOMContentLoaded", renderLinks);
