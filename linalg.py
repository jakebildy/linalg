import random
import io

from flask import Flask, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


app = Flask(__name__)





@app.route('/')
def plot():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]

    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'

    mainmenu = '''<html>
        <body bgcolor="#000000">
<h2 style="text-align: center;"><span style="color: #ffffff;"><strong>INTUITIVE&nbsp;🤔 LINEAR 📏 ALGEBRA&nbsp;💦</strong></span></h2>
<p style="text-align: center;"><span style="color: #ffffff;"><em>developed by Jake Bildy</em></span></p>
<p style="text-align: center;"><span style="color: #ffffff;">&nbsp;</span></p>
<p style="text-align: center;"><span style="color: #ffffff;"><img src="http://www.ipaomi.com/wp-content/uploads/2017/11/linear_algebra_span_plain.png" alt="" width="615" height="256" /></span></p>
<p style="text-align: center;"><span style="color: #ffffff;">&nbsp;</span></p>
<p style="text-align: center;"><span style="color: #ffffff;">To start, select a chapter:</span></p>
<p style="text-align: center;"><span style="color: #ffffff;">Linear Equations and Matrices</span></p>
<p style="text-align: center;"><span style="color: #ffffff;">Determinants</span></p>
<p style="text-align: center;"><span style="color: #ffffff;">Euclidean Vector Spaces</span></p>
<p style="text-align: center;"><span style="color: #ffffff;">General Vector Spaces</span></p>
<p style="text-align: center;"><span style="color: #ffffff;">Eigenvalues and Eigenvectors</span></p>
<p style="text-align: center;"><span style="color: #ffffff;">Inner Product Spaces</span></p>
<p style="text-align: center;"><span style="color: #ffffff;">Diagonalization and Quadratic Forms</span></p>
<p style="text-align: center;"><span style="color: #ffffff;">General Linear Transformations</span></p>
<p style="text-align: center;"><span style="color: #ffffff;">Numerical Methods</span></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><span style="color: #ffffff;">&nbsp;</span></p>
<p style="text-align: center;"><span style="color: #ffffff;">&nbsp;</span></p>
<p style="text-align: center;"><span style="color: #ffffff;">Or if you just want the answer key to this year's final, <a style="color: #ffffff;" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">click here</a>.</span></p>
</html>
        '''

    return mainmenu

if __name__ == '__main__':
    app.run(debug=True)