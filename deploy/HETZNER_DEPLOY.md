# Green Dome — Despliegue en Hetzner

## 1. Contratar servidor en Hetzner
- Ve a hetzner.com → Cloud → New Project → Add Server
- Tipo: **CX22** (2 vCPU, 4 GB RAM) — suficiente para empezar
- SO: **Ubuntu 24.04 LTS**
- Ubicación: **Helsinki** o **Falkenstein** (más cerca de Sevilla)
- Añade tu SSH key pública
- Anota la IP pública del servidor

## 2. Comprar dominio
- Puedes comprar en Hetzner mismo (DNS → Domains) o en cualquier registrador
- Apunta los registros DNS a la IP del servidor:
  ```
  A    greendome.com      → IP_DEL_SERVIDOR
  A    www.greendome.com  → IP_DEL_SERVIDOR
  ```

## 3. Conectar al servidor
```bash
ssh root@IP_DEL_SERVIDOR
```

## 4. Preparar el servidor
```bash
apt update && apt upgrade -y
apt install -y python3-pip python3-venv nginx certbot python3-certbot-nginx git

# Crear usuario de la app
useradd -m -s /bin/bash greendome
usermod -aG www-data greendome

# Directorios
mkdir -p /var/www/greendome /var/log/greendome
chown -R greendome:www-data /var/www/greendome /var/log/greendome
```

## 5. Subir el proyecto
Desde tu PC Windows (en PowerShell o WSL):
```bash
# Opción A: Git (recomendado)
cd /var/www/greendome
git clone TU_REPO_GIT .

# Opción B: rsync/scp
scp -r "C:/Users/Windows 11/Desktop/Proyecto Felipe/." root@IP:/var/www/greendome/
```

## 6. Instalar dependencias en el servidor
```bash
su - greendome
cd /var/www/greendome
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

## 7. Configurar variables de entorno
```bash
cp deploy/.env.production .env
nano .env   # Edita y rellena los valores reales
```
Genera una SECRET_KEY segura:
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

## 8. Preparar Django para producción
```bash
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser   # Crea tu usuario admin
python manage.py optimize_seo      # Primera carga de SEO
```

## 9. Instalar servicio Gunicorn
```bash
cp deploy/greendome.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable greendome
systemctl start greendome
systemctl status greendome   # Debe mostrar "active (running)"
```

## 10. Configurar Nginx
```bash
cp deploy/nginx.conf /etc/nginx/sites-available/greendome
ln -s /etc/nginx/sites-available/greendome /etc/nginx/sites-enabled/
nginx -t   # Debe decir "syntax is ok"
systemctl reload nginx
```

## 11. Certificado SSL gratuito (HTTPS)
```bash
certbot --nginx -d greendome.com -d www.greendome.com
```
Certbot se renueva solo automáticamente.

## 12. Configurar SEO diario en el servidor
```bash
crontab -e -u greendome
# Añade esta línea:
0 3 * * * /var/www/greendome/venv/bin/python /var/www/greendome/manage.py optimize_seo >> /var/log/greendome/seo.log 2>&1
```

## 13. Verificar
- Abre https://greendome.com en el navegador
- Accede al admin: https://greendome.com/admin/

## Comandos útiles en producción
```bash
# Ver logs de la app
journalctl -u greendome -f

# Reiniciar tras cambios
systemctl restart greendome

# Actualizar código (si usas Git)
cd /var/www/greendome
git pull
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
systemctl restart greendome
```
