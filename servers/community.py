import json
from pathlib import Path
from mcp.server.mcpserver import MCPServer

BASE = Path("/opt/community-mcp/data/official")

identity_data = json.loads(
    (BASE / "ivanivska-mcp0.json").read_text(encoding="utf-8")
)

geodata = json.loads(
    (BASE / "ivanivska-geodata.json").read_text(encoding="utf-8")
)

server = MCPServer(
    name="ivanivska-community",
    title="Іванівська територіальна громада",
    description=(
        "Офіційні адміністративні та довідкові географічні "
        "дані Іванівської громади Чернігівської області."
    ),
    version="0.1.0",
)

@server.tool()
def get_identity() -> dict:
    """Повернути офіційну назву, код КАТОТТГ, область і район громади."""
    return identity_data["community"]

@server.tool()
def list_villages() -> list[dict]:
    """Перелічити всі 17 сіл громади з кодами КАТОТТГ і координатами OSM."""
    geo_by_code = {
        item["katottg"]: item
        for item in geodata["villages"]
    }

    result = []
    for village in identity_data["villages"]:
        geo = geo_by_code.get(village["katottg"], {})
        result.append({
            "name": village["name"],
            "katottg": village["katottg"],
            "latitude": geo.get("latitude"),
            "longitude": geo.get("longitude"),
            "coordinate_source": geo.get("source"),
        })
    return result

@server.tool()
def get_sources() -> dict:
    """Повернути джерела та дати актуальності адміністративних і географічних даних."""
    return {
        "administrative": identity_data["source"],
        "geographic": {
            "name": geodata["source"],
            "retrieved_at": geodata["retrieved_at"],
            "website": "https://www.openstreetmap.org",
        },
    }

if __name__ == "__main__":
    server.run(transport="stdio")
