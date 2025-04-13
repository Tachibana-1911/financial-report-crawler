# VTuber IRデータ分析ポートフォリオ

## 📌 概要

本プロジェクトは、カバー株式会社（ホロライブ）やANYCOLOR（にじさんじ）などのVTuber企業における、
**YouTube登録者数・再生数などのKPIと、IR資料中の売上／利益データとの関係性を分析**することを目的としています。

PDF、Web、API、Excelなど複数データソースを扱い、
Pythonベースでデータ取得・構造化・可視化まで一貫して実行する、ポートフォリオ向けデータパイプラインです。

---

## 🔧 使用技術

- Python（3.11）
- pandas / matplotlib / seaborn
- pdfplumber / requests / selenium
- Git / GitHub
- Excel（手動構造化テンプレート）
- YouTube Data API（予定）
- Streamlit（可視化用、予定）

---

## 📁 構成

```
financial-report-crawler/
├── data/                  # PDF・KPIの元データ
├── src/
│   ├── extractor.py       # PDF構造化スクリプト
│   ├── ir_scraper.py      # IR資料PDFダウンロード
│   └── kpi_loader.py      # KPIテンプレート読み込み
├── output/
│   └── kpi_vs_revenue.csv # 登録者数×売上データ
├── streamlit_app.py       # グラフ可視化アプリ（予定）
└── README.md              # 本ドキュメント
```

---

## 📊 分析テーマ

- 登録者数と売上の相関
- 再生数とスパチャ推定額の分布比較
- セグメント別（JP/EN/ID）の貢献度推定
- 年度ごとのKPI増加傾向とIR資料成長率の比較

---

## 📝 データ出典

- カバー株式会社・ANYCOLOR株式会社 IRページ（公式PDF）
- Hololyzer、YouTube API などの公開データ

---

## 🎯 想定利用シーン

- データエンジニア／データアナリスト志望者のポートフォリオ
- コンテンツ業界における“ファン価値と収益性”のモデル化
- 社内ダッシュボードやKPI設計の参考

---

## 🗝️ ライセンス・注意

本リポジトリは教育・研究目的で構成されています。  
所属事務所・タレント様との関係はございません。
