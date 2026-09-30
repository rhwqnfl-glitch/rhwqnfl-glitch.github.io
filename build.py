import os, html
EMAIL = "rhwqnfl@gmail.com"   # 공개 문의 이메일로 교체
BIZ = "인생개발자"
REP = "장지훈"
BIZNO = "116-08-85770"
UPDATED = "2026-09-30"

APPS = [
 dict(slug="luck-enchant", name="운빨강화로그", icon="luck-enchant.png",
      tag="운에 맡기는 장비 강화 시뮬레이션 게임",
      desc="대장간에서 장비를 강화하고 주문서를 모아 운을 시험해 보는 캐주얼 게임입니다. 강화 결과와 기록을 남기고, 상인에게 장비를 사고팔며 골드를 벌 수 있습니다.",
      feats=["대장간 강화와 주문서 사용","상인 거래와 의뢰","강화 기록(운 순위) 확인"],
      shots=["luck_t7_1_main.png","luck_t7_2_smith.png","luck_t7_3_merchant.png","luck_t7_4_scribe.png","luck_t7_5_bag.png"],
      privacy=["광고: 보상형 광고 제공을 위해 Google AdMob을 사용하며, AdMob이 광고 식별자(광고 ID) 등 기기 정보를 수집·이용할 수 있습니다. 자세한 내용은 Google 개인정보처리방침을 따릅니다.",
               "게임 진행 데이터(골드, 장비, 기록 등)는 기기 내부에만 저장되며 개발자 서버로 전송되지 않습니다.",
               "이름, 연락처, 위치 등 개인 식별 정보는 수집하지 않습니다."],
      extra="광고 ID는 기기 설정에서 초기화하거나 맞춤 광고를 끌 수 있습니다."),
 dict(slug="lotto-log", name="로또로그", icon="lotto-log.png",
      tag="로또 번호 생성과 구매 기록 앱",
      desc="로또 번호를 생성하고 구매 내역을 기록해 두며, 회차별 당첨 번호와 비교해 볼 수 있는 앱입니다. 추첨 시간에 맞춘 알림을 받을 수 있습니다.",
      feats=["번호 생성","구매 내역 기록","당첨 번호 확인","추첨 알림"], shots=["lotto_t7_1_main.png","lotto_t7_3_scroll.png","lotto_t7_5_settings.png"],
      privacy=["구매 내역과 설정은 기기 내부에만 저장되며 개발자 서버로 전송되지 않습니다.",
               "당첨 번호 조회를 위해 동행복권 공개 서버에 회차 번호 정보를 요청합니다. 이 과정에서 개인정보는 전송되지 않습니다.",
               "알림 기능을 위해 알림 권한과 부팅 시 알림 재등록 권한을 사용합니다.",
               "이름, 연락처, 위치 등 개인 식별 정보는 수집하지 않습니다."],
      extra="본 앱은 동행복권과 무관한 개인 개발 앱이며, 번호 생성 결과는 당첨을 보장하지 않습니다."),
 dict(slug="sea-log", name="바다로그", icon="sea-log.png",
      tag="바다 날씨·물때·낚시 정보 앱",
      desc="지도에서 지점을 골라 바다 날씨, 물때, 관측 정보, 미세먼지 등을 확인하는 앱입니다. 공공데이터를 바탕으로 정보를 보여 줍니다.",
      feats=["지점별 바다 날씨와 관측 정보","물때와 조석 정보","낚시 지수","대기질(미세먼지) 정보"], shots=["sea_t7_1_tide.png","sea_t7_2_scroll.png","sea_t7_4_map.png"],
      privacy=["위치: 내 주변 관측소와 날씨를 찾기 위해 기기의 대략적·정확한 위치 정보를 사용합니다. 위치 정보는 기기 안에서만 사용되며 외부로 전송되거나 저장되지 않습니다.",
               "관측소 지도는 카카오맵(Kakao)을 이용해 표시하며, 지도 표시 과정에서 카카오가 접속 정보(IP 등)를 처리할 수 있습니다. 자세한 내용은 카카오 개인정보처리방침을 따릅니다.",
               "정보 조회를 위해 공공데이터포털(기상청, 해양수산부, 한국환경공단 등)의 공개 API에 요청을 보냅니다.",
               "설정과 즐겨찾기 등은 기기 내부에만 저장됩니다.",
               "알림 기능을 위해 알림 및 정확한 알람 권한을 사용할 수 있습니다."],
      extra="제공되는 정보는 참고용이며, 안전과 관련된 판단은 공식 기상 특보 등을 확인해 주세요."),
]

