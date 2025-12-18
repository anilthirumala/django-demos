from flask import Flask, render_template, request, redirect
import crud

app = Flask(__name__)

@app.route("/")
def list_products():
    products = crud.get_all_products()
    return render_template("list.html", products=products)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        crud.create_product(
            request.form["name"],
            float(request.form["price"]),
            request.form["description"]
        )
        return redirect("/")
    return render_template("create.html")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    product = crud.get_product(id)
    if request.method == "POST":
        crud.update_product(
            id,
            request.form["name"],
            float(request.form["price"]),
            request.form["description"]
        )
        return redirect("/")
    return render_template("update.html", product=product)

@app.route("/delete/<int:id>")
def delete(id):
    crud.delete_product(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)