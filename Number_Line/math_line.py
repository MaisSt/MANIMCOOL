from click import group
from manim import *


class NumberLineArcExample(Scene):
    def construct(self):
        # 1. Создаем числовую прямую
        line = NumberLine(
            x_range=[-8, 8, 1],
            length=10,
            include_numbers=False
        )

        # 2. Получаем координаты точек
        start_point = line.n2p(-5)
        end_point = line.n2p(5)

        start_point2 = line.n2p(5)
        end_point2 = line.n2p(-3)

        start_point3 = line.n2p(5)
        end_point3 = line.n2p(-1)


        # 3. Создаем дуги между этими точками и перпендикуляров
        # angle определяет крутизну дуги (PI/3 — аккуратная дуга)
        arc = ArcBetweenPoints(
            start=start_point,
            end=end_point,
            angle=PI / -3,
            color= WHITE
        )

        arc2 = ArcBetweenPoints(
            start=start_point2,
            end=end_point2,
            angle=PI / 4,
            color=RED
        )

        arc3 = ArcBetweenPoints(
            start=start_point3,
            end=end_point3,
            angle=PI / -2,
            color=BLUE
        )


        point1 = line.n2p(-4)
        point2 = line.n2p(-2)
        point3 = line.n2p(0)

        perpend = Line(
            point1,
            point1 + UP * 2.5,
            color=WHITE
        )

        perpend2 = Line(
            point2,
            point2 + UP * 2.5,
            color=WHITE
        )

        perpend3 = Line(
            point3,
            point3 + UP * 2.5,
            color=WHITE
        )

        label1 = Text("x'", font_size=30)
        label1.next_to(perpend.get_end(), RIGHT, buff=0.15)
        label2 = Text("x''", font_size=30)
        label2.next_to(perpend2.get_end(), RIGHT, buff=0.15)
        label3 = Text("x'''", font_size=30)
        label3.next_to(perpend3.get_end(), RIGHT, buff=0.15)

        text1 = Text("E", font_size=30)
        text1.next_to(line.n2p(0), UP*8, buff=0.15)
        text2 = Text("a", font_size=30)
        text2.next_to(line.n2p(5), DOWN*2, buff=0.15)
        text3 = Text("a-α", font_size=28)
        text3.next_to(line.n2p(-5), DOWN*2, buff=0.15)

        text4 = Text("a-β", font_size=28)
        text4.next_to(line.n2p(-3), DOWN*1.5, buff=0.15)

        text5 = Text("a-γ", font_size=28)
        text5.next_to(line.n2p(-1), DOWN * 3, buff=0.15)

        text6 = Text("∃ x'∈ E :- a-α < x' ≤ a", font_size=40)
        text6.next_to(line.n2p(0), DOWN*13, buff=0.15)

        group_per = VGroup(perpend2, perpend3, label2, label3)
        group_arcs = VGroup(arc2, arc3, text4, text5)


        # Анимация появления
        self.wait(2)
        self.play(Create(line), run_time=1.5)
        self.wait(1)
        self.play(Create(arc), run_time=2)
        self.play(Write(text1))
        self.play(Write(text2), Write(text3))
        self.wait(1.5)
        self.play(Create(perpend), run_time=1.5)
        self.play(Write(label1))
        self.wait(1.5)
        self.play(Create(arc2), Write(text4), run_time=1.5)
        self.wait(1.5)
        self.play(Create(perpend2), run_time=1.5)
        self.play(Write(label2))
        self.wait(1.5)
        self.play(Create(arc3), Write(text5), run_time=1.5)
        self.wait(1.5)
        self.play(Create(perpend3), text1.animate.shift(RIGHT), run_time=1.5)
        self.play(Write(label3))
        self.wait(1.5)
        self.play(FadeOut(group_per), FadeOut(group_arcs), text1.animate.shift(LEFT), run_time=1.5)
        self.wait(1.5)
        self.play(Write(text6), run_time=1.5)
        self.wait(3)

