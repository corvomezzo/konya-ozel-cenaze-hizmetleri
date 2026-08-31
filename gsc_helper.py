"""Google Search Console API helper for cenaze-blog automation."""
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

ENV_PATH = Path(__file__).parent / ".env"


def load_env() -> dict:
    env = {}
    with open(ENV_PATH) as f:
        for ln in f:
            ln = ln.strip()
            if "=" in ln and not ln.startswith("#"):
                k, v = ln.split("=", 1)
                env[k.strip()] = v.strip()
    return env


def get_access_token(env: dict) -> str:
    data = urllib.parse.urlencode({
        "refresh_token": env["GSC_OAUTH_REFRESH_TOKEN"],
        "client_id": env["GSC_OAUTH_CLIENT_ID"],
        "client_secret": env["GSC_OAUTH_CLIENT_SECRET"],
        "grant_type": "refresh_token",
    }).encode()
    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token", data=data, method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())["access_token"]


def inspect_url(url: str) -> dict:
    """Inspect a URL via GSC. Returns inspection result dict."""
    env = load_env()
    token = get_access_token(env)
    site = "sc-domain:konyacenazehizmetleri.com"
    body = json.dumps({"inspectionUrl": url, "siteUrl": site}).encode()
    req = urllib.request.Request(
        "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect",
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())


def submit_sitemap(sitemap_url: str) -> int:
    env = load_env()
    token = get_access_token(env)
    site = "sc-domain:konyacenazehizmetleri.com"
    endpoint = (
        f"https://www.googleapis.com/webmasters/v3/sites/"
        f"{urllib.parse.quote(site, safe=':')}/sitemaps/"
        f"{urllib.parse.quote(sitemap_url, safe=':/')}"
    )
    req = urllib.request.Request(
        endpoint, headers={"Authorization": f"Bearer {token}"}, method="PUT"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


def list_sitemaps() -> list:
    env = load_env()
    token = get_access_token(env)
    site = "sc-domain:konyacenazehizmetleri.com"
    req = urllib.request.Request(
        f"https://www.googleapis.com/webmasters/v3/sites/"
        f"{urllib.parse.quote(site, safe=':')}/sitemaps",
        headers={"Authorization": f"Bearer {token}"},
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read()).get("sitemap", [])


def search_analytics(days: int = 7, row_limit: int = 25) -> dict:
    """Pull search analytics for last N days."""
    from datetime import datetime, timedelta
    env = load_env()
    token = get_access_token(env)
    site = "sc-domain:konyacenazehizmetleri.com"
    end = datetime.utcnow().strftime("%Y-%m-%d")
    start = (datetime.utcnow() - timedelta(days=days)).strftime("%Y-%m-%d")
    body = json.dumps({
        "startDate": start,
        "endDate": end,
        "dimensions": ["query"],
        "rowLimit": row_limit,
    }).encode()
    req = urllib.request.Request(
        f"https://www.googleapis.com/webmasters/v3/sites/"
        f"{urllib.parse.quote(site, safe=':')}/searchAnalytics/query",
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: gsc_helper.py [inspect <url> | sitemap | analytics [days]]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "inspect":
        url = sys.argv[2]
        result = inspect_url(url)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif cmd == "sitemap":
        for sm in list_sitemaps():
            print(f"{sm.get('path')} — {sm.get('lastSubmitted')}")
    elif cmd == "analytics":
        days = int(sys.argv[2]) if len(sys.argv) > 2 else 7
        result = search_analytics(days)
        print(json.dumps(result, indent=2, ensure_ascii=False))