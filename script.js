const vocab = [
  { word: "慣れる", reading: "なれる", meaning: "to get used to", pos: "verb", category: "Daily life" },
  { word: "場合", reading: "ばあい", meaning: "case / situation", pos: "noun", category: "Logic" },
  { word: "許可", reading: "きょか", meaning: "permission", pos: "noun", category: "Work" },
  { word: "検討する", reading: "けんとうする", meaning: "to consider", pos: "verb", category: "Work" },
  { word: "届く", reading: "とどく", meaning: "to arrive / reach", pos: "verb", category: "Logistics" },
  { word: "遠慮する", reading: "えんりょする", meaning: "to hold back / refrain", pos: "verb", category: "Etiquette" },
  { word: "様子", reading: "ようす", meaning: "state / appearance", pos: "noun", category: "Observation" },
  { word: "表情", reading: "ひょうじょう", meaning: "facial expression", pos: "noun", category: "People" },
  { word: "確かめる", reading: "たしかめる", meaning: "to confirm", pos: "verb", category: "Work" },
  { word: "責任", reading: "せきにん", meaning: "responsibility", pos: "noun", category: "Work" },
  { word: "余裕", reading: "よゆう", meaning: "margin / room (time/money)", pos: "noun", category: "Planning" },
  { word: "状況", reading: "じょうきょう", meaning: "situation / status", pos: "noun", category: "Logic" },
  { word: "仕方がない", reading: "しかたがない", meaning: "it can’t be helped", pos: "expression", category: "Expression" },
  { word: "回復する", reading: "かいふくする", meaning: "to recover", pos: "verb", category: "Health" },
  { word: "途中で", reading: "とちゅうで", meaning: "on the way / halfway", pos: "expression", category: "Travel" },
  { word: "お互いに", reading: "おたがいに", meaning: "mutually / together", pos: "expression", category: "People" },
  { word: "勇気", reading: "ゆうき", meaning: "courage", pos: "noun", category: "Emotion" },
  { word: "誤解", reading: "ごかい", meaning: "misunderstanding", pos: "noun", category: "People" },
  { word: "都合", reading: "つごう", meaning: "convenience / circumstances", pos: "noun", category: "Planning" },
  { word: "余計な", reading: "よけいな", meaning: "excessive / unnecessary", pos: "na-adjective", category: "Commentary" },
  { word: "確実な", reading: "かくじつな", meaning: "certain / reliable", pos: "na-adjective", category: "Work" },
  { word: "適切な", reading: "てきせつな", meaning: "appropriate", pos: "na-adjective", category: "Work" },
  { word: "明らかな", reading: "あきらかな", meaning: "clear / obvious", pos: "na-adjective", category: "Logic" },
  { word: "厳しい", reading: "きびしい", meaning: "strict / severe", pos: "i-adjective", category: "Commentary" },
  { word: "詳しい", reading: "くわしい", meaning: "detailed", pos: "i-adjective", category: "Work" },
  { word: "頼もしい", reading: "たのもしい", meaning: "reliable / promising", pos: "i-adjective", category: "People" },
  { word: "珍しい", reading: "めずらしい", meaning: "rare / unusual", pos: "i-adjective", category: "Observation" },
  { word: "偶然", reading: "ぐうぜん", meaning: "by chance", pos: "expression", category: "Expression" },
  { word: "当然", reading: "とうぜん", meaning: "natural / of course", pos: "na-adjective", category: "Logic" },
  { word: "自然に", reading: "しぜんに", meaning: "naturally", pos: "expression", category: "Expression" },
];