CSS = """:root{--bg:#f7f7f5;--fg:#1c1c1a;--muted:#6b6b66;--card:#fff;--line:#e4e4df;--accent:#2f5d50}
@media(prefers-color-scheme:dark){:root{--bg:#161715;--fg:#ececE8;--muted:#9a9a93;--card:#1f201e;--line:#2c2d2a;--accent:#7fbfa8}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.7 -apple-system,"Apple SD Gothic Neo","Noto Sans KR",sans-serif}
.wrap{max-width:760px;margin:0 auto;padding:0 16px}
header{border-bottom:1px solid var(--line)}header .wrap{display:flex;justify-content:space-between;align-items:center;height:56px}
header a{color:var(--fg);text-decoration:none}.brand{font-weight:700}nav a{margin-left:16px;color:var(--muted)}
h1{font-size:1.7rem;margin:40px 0 8px}h2{font-size:1.15rem;margin:32px 0 8px}p.lead{color:var(--muted);margin:0 0 24px}
.card{display:flex;gap:16px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px;margin:12px 0;color:inherit;text-decoration:none}
.card img,.ph{width:64px;height:64px;border-radius:14px;flex:none;object-fit:cover;background:var(--line)}
.card b{display:block}.card span{color:var(--muted);font-size:.92rem}
ul{padding-left:20px}a{color:var(--accent)}
.shots{display:flex;gap:10px;overflow-x:auto;padding-bottom:8px}.shots img{height:320px;border-radius:10px;border:1px solid var(--line)}
table{border-collapse:collapse;width:100%}td{border-bottom:1px solid var(--line);padding:10px 4px;vertical-align:top}td:first-child{color:var(--muted);width:130px}
footer{border-top:1px solid var(--line);margin-top:56px;padding:24px 0;color:var(--muted);font-size:.88rem}"""

def page(path, title, body, depth):
    r = "../"*depth
    h = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><link rel="stylesheet" href="{r}style.css"></head><body>
<header><div class="wrap"><a class="brand" href="{r}">{BIZ}</a><nav><a href="{r}">앱</a><a href="{r}contact/">문의</a></nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap">상호 {BIZ} · 대표 {REP} · 사업자등록번호 {BIZNO} · 문의 <a href="mailto:{EMAIL}">{EMAIL}</a><br>© {BIZ}</div></footer></body></html>"""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w", encoding="utf-8").write(h)

open("style.css","w").write(CSS)


