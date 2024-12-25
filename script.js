// Pre-loaded links with title, description, and URL
const links = [
    { title: "Website Source Code", description: "Download The Source Code for this website", url: "https://mega.nz/folder/vZcFFQ5b#fXTpjT9Huic_O6C8Hf-Cjw" },
    { title: "Multi-Use App (Under Development)", description: "Download the Multi-use app (Current functions: Calculator, rock paper scissors, and many easter eggs and debugging options use code \"69\" for a easter egg)", url: "https://mega.nz/file/PV12UAhb#xncaNvaAOK4PxLZPXRuz31s7qGsuWovlox5enoM32rI" },
    { title: "Efficient Multi use app (Chatgpt)", description: "A Reference File for How to write streamlined code", url: "https://mega.nz/file/3QdASJzC#JDFhVP1df-Re5-4SrboAOh2u3zg78NXqZ9lX4Mjra9U" },
    { title: "Pranx", description: "Fun Site For Pranking People or passing time", url: "https://pranx.com/" },
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
