import urllib.request
import ssl
import json
from typing import Any, Dict, List

CTX = ssl._create_unverified_context()
UA = {"User-Agent": "Mozilla/5.0"}

STOCKS = [
    ("sh600036", "招商银行"),
    ("sz000651", "格力电器"),
    ("sh601628", "中国人寿"),
    ("sz002463", "沪电股份"),
    ("sh600089", "特变电工"),
    ("sh601138", "工业富联"),
    ("sh600031", "三一重工"),
]


def get(url: str) -> Dict[str, Any]:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=15, context=CTX) as resp:
        return json.loads(resp.read().decode("utf-8", errors="ignore"))


def ma(vals: List[float], n: int) -> float:
    if len(vals) < n:
        return float("nan")
    return sum(vals[-n:]) / n


def main() -> None:
    for sym, name in STOCKS:
        url = f"https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param={sym},day,,,35,qfq"
        try:
            data = get(url)
            node = data.get("data", {}).get(sym, {})
            klines = node.get("qfqday") or node.get("day") or []
            closes: List[float] = []
            for line in klines:
                try:
                    closes.append(float(line[2]))
                except Exception:
                    continue
            if len(closes) < 6:
                print(f"{name}: 数据不足 {len(closes)}")
                continue
            cur = closes[-1]
            print(f"{name} {sym}: 收盘={cur} MA5={ma(closes,5):.2f} MA10={ma(closes,10):.2f} MA20={ma(closes,20):.2f} 近5日%={(cur/closes[-6]-1)*100:.2f}")
            print(f"   最近6日收盘: {[round(c,2) for c in closes[-6:]]}")
        except Exception as e:
            print(f"{name}: ERR {e}")


if __name__ == "__main__":
    main()