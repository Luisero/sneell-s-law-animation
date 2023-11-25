from manim import *

class Snell(Scene):
    def construct(self):
        text1 = Text('Demonstração da lei de Snell',
                     color=LIGHT_PINK,
                     font_size=40)
        
        latex_temp = TexTemplate()
        latex_temp.add_to_preamble(r"\usepackage{tikz}")

        latex_temp.add_to_preamble(r'''
    
    \usepackage{xcolor}
    \usetikzlibrary{arrows,shapes,positioning}
\usetikzlibrary{decorations.markings}
\tikzstyle arrowstyle=[scale=1]
\tikzstyle directed=[postaction={decorate,decoration={markings,
    mark=at position .65 with {\arrow[arrowstyle]{stealth}}}}]
\tikzstyle reverse directed=[postaction={decorate,decoration={markings,
    mark=at position .65 with {\arrowreversed[arrowstyle]{stealth};}}}]
''')
        
        

        text2 = Tex(r'''\begin{tikzpicture}

    % define coordinates
    \coordinate (O) at (0,0) ;
    \coordinate (A) at (0,4) ;
    \coordinate (B) at (0,-4) ;
    
    % media
    \fill[blue!25!,opacity=.3] (-4,0) rectangle (4,4);
    \fill[blue!60!,opacity=.3] (-4,0) rectangle (4,-4);
    \node[right] at (2,2) {Air};
    \node[left] at (-2,-2) {Water};

    % axis
    \draw[dash pattern=on5pt off3pt] (A) -- (B) ;

    % rays
    \draw[red,ultra thick,reverse directed] (O) -- (130:5.2);
    \draw[blue,directed,ultra thick] (O) -- (-70:4.24);

    % angles
    \draw (0,1) arc (90:130:1);
    \draw (0,-1.4) arc (270:290:1.4) ;
    \node[] at (280:1.8)  {$\theta_{2}$};
    \node[] at (110:1.4)  {$\theta_{1}$};
\end{tikzpicture}''', tex_template=latex_temp, fill_opacity=0, stroke_width=2, color=WHITE)
        
        self.play(Write(text1), runtime=5)
        self.wait(3)
        self.remove(text1)
        self.play(Write(text2))
        self.wait(4)
        