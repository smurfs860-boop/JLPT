import json
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent

VOCAB = [
    {
        "word": "慣れる",
        "reading": "なれる",
        "meaning": "to get used to",
        "pos": "verb",
        "category": "Daily life",
        "examples": [
            {"compound": "慣用句", "reading": "かんようく", "meaning": "idiom / set phrase"},
            {"compound": "習慣", "reading": "しゅうかん", "meaning": "habit"},
        ],
    },
    {
        "word": "場合",
        "reading": "ばあい",
        "meaning": "case / situation",
        "pos": "noun",
        "category": "Logic",
        "examples": [
            {"compound": "万一の場合", "reading": "まんいちのばあい", "meaning": "in case of emergency"},
            {"compound": "その場合", "reading": "そのばあい", "meaning": "in that case"},
        ],
    },
    {
        "word": "許可",
        "reading": "きょか",
        "meaning": "permission",
        "pos": "noun",
        "category": "Work",
        "examples": [
            {"compound": "許可証", "reading": "きょかしょう", "meaning": "permit / license"},
            {"compound": "無許可", "reading": "むきょか", "meaning": "without permission"},
        ],
    },
    {
        "word": "検討する",
        "reading": "けんとうする",
        "meaning": "to consider",
        "pos": "verb",
        "category": "Work",
        "examples": [
            {"compound": "再検討", "reading": "さいけんとう", "meaning": "review / reconsideration"},
            {"compound": "検討中", "reading": "けんとうちゅう", "meaning": "under consideration"},
        ],
    },
    {
        "word": "届く",
        "reading": "とどく",
        "meaning": "to arrive / reach",
        "pos": "verb",
        "category": "Logistics",
        "examples": [
            {"compound": "手紙が届く", "reading": "てがみがとどく", "meaning": "a letter arrives"},
            {"compound": "届け出", "reading": "とどけで", "meaning": "report / notification"},
        ],
    },
    {
        "word": "遠慮する",
        "reading": "えんりょする",
        "meaning": "to hold back / refrain",
        "pos": "verb",
        "category": "Etiquette",
        "examples": [
            {"compound": "ご遠慮ください", "reading": "ごえんりょください", "meaning": "please refrain"},
            {"compound": "遠慮なく", "reading": "えんりょなく", "meaning": "without holding back"},
        ],
    },
    {
        "word": "様子",
        "reading": "ようす",
        "meaning": "state / appearance",
        "pos": "noun",
        "category": "Observation",
        "examples": [
            {"compound": "様子を見る", "reading": "ようすをみる", "meaning": "wait and see / watch the situation"},
            {"compound": "様子がおかしい", "reading": "ようすがおかしい", "meaning": "something seems off"},
        ],
    },
    {
        "word": "表情",
        "reading": "ひょうじょう",
        "meaning": "facial expression",
        "pos": "noun",
        "category": "People",
        "examples": [
            {"compound": "表情豊か", "reading": "ひょうじょうゆたか", "meaning": "expressive"},
            {"compound": "真剣な表情", "reading": "しんけんなひょうじょう", "meaning": "serious look"},
        ],
    },
    {
        "word": "確かめる",
        "reading": "たしかめる",
        "meaning": "to confirm",
        "pos": "verb",
        "category": "Work",
        "examples": [
            {"compound": "身元を確かめる", "reading": "みもとをたしかめる", "meaning": "verify identity"},
            {"compound": "真偽を確かめる", "reading": "しんぎをたしかめる", "meaning": "check the truth"},
        ],
    },
    {
        "word": "責任",
        "reading": "せきにん",
        "meaning": "responsibility",
        "pos": "noun",
        "category": "Work",
        "examples": [
            {"compound": "責任者", "reading": "せきにんしゃ", "meaning": "person in charge"},
            {"compound": "責任感", "reading": "せきにんかん", "meaning": "sense of responsibility"},
        ],
    },
    {
        "word": "余裕",
        "reading": "よゆう",
        "meaning": "margin / room (time/money)",
        "pos": "noun",
        "category": "Planning",
        "examples": [
            {"compound": "時間に余裕がある", "reading": "じかんによゆうがある", "meaning": "have time to spare"},
            {"compound": "余裕がない", "reading": "よゆうがない", "meaning": "have no leeway"},
        ],
    },
    {
        "word": "状況",
        "reading": "じょうきょう",
        "meaning": "situation / status",
        "pos": "noun",
        "category": "Logic",
        "examples": [
            {"compound": "現在の状況", "reading": "げんざいのじょうきょう", "meaning": "current situation"},
            {"compound": "状況説明", "reading": "じょうきょうせつめい", "meaning": "situational briefing"},
        ],
    },
    {
        "word": "仕方がない",
        "reading": "しかたがない",
        "meaning": "it can’t be helped",
        "pos": "expression",
        "category": "Expression",
        "examples": [
            {"compound": "仕方なく", "reading": "しかたなく", "meaning": "reluctantly"},
            {"compound": "仕方のない人", "reading": "しかたのないひと", "meaning": "hopeless person"},
        ],
    },
    {
        "word": "回復する",
        "reading": "かいふくする",
        "meaning": "to recover",
        "pos": "verb",
        "category": "Health",
        "examples": [
            {"compound": "体力が回復する", "reading": "たいりょくがかいふくする", "meaning": "regain stamina"},
            {"compound": "回復傾向", "reading": "かいふくけいこう", "meaning": "signs of recovery"},
        ],
    },
    {
        "word": "途中で",
        "reading": "とちゅうで",
        "meaning": "on the way / halfway",
        "pos": "expression",
        "category": "Travel",
        "examples": [
            {"compound": "道の途中で", "reading": "みちのとちゅうで", "meaning": "on the way"},
            {"compound": "途中下車", "reading": "とちゅうげしゃ", "meaning": "stopover ticket"},
        ],
    },
    {
        "word": "お互いに",
        "reading": "おたがいに",
        "meaning": "mutually / together",
        "pos": "expression",
        "category": "People",
        "examples": [
            {"compound": "お互いさま", "reading": "おたがいさま", "meaning": "we're in the same boat"},
            {"compound": "お互いの立場", "reading": "おたがいのたちば", "meaning": "each other's position"},
        ],
    },
    {
        "word": "勇気",
        "reading": "ゆうき",
        "meaning": "courage",
        "pos": "noun",
        "category": "Emotion",
        "examples": [
            {"compound": "勇気を出す", "reading": "ゆうきをだす", "meaning": "pluck up courage"},
            {"compound": "勇気づける", "reading": "ゆうきづける", "meaning": "encourage"},
        ],
    },
    {
        "word": "誤解",
        "reading": "ごかい",
        "meaning": "misunderstanding",
        "pos": "noun",
        "category": "People",
        "examples": [
            {"compound": "誤解を招く", "reading": "ごかいをまねく", "meaning": "cause a misunderstanding"},
            {"compound": "誤解が解ける", "reading": "ごかいがとける", "meaning": "clear up a misunderstanding"},
        ],
    },
    {
        "word": "都合",
        "reading": "つごう",
        "meaning": "convenience / circumstances",
        "pos": "noun",
        "category": "Planning",
        "examples": [
            {"compound": "都合がつく", "reading": "つごうがつく", "meaning": "manage to fit the schedule"},
            {"compound": "都合が悪い", "reading": "つごうがわるい", "meaning": "inconvenient"},
        ],
    },
    {
        "word": "余計な",
        "reading": "よけいな",
        "meaning": "excessive / unnecessary",
        "pos": "na-adjective",
        "category": "Commentary",
        "examples": [
            {"compound": "余計なお世話", "reading": "よけいなおせわ", "meaning": "meddling / needless help"},
            {"compound": "余計な心配", "reading": "よけいなしんぱい", "meaning": "unnecessary worry"},
        ],
    },
    {
        "word": "確実な",
        "reading": "かくじつな",
        "meaning": "certain / reliable",
        "pos": "na-adjective",
        "category": "Work",
        "examples": [
            {"compound": "確実な方法", "reading": "かくじつなほうほう", "meaning": "reliable method"},
            {"compound": "確実に成功", "reading": "かくじつにせいこう", "meaning": "succeed for sure"},
        ],
    },
    {
        "word": "適切な",
        "reading": "てきせつな",
        "meaning": "appropriate",
        "pos": "na-adjective",
        "category": "Work",
        "examples": [
            {"compound": "適切な対応", "reading": "てきせつなたいおう", "meaning": "appropriate response"},
            {"compound": "適切な表現", "reading": "てきせつなひょうげん", "meaning": "suitable wording"},
        ],
    },
    {
        "word": "明らかな",
        "reading": "あきらかな",
        "meaning": "clear / obvious",
        "pos": "na-adjective",
        "category": "Logic",
        "examples": [
            {"compound": "明らかな違い", "reading": "あきらかなちがい", "meaning": "obvious difference"},
            {"compound": "原因を明らかにする", "reading": "げんいんをあきらかにする", "meaning": "make the cause clear"},
        ],
    },
    {
        "word": "厳しい",
        "reading": "きびしい",
        "meaning": "strict / severe",
        "pos": "i-adjective",
        "category": "Commentary",
        "examples": [
            {"compound": "厳しい条件", "reading": "きびしいじょうけん", "meaning": "strict conditions"},
            {"compound": "厳しく指導する", "reading": "きびしくしどうする", "meaning": "instruct strictly"},
        ],
    },
    {
        "word": "詳しい",
        "reading": "くわしい",
        "meaning": "detailed",
        "pos": "i-adjective",
        "category": "Work",
        "examples": [
            {"compound": "詳しい説明", "reading": "くわしいせつめい", "meaning": "detailed explanation"},
            {"compound": "地理に詳しい", "reading": "ちりにくわしい", "meaning": "knowledgeable about geography"},
        ],
    },
    {
        "word": "頼もしい",
        "reading": "たのもしい",
        "meaning": "reliable / promising",
        "pos": "i-adjective",
        "category": "People",
        "examples": [
            {"compound": "頼もしい味方", "reading": "たのもしいみかた", "meaning": "reliable ally"},
            {"compound": "頼もしく感じる", "reading": "たのもしくかんじる", "meaning": "feel reassured"},
        ],
    },
    {
        "word": "珍しい",
        "reading": "めずらしい",
        "meaning": "rare / unusual",
        "pos": "i-adjective",
        "category": "Observation",
        "examples": [
            {"compound": "珍しい体験", "reading": "めずらしいたいけん", "meaning": "rare experience"},
            {"compound": "珍しい動物", "reading": "めずらしいどうぶつ", "meaning": "unusual animal"},
        ],
    },
    {
        "word": "偶然",
        "reading": "ぐうぜん",
        "meaning": "by chance",
        "pos": "expression",
        "category": "Expression",
        "examples": [
            {"compound": "偶然会う", "reading": "ぐうぜんあう", "meaning": "meet by chance"},
            {"compound": "偶然の一致", "reading": "ぐうぜんのいっち", "meaning": "coincidence"},
        ],
    },
    {
        "word": "当然",
        "reading": "とうぜん",
        "meaning": "natural / of course",
        "pos": "na-adjective",
        "category": "Logic",
        "examples": [
            {"compound": "当然の結果", "reading": "とうぜんのけっか", "meaning": "natural outcome"},
            {"compound": "当然だと思う", "reading": "とうぜんだとおもう", "meaning": "think it is only natural"},
        ],
    },
    {
        "word": "自然に",
        "reading": "しぜんに",
        "meaning": "naturally",
        "pos": "expression",
        "category": "Expression",
        "examples": [
            {"compound": "自然に笑う", "reading": "しぜんにわらう", "meaning": "smile naturally"},
            {"compound": "自然に治る", "reading": "しぜんになおる", "meaning": "heal on its own"},
        ],
    },
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
    {"title": "Listening test: short dialogues", "meta": "5 quick JLPT-style questions", "category": "listening"},
    {"title": "Listening test: announcements", "meta": "Bus/train audio prompts", "category": "listening"},
    {"title": "Listening test: instructions", "meta": "Follow spoken steps to choose answers", "category": "listening"},
    {"title": "Listening test: opinions", "meta": "Decide speaker stance from a clip", "category": "listening"},
    {"title": "Listening test: schedules", "meta": "Match times and places from audio", "category": "listening"},
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


def json_response(handler: SimpleHTTPRequestHandler, payload: dict) -> None:
    encoded = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(200)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(encoded)))
    handler.end_headers()
    handler.wfile.write(encoded)


class StudyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):  # noqa: N802  (http.server naming)
        if self.path == "/api/vocab":
            categories = sorted({item["category"] for item in VOCAB})
            json_response(self, {"items": VOCAB, "categories": categories})
            return

        if self.path == "/api/grammar":
            json_response(self, {"items": GRAMMAR})
            return

        if self.path == "/api/tasks":
            json_response(self, {"items": TASKS})
            return

        if self.path == "/api/focus":
            focus_set = FOCUS_IDEAS[0]
            json_response(self, {"items": focus_set, "topic": focus_set[0]})
            return

        if self.path == "/":
            self.path = "/index.html"

        return super().do_GET()

    def log_message(self, fmt, *args):
        return  # silence default stdout noise


def run_server():
    port = int(os.getenv("PORT", "5000"))
    with ThreadingHTTPServer(("0.0.0.0", port), StudyHandler) as httpd:
        print(f"Serving JLPT N3 Study Hub at http://localhost:{port}")
        httpd.serve_forever()


if __name__ == "__main__":
    run_server()
