from manim import *


class Urafsin(Scene):
    def construct(self):
        # 1 сцена(пример с окружностью)
        # Пример
        zad = MathTex(r'x_n = \frac{1}{n} + sin(\frac{\pi n}{3})')

        # График
        axes = Axes(
            x_range=[-1, 1, 1],
            y_range=[-1, 1, 1],
            x_length=6,
            y_length=6,
            x_axis_config={"color": WHITE},
            tips=False
        )

        axes.shift(RIGHT * 3)

        #Круг с
        center_point = ORIGIN + RIGHT*3
        circle = Circle(
            radius=1.75,
            color=WHITE
        ).move_to(center_point)
        dot = Dot(center_point, color=WHITE)


        angle_tracker = ValueTracker(0)

        line = always_redraw(lambda: Line(
            start=center_point,
            end=center_point + RIGHT * circle.radius,
            color=RED
        ).rotate(
            angle_tracker.get_value(),
            about_point=center_point
        ))

        circle_line = VGroup(line, circle)




        # Формулы точек
        text1 = MathTex('n = 6k-5')
        text2 = MathTex('n = 6k-4')
        text3 = MathTex('n = 6k-3')
        text4 = MathTex('n = 6k-2')
        text5 = MathTex('n = 6k-1')
        text6 = MathTex('n = 6k-0')


        text2.shift(DOWN*0.7)
        text3.shift(DOWN*1.45)
        text4.shift(DOWN*2.2)
        text5.shift(DOWN*2.95)
        text6.shift(DOWN*3.65)

        tochki = VGroup(text1, text2, text3, text4, text5, text6)

        tochki.shift(LEFT*3, UP*0.8)




        self.wait(1)
        self.play(Write(zad))
        self.wait(1)
        self.play(zad.animate.shift(LEFT*3, UP*2))
        self.play(Write(axes), Write(circle))
        self.play(Write(tochki))
        self.play(Write(line))
        self.wait(1)

        self.play(
            angle_tracker.animate.set_value(PI / 3),
            run_time=1.5,
            rate_func=smooth
        )

        self.play(Wiggle(text1, scale_value=1.3, n_wiggles=8, run_time=2))
        self.wait(0.5)

        self.play(
            angle_tracker.animate.set_value((2*PI) / 3),
            run_time=1.5,
            rate_func=smooth
        )

        self.play(Wiggle(text2, scale_value=1.3, n_wiggles=8, run_time=2))
        self.wait(0.5)

        self.play(
            angle_tracker.animate.set_value(PI),
            run_time=1.5,
            rate_func=smooth
        )

        self.play(Wiggle(text3, scale_value=1.3, n_wiggles=8, run_time=2))
        self.wait(0.5)

        self.play(
            angle_tracker.animate.set_value((4 * PI) / 3),
            run_time=1.5,
            rate_func=smooth
        )

        self.play(Wiggle(text4, scale_value=1.3, n_wiggles=8, run_time=2))
        self.wait(0.5)

        self.play(
            angle_tracker.animate.set_value((5 * PI) / 3),
            run_time=2,
            rate_func=smooth
        )

        self.play(Wiggle(text5, scale_value=1.3, n_wiggles=8, run_time=2))
        self.wait(0.5)

        self.play(
            angle_tracker.animate.set_value(2 * PI),
            run_time=1.5,
            rate_func=smooth
        )

        self.play(Wiggle(text6, scale_value=1.3, n_wiggles=8, run_time=2))
        self.wait(0.5)
        self.play(Unwrite(zad), Unwrite(axes), Unwrite(circle_line), Unwrite(tochki))
        self.wait()


        # 2 сцена(решение с последовательностью)

class Urafsin2(Scene):
    def construct(self):

        text1_2 = MathTex(r'\frac{1}{6k-5} + \frac{\sqrt{3}}{2} \approx \frac{1}{6k-5} + 0,85')
        text1_2_1 = MathTex(r'1,85; 0,99; ... \to \frac{\sqrt{3}}{2}')
        text1_2_1.shift(RIGHT*3)

        text2_2 = MathTex(r'\frac{1}{6k-4} + \frac{\sqrt{3}}{2} \approx \frac{1}{6k-4} + 0,85')
        text2_2_1 = MathTex(r'1,35; 0,975; ... \to \frac{\sqrt{3}}{2}')
        text2_2_1.shift(RIGHT*3.2)

        text3_2 = MathTex(r'\frac{1}{6k-3}')
        text3_2_1 = MathTex(r'0,(3); 0,(1); ... \to 0')
        text3_2.shift(DOWN*2)
        text3_2_1.shift(DOWN*2)

        gr_tx1 = VGroup(text1_2, text1_2_1, text2_2, text2_2_1, text3_2, text3_2_1)


        text4_2 = MathTex(r'\frac{1}{6k-2} - \frac{\sqrt{3}}{2} \approx \frac{1}{6k-2} - 0,85')
        text4_2_1 = MathTex(r'-0,6; -0,75; ... \to -\frac{\sqrt{3}}{2}')
        text4_2_1.shift(RIGHT*3.2)

        text5_2 = MathTex(r'\frac{1}{6k-1} - \frac{\sqrt{3}}{2} \approx \frac{1}{6k-1} - 0,85')
        text5_2_1 = MathTex(r'-0,65; -0,75...; ... \to -\frac{\sqrt{3}}{2}')
        text5_2_1.shift(RIGHT * 3.4)

        text6_2 = MathTex(r'\frac{1}{6k}')
        text6_2_1 = MathTex(r'0,16...; 0,083...; ... \to 0')
        text6_2.shift(DOWN * 2)
        text6_2_1.shift(DOWN * 2)

        gr_tx2 = VGroup(text4_2, text4_2_1, text5_2, text5_2_1, text6_2, text6_2_1)


        self.play(Write(text1_2))
        self.play(text1_2.animate.shift(LEFT*3))
        self.play(Write(text1_2_1))
        self.play(text1_2.animate.shift(UP*2), text1_2_1.animate.shift(UP*2))

        self.play(Write(text2_2))
        self.play(text2_2.animate.shift(LEFT*3))
        self.play(Write(text2_2_1))


        self.play(Write(text3_2))
        self.play(text3_2.animate.shift(LEFT * 5.6))
        self.play(Write(text3_2_1))
        self.play(text3_2_1.animate.shift(LEFT * 2.6))

        self.wait(1)
        self.play(FadeOut(gr_tx1))
        self.wait(1)

        self.play(Write(text4_2))
        self.play(text4_2.animate.shift(LEFT*3))
        self.play(Write(text4_2_1))
        self.play(text4_2.animate.shift(UP*2), text4_2_1.animate.shift(UP*2))

        self.play(Write(text5_2))
        self.play(text5_2.animate.shift(LEFT * 3.2))
        self.play(Write(text5_2_1))

        self.play(Write(text6_2))
        self.play(text6_2.animate.shift(LEFT * 6))
        self.play(Write(text6_2_1))
        self.play(text6_2_1.animate.shift(LEFT * 3))

        self.wait(1)
        self.play(Unwrite(gr_tx2))
        self.wait(1)

