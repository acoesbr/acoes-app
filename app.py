from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        entrada = request.form.get("valores")
        try:
            valores = [float(v.strip()) for v in entrada.split(",")]
            dobrados = [v * 2 for v in valores]
            resultado = f"Originais: {valores}<br>Com 100% de aumento: {dobrados}"
        except ValueError:
            resultado = "Erro: insira apenas números separados por vírgula."
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
