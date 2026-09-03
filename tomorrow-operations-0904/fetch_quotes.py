import urllib.request
import re
import ssl
from typing import List, Dict

CTX = ssl._create_unverified_context()

URL = "https://qt.gtimg.cn/q="
SYMBOLS = [
    "sh000001", "sz399001", "sz399006", "sh000300",
    "sh600036", "sz000651", "sh601628", "sz002463",
    "sh600031", "sh600089", "sh601138", "sh601088",
    "sh600118", "sh600566", "sh600522", "sh600487",
]


def fetch(symbols: List[str]) -> str:
    req = urllib.request.Request(URL + ",".join(symbols), headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15, context=CTX) as resp:
        return resp.read().decode("gbk", errors="ignore")


def parse(raw: str) -> Dict[str, Dict[str, str]]:
    result: Dict[str, Dict[str, str]] = {}
    for m in re.finditer(r'v_(\w+)="([^"]*)"', raw):
        sym = m.group(1)
        fields = m.group(2).split("~")
        if len(fields) < 50:
            result[sym] = {"raw_fields": str(len(fields))}
            continue
        result[sym] = {
            "name": fields[1],
            "code": fields[2],
            "price": fields[3],
            "prev_close": fields[4],
            "open": fields[5],
            "change": fields[31],
            "pct": fields[32],
            "high": fields[33],
            "low": fields[34],
            "amount_wan": fields[37],
            "turnover": fields[38],
            "time": fields[30],
        }
    return result


def main() -> None:
    data = fetch(SYMBOLS)
    parsed = parse(data)
    for sym in SYMBOLS:
        info = parsed.get(sym)
        if not info:
            print(f"{sym}: NO DATA")
            continue
        print(f"{sym} {info.get('name','')} 现价={info.get('price','')} 涨跌%={info.get('pct','')} "
              f"开盘={info.get('open','')} 高={info.get('high','')} 低={info.get('low','')} "
              f"成交额万={info.get('amount_wan','')} 换手={info.get('turnover','')} time={info.get('time','')}")


if __name__ == "__main__":
    main()