def write_privacy(a, path, depth):
    items = "".join(f"<li>{p}</li>" for p in a["privacy"])
    ads = ""
    if a["slug"] == "luck-enchant":
        ads = '<p>맞춤 광고는 기기의 <b>설정 &gt; Google &gt; 광고</b>에서 광고 ID를 삭제하거나 맞춤 광고를 끌 수 있습니다.</p>'
    page(path, f'{a["name"]} 개인정보처리방침 - {BIZ}', f"""<h1>{a["name"]} 개인정보처리방침</h1>
<p class="lead">시행일 {UPDATED}</p>
<p>{BIZ}(대표 {REP}, 이하 "개발자")는 {a["name"]} 앱(이하 "앱") 이용자의 개인정보를 소중히 다루며, 관련 법령에 따라 아래와 같이 처리합니다.</p>
<h2>1. 수집·이용하는 정보</h2><ul>{items}</ul><p>{a["extra"]}</p>{ads}
<h2>2. 회원가입 및 계정</h2><p>앱은 회원가입이나 로그인을 요구하지 않으며, 개발자는 이용자를 식별할 수 있는 정보를 서버에 보관하지 않습니다.</p>
<h2>3. 보관 및 이용 기간</h2><p>앱 데이터는 이용자의 기기에만 저장되며, 앱을 삭제하면 함께 삭제됩니다. 외부 서비스(광고, 지도, 공공데이터 등)가 처리하는 정보는 각 서비스의 정책에 따른 기간 동안 보관됩니다.</p>
<h2>4. 제3자 제공 및 국외 이전</h2><p>개발자는 이용자의 개인정보를 별도로 수집하거나 제3자에게 제공·판매하지 않습니다. 위에 적은 외부 서비스 사업자(Google, 카카오 등)는 자체 정책에 따라 정보를 국외 서버를 포함한 곳에서 처리할 수 있습니다.</p>
<h2>5. 이용자의 권리</h2><p>이용자는 기기 설정에서 권한(알림, 위치 등)을 언제든 허용하거나 철회할 수 있고, 앱 삭제로 저장된 데이터를 지울 수 있습니다. 개인정보 열람·삭제 등 요청은 아래 문의처로 보내 주세요.</p>
<h2>6. 아동의 개인정보</h2><p>앱은 만 14세 미만 아동을 대상으로 하지 않으며, 아동의 개인정보를 알면서 수집하지 않습니다.</p>
<h2>7. 안전성 확보</h2><p>개발자는 개인정보를 서버에 저장하지 않으며, 앱 통신은 가능한 범위에서 암호화(HTTPS)된 연결을 사용합니다.</p>
<h2>8. 문의 및 개인정보 보호책임자</h2><p>책임자: {REP} · 상호: {BIZ}<br>이메일: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>9. 방침의 변경</h2><p>방침이 바뀌면 이 페이지에 공지하며, 시행일을 갱신합니다.</p>""", depth)

cards = ""
for a in APPS:
    ic = f'<img src="assets/{a["icon"]}" alt="">' if a["icon"] else '<div class="ph"></div>'
    cards += f'<a class="card" href="apps/{a["slug"]}/">{ic}<div><b>{a["name"]}</b><span>{a["tag"]}</span></div></a>'
page("index.html", f"{BIZ} - 모바일 앱 개발", f"""<h1>{BIZ}</h1>
<p class="lead">일상에서 쓰는 가벼운 모바일 앱을 만드는 개인 개발 사업자입니다.</p>
<h2>앱</h2>{cards}
<h2>회사 정보</h2><table>
<tr><td>상호</td><td>{BIZ} (insaeng developer)</td></tr><tr><td>대표자</td><td>{REP}</td></tr>
<tr><td>사업자등록번호</td><td>{BIZNO}</td></tr><tr><td>업태 / 종목</td><td>소매업 / 전자상거래 소매 중개업</td></tr>
<tr><td>문의</td><td><a href="mailto:{EMAIL}">{EMAIL}</a></td></tr></table>""", 0)

for a in APPS:
    ic = f'<img src="../../assets/{a["icon"]}" alt="" style="width:88px;height:88px;border-radius:20px">' if a["icon"] else ""
    shots = '<h2>스크린샷</h2><div class="shots">'+"".join(f'<img src="../../assets/{s}" alt="">' for s in a["shots"])+"</div>" if a["shots"] else ""
    feats = "".join(f"<li>{f}</li>" for f in a["feats"])
    page(f'apps/{a["slug"]}/index.html', f'{a["name"]} - {BIZ}', f"""{ic}<h1>{a["name"]}</h1><p class="lead">{a["tag"]}</p>
<p>{a["desc"]}</p><h2>주요 기능</h2><ul>{feats}</ul>{shots}
<h2>정책</h2><p><a href="../../privacy/{a["slug"]}/">개인정보처리방침</a> · <a href="../../contact/">문의하기</a></p>""", 2)
    write_privacy(a, f'privacy/{a["slug"]}/index.html', 2)
    if a["slug"] == "luck-enchant":
        write_privacy(a, "privacy.html", 0)  # 기존 주소(/privacy.html) 유지

page("contact/index.html", f"문의 - {BIZ}", f"""<h1>문의</h1><p class="lead">앱 이용 중 문의, 오류 제보, 제휴 문의를 받습니다.</p>
<table><tr><td>이메일</td><td><a href="mailto:{EMAIL}">{EMAIL}</a></td></tr>
<tr><td>상호</td><td>{BIZ}</td></tr><tr><td>대표자</td><td>{REP}</td></tr><tr><td>사업자등록번호</td><td>{BIZNO}</td></tr></table>""", 1)
