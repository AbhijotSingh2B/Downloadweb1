// Pre-loaded links with title, description, and URL
const links = [
    { title: "Python Projects", description: "Python Projects that I have made", url: "python-projects.html" },
    { title: "Coding Prerequisites", description: "See some pre-requisites for running python and/or other languages. Click to download or view details.", url: "prerequisites.html" },
    { title: "Pranx", description: "Fun Site For Pranking People or passing time", url: "https://pranx.com/" },
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
