# Docker & Docker Compose - Cheat Sheet

## 📋 תוכן עניינים
- [ניהול קונטיינרים](#ניהול-קונטיינרים)
- [רשתות (Networks)](#רשתות-networks)
- [Volumes](#volumes)
- [בדיקה וניטור](#בדיקה-וניטור)
- [Docker Compose - מחזור חיים](#docker-compose---מחזור-חיים)
- [Docker Compose - ניפוי באגים](#docker-compose---ניפוי-באגים)
- [Docker Compose - בנייה ומשיכה](#docker-compose---בנייה-ומשיכה)
- [Docker Compose - ניהול מתקדם](#docker-compose---ניהול-מתקדם)
- [משתני סביבה](#משתני-סביבה)
- [פקודות בתוך קונטיינר](#פקודות-בתוך-קונטיינר)
- [ניקוי ותחזוקה](#ניקוי-ותחזוקה)
- [פקודות מערכת הפעלה](#פקודות-מערכת-הפעלה)

---

## ניהול קונטיינרים

| **פקודה** | **הסבר** |
|-----------|----------|
| `docker run -d --name <n> <image>` | הרצת קונטיינר ברקע עם שם |
| `docker run -d --name <n> --network <net> <image>` | הרצת קונטיינר עם רשת ושם |
| `docker run -it <image> sh` | הרצת קונטיינר אינטראקטיבי עם shell |
| `docker run -d -p <host-port>:<container-port> <image>` | הרצת קונטיינר עם מיפוי פורט |
| `docker run -d -e <VAR>=<value> <image>` | הרצת קונטיינר עם משתנה סביבה |
| `docker ps` | הצגת קונטיינרים רצים |
| `docker ps -a` | הצגת כל הקונטיינרים (כולל עצורים) |
| `docker ps -q` | הצגת רק מזהי הקונטיינרים |
| `docker ps --filter name=<pattern>` | סינון קונטיינרים לפי שם |
| `docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}"` | תצוגה מעוצבת של קונטיינרים |
| `docker start <container-name>` | הפעלת קונטיינר קיים |
| `docker stop <container-name>` | עצירת קונטיינר |
| `docker restart <container-name>` | הפעלה מחדש של קונטיינר |
| `docker rm <container-name>` | מחיקת קונטיינר |
| `docker rm -f <container-name>` | מחיקת קונטיינר בכוח (גם אם רץ) |
| `docker exec -it <container-name> sh` | כניסה אינטראקטיבית לקונטיינר |
| `docker exec <container-name> <command>` | הרצת פקודה בקונטיינר רץ |

---

## רשתות (Networks)

| **פקודה** | **הסבר** |
|-----------|----------|
| `docker network create <network-name>` | יצירת רשת Docker חדשה |
| `docker network ls` | הצגת רשימת כל הרשתות |
| `docker network inspect <network-name>` | הצגת פרטים מלאים על רשת |
| `docker network connect <network-name> <container>` | חיבור קונטיינר קיים לרשת |
| `docker network rm <network-name>` | מחיקת רשת |

---

## Volumes

| **פקודה** | **הסבר** |
|-----------|----------|
| `docker volume ls` | הצגת volumes |
| `docker volume inspect <volume-name>` | הצגת מידע על volume |
| `docker volume rm <volume-name>` | מחיקת volume |

---

## בדיקה וניטור

| **פקודה** | **הסבר** |
|-----------|----------|
| `docker logs <container-name>` | הצגת לוגים של קונטיינר |
| `docker logs --tail <number> <container-name>` | הצגת מספר שורות אחרונות מהלוג |
| `docker logs -f <container-name>` | מעקב אחר לוגים בזמן אמת |
| `docker inspect <container-name>` | הצגת כל המידע על קונטיינר בפורמט JSON |
| `docker events --filter container=<id>` | צפייה באירועי קונטיינר בזמן אמת |
| `docker stats` | הצגת שימוש במשאבים של קונטיינרים |
| `docker top <container-name>` | הצגת תהליכים רצים בקונטיינר |

---

## Docker Compose - מחזור חיים

| **פקודה** | **הסבר** |
|-----------|----------|
| `docker compose up` | הרצת כל השירותים (foreground) |
| `docker compose up -d` | הרצת כל השירותים ברקע |
| `docker compose up --build` | בנייה והרצה של שירותים |
| `docker compose up -d --force-recreate` | יצירה מחדש של קונטיינרים |
| `docker compose up -d --scale <service>=<num>` | הרצה עם מספר instances |
| `docker compose down` | עצירה ומחיקת קונטיינרים ורשתות |
| `docker compose down -v` | עצירה ומחיקה כולל volumes |
| `docker compose start` | הפעלת שירותים קיימים |
| `docker compose stop` | עצירת שירותים רצים |
| `docker compose restart` | הפעלה מחדש של שירותים |
| `docker compose pause` | השהיית שירותים |
| `docker compose unpause` | המשך הרצה של שירותים |

---

## Docker Compose - ניפוי באגים

| **פקודה** | **הסבר** |
|-----------|----------|
| `docker compose ps` | הצגת מצב שירותים בפרויקט |
| `docker compose logs <service>` | הצגת לוגים של שירות |
| `docker compose logs -f` | מעקב אחר לוגים של כל השירותים |
| `docker compose logs --tail <number>` | הצגת מספר שורות אחרונות |
| `docker compose exec <service> <command>` | הרצת פקודה בשירות רץ |
| `docker compose exec <service> sh` | כניסה אינטראקטיבית לשירות |
| `docker compose exec <service> env` | הצגת משתני סביבה של שירות |
| `docker compose config` | הצגת תצורה ממוזגת ומאומתת |
| `docker compose top` | הצגת תהליכים רצים בכל השירותים |

---

## Docker Compose - בנייה ומשיכה

| **פקודה** | **הסבר** |
|-----------|----------|
| `docker compose build` | בנייה של כל ה-images |
| `docker compose build --no-cache` | בנייה ללא שימוש ב-cache |
| `docker compose build <service>` | בנייה של שירות ספציפי |
| `docker compose pull` | משיכת images עבור כל השירותים |

---

## Docker Compose - ניהול מתקדם

| **פקודה** | **הסבר** |
|-----------|----------|
| `docker compose run <service> <command>` | הרצה חד-פעמית של פקודה |
| `docker compose rm -s -v <service>` | מחיקת שירות ספציפי |
| `docker compose -p <project-name> up` | הרצה עם שם פרויקט מפורש |
| `docker compose -p <project-name> ps` | הצגת שירותים בפרויקט ספציפי |
| `docker compose -p <project-name> down` | עצירת פרויקט ספציפי |
| `docker compose -f <file1> -f <file2> up` | שימוש בקבצי Compose מרובים |

---

## משתני סביבה

| **פקודה** | **הסבר** |
|-----------|----------|
| `export $(cat .env \| xargs)` | (Linux/macOS) טעינת משתני .env לסביבה |
| `Get-Content .env \| ForEach-Object {...}` | (PowerShell) טעינת משתני .env |
| `$env:VAR=value; docker compose up` | (PowerShell) הגדרת משתנה והרצה |
| `VAR=value docker compose up` | (Linux/macOS) הגדרת משתנה והרצה |

---

## פקודות בתוך קונטיינר

| **פקודה** | **הסבר** |
|-----------|----------|
| `ip a` | הצגת ממשקי רשת |
| `ping -c 1 <hostname>` | בדיקת חיבור לשרת אחר |
| `nc -z <hostname> <port>` | בדיקת חיבור לפורט |
| `curl http://<hostname>` | בקשת HTTP לשרת |
| `nslookup <hostname>` | בדיקת רזולוציית DNS |
| `cat /etc/resolv.conf` | הצגת הגדרות DNS |
| `pg_isready -U <user>` | (PostgreSQL) בדיקת מוכנות מסד נתונים |
| `env` | הצגת משתני סביבה |
| `ls -la <path>` | הצגת קבצים בתיקייה |
| `cat <file>` | הצגת תוכן קובץ |

---

## ניקוי ותחזוקה

| **פקודה** | **הסבר** |
|-----------|----------|
| `docker image prune` | מחיקת images שלא בשימוש |
| `docker system prune -a` | מחיקת כל המשאבים שלא בשימוש |
| `docker volume prune` | מחיקת volumes שלא בשימוש |
| `docker network prune` | מחיקת רשתות שלא בשימוש |

---

## פקודות מערכת הפעלה

### Linux/macOS

| **פקודה** | **הסבר** |
|-----------|----------|
| `mkdir <directory>` | יצירת תיקייה |
| `mkdir -p <directory>` | יצירת תיקייה כולל תיקיות אב |
| `cd <directory>` | מעבר לתיקייה |
| `cat > file <<'EOF'` | יצירת קובץ עם תוכן |
| `cp <source> <dest>` | העתקת קובץ |

### Windows PowerShell

| **פקודה** | **הסבר** |
|-----------|----------|
| `mkdir <directory>` | יצירת תיקייה |
| `cd <directory>` | מעבר לתיקייה |
| `@"....."@ \| Out-File -Encoding utf8 file` | יצירת קובץ עם תוכן |
| `Copy-Item <source> <dest>` | העתקת קובץ |

---

## 🔍 צ'קליסט לניפוי באגים (Debugging Checklist)

1. **`docker compose ps`** → מה רץ? מה יצא?
2. **`docker compose logs <service>`** → מה השירות אומר?
3. **`docker compose exec <service> sh`** → מה השירות רואה?
4. **`docker compose config`** → איזו תצורה Compose השתמש?
5. **`docker inspect`** / **`docker network inspect`** → מה קיים בזמן ריצה?

---

## 💡 טיפים חשובים

- **קונטיינר רץ כל עוד התהליך הראשי שלו רץ** - אם התהליך מסתיים, הקונטיינר נעצר
- **`docker compose exec` עובד רק על קונטיינרים רצים** - אם הקונטיינר יצא מיד, לא ניתן להיכנס אליו
- **`ports` חושף שירותים לhost** - קונטיינרים מדברים זה עם זה דרך שם השירות ופורט פנימי
- **`localhost` בתוך קונטיינר** = הקונטיינר עצמו, לא ה-host
- **`depends_on`** שולט בסדר הפעלה, לא במוכנות השירות
- **`down -v`** מוחק גם volumes - זה לא באג, זה שליטה מפורשת במחזור החיים
