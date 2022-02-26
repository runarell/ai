# 플라스크 모듈 (서버 통제) 불러오기
from flask import Flask, render_template, request
from vsearch import search4letters
app = Flask(__name__)  # Flask 객체 생성 APP변수명 할당
# 객체 생성시 생성자에 __name__ 파이썬 인터프린터가
# 제공하는 값, 현재 활성 모듈의 이름을 가진다.

# @ 데코레이터 decorator 장식자


# @app.route('/')        # 사이트 접근 주소
# def hello() -> "302":
#     return redirect("/entry")


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "찾은 결과 입니다."
    results = str(search4letters(phrase, letters))

    return render_template("results.html", the_phrase=phrase, the_letters=letters, the_title=title, the_results=results)
    # return str(search4letters("fjlkdsajlfd", "aeiou"))


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template("entry.html", the_title="글자 찾기 사이트 방문을 환영합니다! by 26이재원")


if __name__ == "__main__":
    app.run(debug=True)
# 로컬에서 테스트와 개발 할때는
# app.run(debug=True) 싱행이 되어야함
# 웹에서 배포시 실행하면 안된다.
# if __name__ == "__main__":
# 웹상에서는 실행을 막게 된다.
