from model import *
import glm
import pygame as pg


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = AdvancedSkyBox(app)
        self.movinX = 0
        self.movinY = 0

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        n, s = 20, 1
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, 0, z)))
        # add(Cube(app, pos=(0, 0, 0)))

        add(Cat(app, pos=(0, 4, 0)))

        # n, s = 30, 5
        # for x in range(-n, n, s):
        #     for z in range(-n, n, s):
        #         add(Cat(app, pos=(x, -1, z)))

    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()

    def get_object_list(self, location):
        the_obj = self.objects[location]
        print(the_obj, the_obj.giving_datas(), 'end')



    def moving(self):
        keys = pg.key.get_pressed()
        neco = next((x for x in self.objects if x.tex_id == 'cat'), None)

        block = self.objects[1]

        if keys[pg.K_UP]:
            neco.m_model = glm.translate(neco.m_model, (0.3, 0, 0))
            # neco.m_model[3][0] += 1
        if keys[pg.K_DOWN]:
            neco.m_model = glm.translate(neco.m_model, (-0.3, 0, 0))
            # neco.m_model[3][0] -= 1
        if keys[pg.K_LEFT]:
            neco.m_model = glm.rotate(neco.m_model, 0.1, glm.vec3(0, 1, 0))
            # neco.m_model[3][2] += 1
        if keys[pg.K_RIGHT]:
            neco.m_model = glm.rotate(neco.m_model, -0.1, glm.vec3(0, 1, 0))
            # neco.m_model[3][2] -= 1
        if keys[pg.K_SPACE]:
            neco.m_model = glm.translate(neco.m_model, (0, 0.5, 0))
            # neco.m_model[3][2] -= 1

        neco.m_model = glm.translate(neco.m_model, (0, -0.1, 0))
        self.collision()
        # print(neco.m_model[3])

    def collision(self):
        neco = next((x for x in self.objects if x.tex_id == 'cat'), None)
        # block = next((x for x in self.objects if x.tex_id == 0), None)

        # if neco.m_model[3][1] - 1 < block.m_model[3][1] and int(neco.m_model[3][0]) == int(block.m_model[3][0]) and int(neco.m_model[3][2]) == int(block.m_model[3][2]):
        #     neco.m_model = glm.translate(neco.m_model, (0, block.pos[1] + 0.01, 0))

        # remove_neco = self.objects
        # remove_neco.pop(100)

        for obj in self.objects:
            if obj.tex_id == 'cat':
                break
            elif int(neco.m_model[3][1])  == int(obj.m_model[3][1]) and int(neco.m_model[3][0]) == int(
                    obj.m_model[3][0]) and int(neco.m_model[3][2]) == int(obj.m_model[3][2]):
                neco.m_model[3][1] = (obj.m_model[3][1] + 1)
            # else:
            #     print('else')
