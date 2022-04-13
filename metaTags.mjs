 
export function init(title, description, previewImageUrl, w, h) {

    const text = `
    <meta property="og:type" content="website" />
    <meta property="og:title" content="${title}" />
    <meta property="og:locale" content="en_GB" />
    <meta property="og:description" content="${description}" />
    <meta property="og:image:alt" content="${description}" />
    <meta property="og:image" content="${previewImageUrl}" />
    <meta property="og:image:width" content="${w}" />
    <meta property="og:image:height" content="${h}" />
    `;
    document.head.innerHTML += text
}
