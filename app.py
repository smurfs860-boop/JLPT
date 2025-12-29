import random
from pathlib import Path

from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")


VOCAB = [
    {"word": "慣れる", "reading": "なれる", "meaning": "to get used to", "pos": "verb", "category": "Daily life"},
    {"word": "場合", "reading": "ばあい", "meaning": "case / situation", "pos": "noun", "category": "Logic"},
    {"word": "許可", "reading": "きょか", "meaning": "permission", "pos": "noun", "category": "Work"},
    {"word": "検討する", "reading": "けんとうする", "meaning": "to consider", "pos": "verb", "category": "Work"},
    {"word": "届く", "reading": "とどく", "meaning": "to arrive / reach", "pos": "verb", "category": "Logistics"},
    {"word": "遠慮する", "reading": "えんりょする", "meaning": "to hold back / refrain", "pos": "verb", "category": "Etiquette"},
    {"word": "様子", "reading": "ようす", "meaning": "state / appearance", "pos": "noun", "category": "Observation"},
    {"word": "表情", "reading": "ひょうじょう", "meaning": "facial expression", "pos": "noun", "category": "People"},
    {"word": "確かめる", "reading": "たしかめる", "meaning": "to confirm", "pos": "verb", "category": "Work"},
    {"word": "責任", "reading": "せきにん", "meaning": "responsibility", "pos": "noun", "category": "Work"},
    {"word": "余裕", "reading": "よゆう", "meaning": "margin / room (time/money)", "pos": "noun", "category": "Planning"},
    {"word": "状況", "reading": "じょうきょう", "meaning": "situation / status", "pos": "noun", "category": "Logic"},
    {"word": "仕方がない", "reading": "しかたがない", "meaning": "it can’t be helped", "pos": "expression", "category": "Expression"},
    {"word": "回復する", "reading": "かいふくする", "meaning": "to recover", "pos": "verb", "category": "Health"},
    {"word": "途中で", "reading": "とちゅうで", "meaning": "on the way / halfway", "pos": "expression", "category": "Travel"},
    {"word": "お互いに", "reading": "おたがいに", "meaning": "mutually / together", "pos": "expression", "category": "People"},
    {"word": "勇気", "reading": "ゆうき", "meaning": "courage", "pos": "noun", "category": "Emotion"},
    {"word": "誤解", "reading": "ごかい", "meaning": "misunderstanding", "pos": "noun", "category": "People"},
    {"word": "都合", "reading": "つごう", "meaning": "convenience / circumstances", "pos": "noun", "category": "Planning"},
    {"word": "余計な", "reading": "よけいな", "meaning": "excessive / unnecessary", "pos": "na-adjective", "category": "Commentary"},
    {"word": "確実な", "reading": "かくじつな", "meaning": "certain / reliable", "pos": "na-adjective", "category": "Work"},
    {"word": "適切な", "reading": "てきせつな", "meaning": "appropriate", "pos": "na-adjective", "category": "Work"},
    {"word": "明らかな", "reading": "あきらかな", "meaning": "clear / obvious", "pos": "na-adjective", "category": "Logic"},
    {"word": "厳しい", "reading": "きびしい", "meaning": "strict / severe", "pos": "i-adjective", "category": "Commentary"},
    {"word": "詳しい", "reading": "くわしい", "meaning": "detailed", "pos": "i-adjective", "category": "Work"},
    {"word": "頼もしい", "reading": "たのもしい", "meaning": "reliable / promising", "pos": "i-adjective", "category": "People"},
    {"word": "珍しい", "reading": "めずらしい", "meaning": "rare / unusual", "pos": "i-adjective", "category": "Observation"},
    {"word": "偶然", "reading": "ぐうぜん", "meaning": "by chance", "pos": "expression", "category": "Expression"},
    {"word": "当然", "reading": "とうぜん", "meaning": "natural / of course", "pos": "na-adjective", "category": "Logic"},
    {"word": "自然に", "reading": "しぜんに", "meaning": "naturally", "pos": "expression", "category": "Expression"},
]