const grammarPatterns = [
  {
    title: "〜たばかり",
    usage: "Vた + ばかり",
    meaning: "just did / just finished",
    example: "日本に来たばかりなので、まだ友達が少ない。",
    nuance: "Very recent timing; speaker feels the action is fresh.",
  },
  {
    title: "〜うちに",
    usage: "Vる / Vている / い・な / N + うちに",
    meaning: "while / before (something changes)",
    example: "熱いうちに早く食べてください。",
    nuance: "Do something before the situation shifts.",
  },
  {
    title: "〜ように言う",
    usage: "Vる / Vない + ように + 言う/注意する",
    meaning: "tell/ask someone to do or not do",
    example: "先生に、宿題を忘れないように言われました。",
    nuance: "Soft instruction compared to 〜てください.",
  },
  {
    title: "〜わけではない",
    usage: "Plain form + わけではない",
    meaning: "it does not mean that… / not necessarily",
    example: "嫌いなわけではないが、今は食べたくない。",
    nuance: "Partially deny an assumption; soften disagreement.",
  },
  {
    title: "〜おそれがある",
    usage: "Vる / Nの + おそれがある",
    meaning: "there is a fear/possibility that… (negative result)",
    example: "大雨で川があふれるおそれがあります。",
    nuance: "Used for warnings or risk statements.",
  },
  {
    title: "〜っぱなし",
    usage: "Vます-stem + っぱなし",
    meaning: "leave as-is / left in that state",
    example: "ドアを開けっぱなしにしないでください。",
    nuance: "Implies carelessness or negligence.",
  },
  {
    title: "〜に違いない",
    usage: "Plain form + に違いない",
    meaning: "must be / I am sure that…",
    example: "あの明かりは駅に違いない。",
    nuance: "Strong conviction based on some evidence.",
  },
  {
    title: "〜ようにしている",
    usage: "Vる / Vない + ようにしている",
    meaning: "make an effort to / try to keep doing",
    example: "毎日日本語で日記を書くようにしています。",
    nuance: "Habit formation; ongoing effort.",
  },
  {
    title: "〜わけにはいかない",
    usage: "Vる + わけにはいかない",
    meaning: "cannot (due to social/moral reasons)",
    example: "今日はテストなので、遅刻するわけにはいかない。",
    nuance: "Speaker feels pressure or responsibility.",
  },
  {
    title: "〜最中に",
    usage: "Nの / Vている + 最中に",
    meaning: "in the middle of / right when",
    example: "食事の最中に電話が鳴った。",
    nuance: "Unexpected interruption.",
  },
];

const tasks = [
  { title: "Shadow 10 lines aloud", meta: "Listening + pronunciation", category: "listening" },
  { title: "Review 10 vocabulary", meta: "Choose from the vocab explorer", category: "vocab" },
  { title: "Write 3 example sentences", meta: "Use today’s grammar", category: "grammar" },
  { title: "Skim one news paragraph", meta: "Under 5 minutes, no dictionary", category: "reading" },
  { title: "Kanji flash (5)", meta: "On/kun + one sentence", category: "kanji" },
  { title: "Speak for 90 seconds", meta: "Record yourself explaining your day", category: "speaking" },
];

const focusIdeas = [
  ["〜たばかり", "〜ようにしている", "〜わけではない"],
  ["〜おそれがある", "〜に違いない", "〜うちに"],
  ["〜わけにはいかない", "〜ように言う", "〜っぱなし"],
];

const taskList = document.getElementById("task-list");
const targetInput = document.getElementById("target");
const targetMinutes = document.getElementById("target-minutes");
const wordsReviewed = document.getElementById("words-reviewed");
const grammarReviewed = document.getElementById("grammar-reviewed");
const vocabGrid = document.getElementById("vocab-grid");
const categoryFilter = document.getElementById("category-filter");
const posFilter = document.getElementById("pos-filter");
const searchInput = document.getElementById("search");
const grammarList = document.getElementById("grammar-list");
const promptLabel = document.getElementById("prompt-label");
const promptQuestion = document.getElementById("prompt-question");
const promptAnswer = document.getElementById("prompt-answer");
const revealBtn = document.getElementById("reveal");
const nextBtn = document.getElementById("next");
const toggleButtons = document.querySelectorAll(".toggle-btn");
const streakValue = document.getElementById("streak-value");
const heroFocusList = document.getElementById("focus-list");
const heroFocusTopic = document.getElementById("focus-topic");
const scrollToPractice = document.getElementById("scroll-to-practice");
const startSession = document.getElementById("start-session");

