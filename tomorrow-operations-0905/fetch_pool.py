import urllib.request
import ssl
import json
from typing import Any, Dict, List

CTX = ssl._create_unverified_context()
UA = {"User-Agent": "Mozilla/5.0"}
DATE = "20260904"
UT = "7eea3edcaed734bea9cbfc24409ed989"


def get(url: str) -> Dict[str, Any]:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=15, context=CTX) as resp:
        return json.loads(resp.read().decode("utf-8", errors="ignore"))


def main() -> None:
    try:
        zt_full = get(f"https://push2ex.eastmoney.com/getTopicZTPool?ut={UT}&dpt=wz.ztzt&Pageindex=0&pagesize=400&sort=fbt:asc&date={DATE}")
        dt_full = get(f"https://push2ex.eastmoney.com/getTopicDTPool?ut={UT}&dpt=wz.ztzt&Pageindex=0&pagesize=400&sort=fbt:asc&date={DATE}")
        zt_data = zt_full.get("data") or {}
        dt_data = dt_full.get("data") or {}
        zt_pool: List[Any] = zt_data.get("pool", [])
        dt_pool: List[Any] = dt_data.get("pool", [])
        print(f"涨停总数(全市场): {zt_data.get('tc', 0)}")
        print(f"跌停总数: {dt_data.get('tc', 0)}")
        print("\n== 涨停明细(按连板降序) ==")
        ranked = sorted(zt_pool, key=lambda x: x.get("lbc", 0), reverse=True)
        for item in ranked[:60]:
            print(f"  {item.get('n','')} {item.get('c','')} 连板{item.get('lbc',0)} 涨幅{item.get('zttj',{}).get('zbc') if item.get('zttj') else 10}")
        print("\n== 跌停明细 ==")
        for item in dt_pool[:20]:
            print(f"  {item.get('n','')} {item.get('c','')} 连跌{item.get('lbc',0)}")
    except Exception as e:
        print("POOL ERR", e)


if __name__ == "__main__":
    main()