# 3 сцена прямая и результат
class Urafsin3(Scene):
    def construct(self):
        # 1. Создаем числовую прямую
        number_line = NumberLine(
            x_range=[-1, 2, 1],  # [минимум, максимум, шаг]
            length=13, # длина прямой на экране
            include_ticks=False,
            color=BLUE,  # цвет линии
        )

        # 2. Определяем координаты точек, которые нужно отметить
        points_to_mark = [-0.85, -0.6, 0, 0.3, 0.85, 1.85]

        # Группа, в которую соберем все точки и их подписи
        dots_group = VGroup()

        for x in points_to_mark:
            # Превращаем числовое значение на прямой в 3D-координату Manim
            point_coord = number_line.n2p(x)

            # Создаем точку
            dot = Dot(point_coord, color=RED, radius=0.08)

            # (Опционально) Создаем подпись над точкой
            label = MathTex(f"{x}").next_to(dot, UP, buff=0.2).scale(0.6)
            label.set_color(YELLOW)

            dots_group.add(dot, label)

        hatches = VGroup()
        hatches2 = VGroup()

        x1 = number_line.n2p(-0.85)[0]
        x2 = number_line.n2p(-0.6)[0]


        x1_2 = number_line.n2p(0)[0]
        x2_2 = number_line.n2p(0.3)[0]


        x1_3 = number_line.n2p(0.85)[0]
        x2_3 = number_line.n2p(1.85)[0]

        y = number_line.get_y()
        step = 0.12
        hatch_length = 0.18

        x = x1
        while x <= x2:
            hatch = Line(
                [x - hatch_length / 2, y - hatch_length / 2, 0],
                [x + hatch_length / 2, y + hatch_length / 2, 0],
                color=YELLOW,
                stroke_width=3
            )
            hatches.add(hatch)
            x += step

        x = x1_2
        while x <= x2_2:
            hatch2 = Line(
                [x - hatch_length / 2, y - hatch_length / 2, 0],
                [x + hatch_length / 2, y + hatch_length / 2, 0],
                color=YELLOW,
                stroke_width=3
            )
            hatches2.add(hatch2)
            x += step



        x = x1_3
        while x <= x2_3:
            hatch2 = Line(
                [x - hatch_length / 2, y - hatch_length / 2, 0],
                [x + hatch_length / 2, y + hatch_length / 2, 0],
                color=YELLOW,
                stroke_width=3
            )
            hatches2.add(hatch2)
            x += step

        to1 = MathTex(r'\leftarrow')
        to2 = MathTex(r'\leftarrow')
        to3 = MathTex(r'\leftarrow')
        to1.shift(DOWN*0.5, LEFT*5.4)
        to2.shift(DOWN*0.5, LEFT*1.6)
        to3.shift(DOWN*0.5, RIGHT*3.7)


        res = MathTex(r'\overline{\lim{x_n}} = \frac{\sqrt{3}}{2}; \underline{\lim{x_n}} = -\frac{\sqrt{3}}{2}')
        res2 = MathTex(r'\sup{x_n} = 1 + \frac{\sqrt{3}}{2}; \inf{x_n} = -\frac{\sqrt{3}}{2}')
        res.shift(DOWN*1.5)
        res2.shift(DOWN*3)

        thanks = Text('Thanks for watching!', font_size=30)

        # 3. Анимация появления на сцене
        self.play(Write(number_line))
        self.wait(0.5)

        # Точки появляются с эффектом увеличения (GrowFromCenter)
        self.play(
            AnimationGroup(
                *[GrowFromCenter(obj) for obj in dots_group],
                lag_ratio=0.3
            ),
            run_time=2
        )
        self.wait(2)
        self.play(Create(hatches), Create(hatches2), run_time=2)
        self.wait(2)
        self.play(Write(to1), Write(to2), Write(to3))
        self.wait(1)
        self.play(Write(res), Write(res2))
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)
        self.play(Write(thanks))
        self.wait(2)
        self.play(Unwrite(thanks))
        self.wait(0.5)

