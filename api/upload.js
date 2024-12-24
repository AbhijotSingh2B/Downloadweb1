import fs from 'fs';
import path from 'path';

export default async function handler(req, res) {
    if (req.method === 'POST') {
        try {
            const chunks = [];
            req.on('data', chunk => chunks.push(chunk));
            req.on('end', () => {
                const boundary = req.headers['content-type'].split('boundary=')[1];
                const buffer = Buffer.concat(chunks);
                const parts = buffer.toString().split(`--${boundary}`);

                const contentDisposition = parts[1].split('\r\n')[1];
                const fileName = contentDisposition.match(/filename="(.+?)"/)[1];
                const fileData = parts[1].split('\r\n\r\n')[1].split('\r\n--')[0];

                const uploadDir = path.join(process.cwd(), 'public/uploads');
                if (!fs.existsSync(uploadDir)) {
                    fs.mkdirSync(uploadDir, { recursive: true });
                }

                const filePath = path.join(uploadDir, fileName);
                fs.writeFileSync(filePath, fileData, { encoding: 'binary' });

                res.status(200).json({ filePath: `/uploads/${fileName}` });
            });
        } catch (error) {
            res.status(500).json({ error: 'File upload failed' });
        }
    } else {
        res.status(405).json({ error: 'Method not allowed' });
    }
}