let mode = "vocab";
let streak = 0;
let wordsCount = 0;
let grammarCount = 0;

function renderTasks() {
  taskList.innerHTML = "";
  tasks.forEach((task, index) => {
    const wrapper = document.createElement("label");
    wrapper.className = "task-card";
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = JSON.parse(localStorage.getItem(`task-${index}`)) || false;
    if (checkbox.checked) {
      wrapper.classList.add("checked");
    }
    checkbox.addEventListener("change", () => {
      localStorage.setItem(`task-${index}`, checkbox.checked);
      wrapper.classList.toggle("checked", checkbox.checked);
    });

    const body = document.createElement("div");
    const title = document.createElement("p");
    title.className = "task-title";
    title.textContent = task.title;
    const meta = document.createElement("p");
    meta.className = "task-meta";
    meta.textContent = task.meta;

    body.appendChild(title);
    body.appendChild(meta);
    wrapper.appendChild(checkbox);
    wrapper.appendChild(body);
    taskList.appendChild(wrapper);
  });
}

function updateTargetMinutes() {
  targetMinutes.textContent = targetInput.value;
  localStorage.setItem("target-minutes", targetInput.value);
}

function hydrateTarget() {
  const stored = localStorage.getItem("target-minutes");
  if (stored) {
    targetInput.value = stored;
  }
  targetMinutes.textContent = targetInput.value;
}

function getUniqueCategories() {
  return ["All categories", ...new Set(vocab.map((v) => v.category))];
}

function renderFilters() {
  const categories = getUniqueCategories();
  categoryFilter.innerHTML = "";
  categories.forEach((cat) => {
    const option = document.createElement("option");
    option.value = cat === "All categories" ? "all" : cat;
    option.textContent = cat;
    categoryFilter.appendChild(option);
  });
}

function renderVocab() {
  const term = searchInput.value.toLowerCase();
  const category = categoryFilter.value;
  const pos = posFilter.value;

  vocabGrid.innerHTML = "";
  vocab
    .filter(
      (item) =>
        (category === "all" || item.category === category) &&
        (pos === "all" || item.pos === pos) &&
        (item.word.toLowerCase().includes(term) ||
          item.reading.includes(term) ||
          item.meaning.toLowerCase().includes(term))
    )
    .forEach((item) => {
      const card = document.createElement("article");
      card.className = "vocab-card";

      const header = document.createElement("div");
      header.className = "vocab-header";

      const word = document.createElement("div");
      word.className = "word";
      word.textContent = item.word;

      const tag = document.createElement("span");
      tag.className = "tag";
      tag.textContent = item.pos;

      header.appendChild(word);
      header.appendChild(tag);

      const reading = document.createElement("p");
      reading.className = "reading";
      reading.textContent = item.reading;

      const meaning = document.createElement("p");
      meaning.className = "meaning";
      meaning.textContent = item.meaning;

      const categoryTag = document.createElement("span");
      categoryTag.className = "tag";
      categoryTag.textContent = item.category;

      card.appendChild(header);
      card.appendChild(reading);
      card.appendChild(meaning);
      card.appendChild(categoryTag);
      vocabGrid.appendChild(card);
    });
}

function renderGrammar() {
  grammarList.innerHTML = "";
  grammarPatterns.forEach((pattern) => {
    const card = document.createElement("article");
    card.className = "grammar-card";

    const title = document.createElement("p");
    title.className = "grammar-title";
    title.textContent = pattern.title;

    const usage = document.createElement("span");
    usage.className = "pill";
    usage.textContent = pattern.usage;

    const nuance = document.createElement("span");
    nuance.className = "pill warning";
    nuance.textContent = pattern.nuance;

    const example = document.createElement("span");
    example.className = "pill info";
    example.textContent = pattern.example;

    const meaning = document.createElement("p");
    meaning.className = "meaning";
    meaning.textContent = pattern.meaning;

    card.appendChild(title);
    card.appendChild(usage);
    card.appendChild(meaning);
    card.appendChild(nuance);
    card.appendChild(example);
    grammarList.appendChild(card);
  });
}

