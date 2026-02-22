alias d='python ~/tt.py'
alias d='python ~/tt.py'
python ~/web_app.py &
alias stop='pkill -f web_app.py && echo "🔴 Сервер зупинено"'
alias status='ps aux | grep web_app.py | grep -v grep && echo "🟢 Сервер працює" || echo "⚪ Сервер вимкнено"'

