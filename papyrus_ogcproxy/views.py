from urlparse import urlparse
from httplib2 import Http

from pyramid.httpexceptions import (HTTPForbidden, HTTPBadRequest,
                                    HTTPBadGateway, HTTPNotAcceptable)
from pyramid.response import Response


allowed_content_types = (
    "application/xml", "text/xml",
    "application/vnd.ogc.se_xml",            # OGC Service Exception
    "application/vnd.ogc.se+xml",            # OGC Service Exception
    "application/vnd.ogc.success+xml",       # OGC Success (SLD Put)
    "application/vnd.ogc.wms_xml",           # WMS Capabilities
    "application/vnd.ogc.context+xml",       # WMC
    "application/vnd.ogc.gml",               # GML
    "application/vnd.ogc.sld+xml",           # SLD
    "application/vnd.google-earth.kml+xml",  # KML
)

allowed_hosts = (
    # list allowed hosts here (no port limiting)
)

forwarded_headers = (
    "Accept-Language",
    "Accept-Encoding",
    "Accept",
    "Cache-Control",
    "Content-Type",
)

# The proxy to use to make requests (default: None).
#
# Example usage:
#   views.proxy_info = ProxyInfo(socks.SOCKS5, 'localhost', 1080)
#
proxy_info = None


def ogcproxy(request):
    url = request.params.get("url")
    if url is None:
        return HTTPBadRequest("Missing url in the query string")

    # check for full url
    parsed_url = urlparse(url)
    if not parsed_url.netloc or parsed_url.scheme not in ("http", "https"):
        return HTTPBadRequest("Wrong scheme")

    # forward request to target (without Host Header)
    http = Http(
        disable_ssl_certificate_validation=True,
        proxy_info=proxy_info)

    headers = {h: request.headers[h] for h in forwarded_headers if h in request.headers}

    try:
        resp, content = http.request(
            url, method=request.method, body=request.body, headers=headers
        )
    except:
        return HTTPBadGateway()

    # check for allowed content types
    if "content-type" in resp:
        ct = resp["content-type"]
        if not ct.split(";")[0] in allowed_content_types:
            # allow any content type from allowed hosts (any port)
            if parsed_url.netloc not in allowed_hosts:
                return HTTPForbidden("Wrong returned content type")
    else:
        return HTTPNotAcceptable("No returned content type")

    response = Response(content, status=resp.status,
                        headers={"Content-Type": ct})

    return response
