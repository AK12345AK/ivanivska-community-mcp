# Ivanivska Community MCP

MCP-сервери Іванівської територіальної громади
Чернігівського району Чернігівської області.

## Архітектура

- 1 MCP-сервер територіальної громади
- 17 окремих MCP-серверів населених пунктів
- Python, MCP SDK, Starlette, Uvicorn
- Streamable HTTP через HTTPS

## Публічна адреса

https://community.ukrdigital.org

MCP громади:
https://community.ukrdigital.org/mcp/community/mcp

MCP окремого села:
https://community.ukrdigital.org/mcp/{KATOTTG}/mcp

## Інструменти

MCP громади:
- get_identity
- list_villages
- get_sources

MCP села:
- get_identity
- get_basic_profile
- get_sources

## Джерела

- КАТОТТГ — Міністерство розвитку громад та територій України
- Географічні координати — OpenStreetMap / Nominatim

## Статус

Версія 0.1.0 — базові адміністративні та географічні дані.

Усі 18 MCP протестовані через HTTPS.
MCP громади успішно підключений до ChatGPT.

## Розвиток

Планується інтеграція документів сільради,
рішень сесій, бюджету, закупівель та інших
відкритих даних громади.
