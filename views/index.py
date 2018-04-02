from flask import Flask, Blueprint, render_template, request, session

index = Blueprint("index", __name__, template_folder="templates")

@index.route("/index",methods=["GET"])
def myindex():
    return "INDEX"

