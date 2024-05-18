const puppeteer = require('puppeteer');

async function getFacebookUid(profileUrl) {
    // เปิดเบราว์เซอร์และเปิดแท็บใหม่
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();

    try {
        // ไปที่ URL ของโปรไฟล์
        await page.goto(profileUrl, { waitUntil: 'networkidle2' });

        // ดึงข้อมูล HTML ของหน้าเว็บ
        const pageContent = await page.content();

        // หา UID จาก HTML ด้วยการใช้ regex
        const uidMatch = pageContent.match(/fb:\/\/profile\/(\d+)/);
        if (uidMatch) {
            return uidMatch[1];
        }

        // ลองค้นหาด้วย regex อื่นๆ
        const alternativeUidMatch = pageContent.match(/"userID":"(\d+)"/);
        if (alternativeUidMatch) {
            return alternativeUidMatch[1];
        }

        // ถ้าไม่พบ UID
        return null;
    } catch (error) {
        console.error(`Error fetching the profile page: ${error.message}`);
        return null;
    } finally {
        // ปิดเบราว์เซอร์
        await browser.close();
    }
}

// ตัวอย่างการใช้งาน
const profileUrl = 'https://www.facebook.com/pakpaphon.jaiwangloke.3';  // เปลี่ยน URL เป็น URL ของโปรไฟล์ที่ต้องการ

getFacebookUid(profileUrl)
    .then(uid => {
        if (uid) {
            console.log(`UID: ${uid}`);
        } else {
            console.log('ไม่พบ UID');
        }
    });
