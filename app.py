from flask import *
import textsummary
import audiosummary
import video

app=Flask(__name__)


@app.route("/")
def demo():
    return render_template("index.html")

@app.route("/upload")
def upload():
    return render_template("file_upload1.html")

@app.route("/upload1")
def upload1():
    return render_template("file_upload2.html")

@app.route("/upload2")
def upload2():
    return render_template("file_upload3.html")

@app.route("/summarize",methods=["POST"])
def summarize():
    global file
    f=request.files['file']
    file=f.filename
    f.save(file)
    textsummary.generate_summary(file)
    filename=file.split(".")[0]+"summary.txt"
    return send_file(filename,as_attachment=True, cache_timeout=0)
    

@app.route("/audiosummarize",methods=["POST"])
def audiosummarize():
   global file
   f=request.files['file']
   file=f.filename
   f.save(file)
   audiosummary.get_large_audio_transcription(file)
   filename="audiosummary.txt"
   return send_file(filename,as_attachment=True, cache_timeout=0)

@app.route("/audiotextsummarize",methods=["POST"])
def audio():
   filename="audio.txt"
   return send_file(filename,as_attachment=True, cache_timeout=0)
    
@app.route("/videosummarize",methods=["POST"])
def videosummarize():
   global file
   f=request.files['file']
   file=f.filename
   f.save(file)
   video.videosummary(file)
   filename="videosummary.txt"
   return send_file(filename,as_attachment=True, cache_timeout=0)

@app.route("/videotextsummarize",methods=["POST"])
def video1():
   filename="video.txt"
   return send_file(filename,as_attachment=True, cache_timeout=0)
    
if __name__ == "__main__":
    app.run(debug=True)