GRAMMAR = [
    {
        "title": "〜たばかり",
        "usage": "Vた + ばかり",
        "meaning": "just did / just finished",
        "example": "日本に来たばかりなので、まだ友達が少ない。",
        "nuance": "Very recent timing; speaker feels the action is fresh.",
    },
    {
        "title": "〜うちに",
        "usage": "Vる / Vている / い・な / N + うちに",
        "meaning": "while / before (something changes)",
        "example": "熱いうちに早く食べてください。",
        "nuance": "Do something before the situation shifts.",
    },
    {
        "title": "〜ように言う",
        "usage": "Vる / Vない + ように + 言う/注意する",
        "meaning": "tell/ask someone to do or not do",
        "example": "先生に、宿題を忘れないように言われました。",
        "nuance": "Soft instruction compared to 〜てください.",
    },
    {
        "title": "〜わけではない",
        "usage": "Plain form + わけではない",
        "meaning": "it does not mean that… / not necessarily",
        "example": "嫌いなわけではないが、今は食べたくない。",
        "nuance": "Partially deny an assumption; soften disagreement.",
    },
    {
        "title": "〜おそれがある",
        "usage": "Vる / Nの + おそれがある",
        "meaning": "there is a fear/possibility that… (negative result)",
        "example": "大雨で川があふれるおそれがあります。",
        "nuance": "Used for warnings or risk statements.",
    },
    {
        "title": "〜っぱなし",
        "usage": "Vます-stem + っぱなし",
        "meaning": "leave as-is / left in that state",
        "example": "ドアを開けっぱなしにしないでください。",
        "nuance": "Implies carelessness or negligence.",
    },
    {
        "title": "〜に違いない",
        "usage": "Plain form + に違いない",
        "meaning": "must be / I am sure that…",
        "example": "あの明かりは駅に違いない。",
        "nuance": "Strong conviction based on some evidence.",
    },
    {
        "title": "〜ようにしている",
        "usage": "Vる / Vない + ようにしている",
        "meaning": "make an effort to / try to keep doing",
        "example": "毎日日本語で日記を書くようにしています。",
        "nuance": "Habit formation; ongoing effort.",
    },
    {
        "title": "〜わけにはいかない",
        "usage": "Vる + わけにはいかない",
        "meaning": "cannot (due to social/moral reasons)",
        "example": "今日はテストなので、遅刻するわけにはいかない。",
        "nuance": "Speaker feels pressure or responsibility.",
    },
    {
        "title": "〜最中に",
        "usage": "Nの / Vている + 最中に",
        "meaning": "in the middle of / right when",
        "example": "食事の最中に電話が鳴った。",
        "nuance": "Unexpected interruption.",
    },
]

TASKS = [
    {"title": "Shadow 10 lines aloud", "meta": "Listening + pronunciation", "category": "listening"},
    {"title": "Review 10 vocabulary", "meta": "Choose from the vocab explorer", "category": "vocab"},
    {"title": "Write 3 example sentences", "meta": "Use today’s grammar", "category": "grammar"},
    {"title": "Skim one news paragraph", "meta": "Under 5 minutes, no dictionary", "category": "reading"},
    {"title": "Kanji flash (5)", "meta": "On/kun + one sentence", "category": "kanji"},
    {"title": "Speak for 90 seconds", "meta": "Record yourself explaining your day", "category": "speaking"},
]

FOCUS_IDEAS = [
    ["〜たばかり", "〜ようにしている", "〜わけではない"],
    ["〜おそれがある", "〜に違いない", "〜うちに"],
    ["〜わけにはいかない", "〜ように言う", "〜っぱなし"],
]


@app.get("/api/vocab")
def get_vocab():
    categories = sorted({item["category"] for item in VOCAB})
    return jsonify({"items": VOCAB, "categories": categories})


@app.get("/api/grammar")
def get_grammar():
    return jsonify({"items": GRAMMAR})


@app.get("/api/tasks")
def get_tasks():
    return jsonify({"items": TASKS})


@app.get("/api/focus")
def get_focus():
    focus_set = random.choice(FOCUS_IDEAS)
    return jsonify({"items": focus_set, "topic": focus_set[0]})


@app.get("/")
def index():
    return send_from_directory(Path(".").resolve(), "index.html")


if __name__ == "__main__":
    app.run(debug=True)
