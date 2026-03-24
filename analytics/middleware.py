import hashlib


class VisitMiddleware:
    EXCLUDED_PATHS = ('/admin/', '/static/', '/media/', '/favicon.ico')

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        path = request.path_info

        if not any(path.startswith(p) for p in self.EXCLUDED_PATHS):
            self._record(request)

        return response

    def _record(self, request):
        from analytics.models import Visit

        ip_raw = (
            request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0].strip()
            or request.META.get('REMOTE_ADDR', '')
        )
        ip_anon = self._anonymize_ip(ip_raw)

        Visit.objects.create(
            page=request.path_info,
            user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
            referrer=request.META.get('HTTP_REFERER', '')[:500],
            ip_anonimizada=ip_anon or None,
        )

    @staticmethod
    def _anonymize_ip(ip: str) -> str:
        if not ip:
            return ''
        if ':' in ip:
            # IPv6 — keep first 4 groups
            parts = ip.split(':')
            return ':'.join(parts[:4]) + '::'
        # IPv4 — zero last octet
        parts = ip.split('.')
        if len(parts) == 4:
            return f'{parts[0]}.{parts[1]}.{parts[2]}.0'
        return ip
