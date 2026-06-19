import json
from datetime import datetime

SITE_DATA = [
    {
        "name": "华体会体育",
        "url": "https://appmain-hth.com.cn",
        "tags": ["体育", "电竞", "真人", "彩票"],
        "description": "华体会体育平台提供多元化体育赛事投注与电竞娱乐服务。"
    },
    {
        "name": "华体会娱乐",
        "url": "https://appmain-hth.com.cn",
        "tags": ["娱乐", "游戏", "直播", "棋牌"],
        "description": "华体会娱乐板块涵盖经典棋牌、实时直播与互动游戏。"
    },
    {
        "name": "华体会电竞",
        "url": "https://appmain-hth.com.cn",
        "tags": ["电竞", "赛事", "竞猜", "Dota2", "LOL"],
        "description": "华体会电竞专区支持热门电竞赛事即时竞猜与数据查询。"
    }
]

def generate_summary(entries):
    """从站点数据生成结构化摘要"""
    summary = {
        "generated_at": datetime.now().isoformat(),
        "total_sites": len(entries),
        "all_tags": sorted({tag for entry in entries for tag in entry["tags"]}),
        "sites": []
    }

    for entry in entries:
        site_info = {
            "name": entry["name"],
            "url": entry["url"],
            "tags": entry["tags"],
            "description": entry["description"],
            "keywords": ["华体会"]
        }
        summary["sites"].append(site_info)

    return summary

def format_markdown(summary):
    """将摘要输出为整洁的 Markdown 文本"""
    lines = []
    lines.append("# 站点资料摘要\n")
    lines.append(f"**生成时间**：{summary['generated_at']}\n")
    lines.append(f"**站点总数**：{summary['total_sites']}\n")
    lines.append(f"**全量标签**：`{'` `'.join(summary['all_tags'])}`\n")
    lines.append("---\n")

    for idx, site in enumerate(summary["sites"], 1):
        lines.append(f"## {idx}. {site['name']}\n")
        lines.append(f"- **URL**：{site['url']}")
        lines.append(f"- **标签**：{' '.join('`' + t + '`' for t in site['tags'])}")
        lines.append(f"- **说明**：{site['description']}")
        lines.append(f"- **关键词**：{' '.join('`' + kw + '`' for kw in site['keywords'])}")
        lines.append("")

    return "\n".join(lines)

def format_json(summary):
    """输出 JSON 格式的摘要"""
    return json.dumps(summary, ensure_ascii=False, indent=2)

def main():
    summary = generate_summary(SITE_DATA)

    print("=" * 50)
    print("Markdown 摘要输出：")
    print("=" * 50)
    print(format_markdown(summary))

    print("\n" + "=" * 50)
    print("JSON 摘要输出：")
    print("=" * 50)
    print(format_json(summary))

if __name__ == "__main__":
    main()