function getRandomPrompt() {
  if (mode === "vocab") {
    const item = vocab[Math.floor(Math.random() * vocab.length)];
    return {
      label: "Vocabulary",
      question: `${item.word} (${item.reading})`,
      answer: `${item.meaning} — ${item.pos}, ${item.category}`,
      countKey: "vocab",
    };
  }
  const pattern = grammarPatterns[Math.floor(Math.random() * grammarPatterns.length)];
  return {
    label: "Grammar",
    question: `${pattern.title} — ${pattern.usage}`,
    answer: `${pattern.meaning}\n例: ${pattern.example}`,
    countKey: "grammar",
  };
}

function incrementCounts(type) {
  if (type === "vocab") {
    wordsCount = Math.min(30, wordsCount + 1);
    wordsReviewed.textContent = `${wordsCount}/30`;
  }
  if (type === "grammar") {
    grammarCount = Math.min(10, grammarCount + 1);
    grammarReviewed.textContent = `${grammarCount}/10`;
  }
}

function showPrompt() {
  const prompt = getRandomPrompt();
  promptLabel.textContent = prompt.label;
  promptQuestion.textContent = prompt.question;
  promptAnswer.textContent = "Say it aloud, then tap reveal.";
  promptAnswer.dataset.answer = prompt.answer;
}

function revealAnswer() {
  if (promptAnswer.dataset.answer) {
    promptAnswer.textContent = promptAnswer.dataset.answer;
  }
}

function setMode(newMode) {
  mode = newMode;
  toggleButtons.forEach((btn) => btn.classList.toggle("active", btn.dataset.mode === mode));
  promptLabel.textContent = mode === "vocab" ? "Vocabulary" : "Grammar";
  promptQuestion.textContent = "Press “Next prompt” to begin";
  promptAnswer.textContent = "Answer will appear here";
}

function handleCorrect() {
  streak += 1;
  if (streak >= 2) {
    incrementCounts(mode === "vocab" ? "vocab" : "grammar");
    streak = 0;
  }
  streakValue.textContent = streak;
}

function setFocus() {
  const random = focusIdeas[Math.floor(Math.random() * focusIdeas.length)];
  const main = random[0];
  heroFocusTopic.textContent = `${main} ・ focus set`;
  heroFocusList.innerHTML = "";
  random.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    heroFocusList.appendChild(li);
  });
}

function scrollToPracticeSection() {
  document.getElementById("practice").scrollIntoView({ behavior: "smooth" });
}

function setSessionButton() {
  startSession.addEventListener("click", () => {
    targetInput.value = Math.max(parseInt(targetInput.value, 10), 15);
    updateTargetMinutes();
    scrollToPracticeSection();
  });
}

targetInput.addEventListener("input", updateTargetMinutes);
categoryFilter.addEventListener("change", renderVocab);
posFilter.addEventListener("change", renderVocab);
searchInput.addEventListener("input", renderVocab);
revealBtn.addEventListener("click", revealAnswer);
nextBtn.addEventListener("click", () => {
  handleCorrect();
  showPrompt();
});
toggleButtons.forEach((btn) =>
  btn.addEventListener("click", () => {
    setMode(btn.dataset.mode);
    streak = 0;
    streakValue.textContent = streak;
  })
);
scrollToPractice.addEventListener("click", scrollToPracticeSection);

hydrateTarget();
renderTasks();
renderFilters();
renderVocab();
renderGrammar();
setMode("vocab");
showPrompt();
setFocus();
setSessionButton();
