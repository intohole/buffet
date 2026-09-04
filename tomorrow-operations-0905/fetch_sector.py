import urllib.request
import ssl
import json
from typing import Any, Dict, List

CTX = ssl._create_unverified_context()
UA = {"User-Agent": "Mozilla/5.0"}


def get(url: str) -> Dict[str, Any]:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=15, context=CTX) as resp:
        return json.loads(resp.read().decode("utf-8", errors="ignore"))


def board(fs: str, po: int, label: str, n: int = 8) -> None:
    url = (f"https://push2.eastmoney.com/api/qt/clist/get?pn=1&pz={n}&po={po}&np=1&fltt=2"
           f"&invt=2&fid=f3&fs={fs}&fields=f2,f3,f12,f14")
    data = get(url)
    rows: List[Any] = data.get("data", {}).get("diff", [])
    print(f"== {label} ==")
    for r in rows:
        print(f"  {r.get('f14')} 涨幅{r.get('f3')}%")


def main() -> None:
    board("m:90+t:2", 1, "行业板块 涨幅TOP", 8)
    board("m:90+t:2", 0, "行业板块 跌幅TOP", 5)
    board("m:90+t:3", 1, "概念板块 涨幅TOP", 10)


if __name__ == "__main__":
    main()