#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#======================= END GPL LICENSE BLOCK ========================

# <pep8 compliant>

from .widgets import create_widget


def create_compass_widget(rig, bone_name, bone_transform_name=None):
    """ Creates a compass-shaped widget.
    """
    obj = create_widget(rig, bone_name, bone_transform_name)
    if obj != None:
        verts = [(0.0, 1.2000000476837158, 0.0), (0.19509032368659973, 0.9807852506637573, 0.0), (0.3826834559440613, 0.9238795042037964, 0.0), (0.5555702447891235, 0.8314695954322815, 0.0), (0.7071067690849304, 0.7071067690849304, 0.0), (0.8314696550369263, 0.5555701851844788, 0.0), (0.9238795042037964, 0.3826834261417389, 0.0), (0.9807852506637573, 0.19509035348892212, 0.0), (1.2000000476837158, 7.549790126404332e-08, 0.0), (0.9807853102684021, -0.19509020447731018, 0.0), (0.9238795638084412, -0.38268327713012695, 0.0), (0.8314696550369263, -0.5555701851844788, 0.0), (0.7071067690849304, -0.7071067690849304, 0.0), (0.5555701851844788, -0.8314696550369263, 0.0), (0.38268327713012695, -0.9238796234130859, 0.0), (0.19509008526802063, -0.9807853102684021, 0.0), (-3.2584136988589307e-07, -1.2999999523162842, 0.0), (-0.19509072601795197, -0.9807851910591125, 0.0), (-0.3826838731765747, -0.9238793253898621, 0.0), (-0.5555707216262817, -0.8314692974090576, 0.0), (-0.7071072459220886, -0.707106351852417, 0.0), (-0.8314700126647949, -0.5555696487426758, 0.0), (-0.923879861831665, -0.3826826810836792, 0.0), (-0.9807854294776917, -0.1950894594192505, 0.0), (-1.2000000476837158, 9.655991561885457e-07, 0.0), (-0.980785071849823, 0.1950913518667221, 0.0), (-0.923879086971283, 0.38268446922302246, 0.0), (-0.831468939781189, 0.5555712580680847, 0.0), (-0.7071058750152588, 0.707107663154602, 0.0), (-0.5555691123008728, 0.8314703702926636, 0.0), (-0.38268208503723145, 0.9238801002502441, 0.0), (-0.19508881866931915, 0.9807855486869812, 0.0)]
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 27), (27, 28), (28, 29), (29, 30), (30, 31), (0, 31)]
        mesh = obj.data
        mesh.from_pydata(verts, edges, [])
        mesh.update()


def create_root_widget(rig, bone_name, bone_transform_name=None):
    """ Creates a widget for the root bone.
    """
    obj = create_widget(rig, bone_name, bone_transform_name)
    if obj != None:
        verts = [(0.7071067690849304, 0.7071067690849304, 0.0), (0.7071067690849304, -0.7071067690849304, 0.0), (-0.7071067690849304, 0.7071067690849304, 0.0), (-0.7071067690849304, -0.7071067690849304, 0.0), (0.8314696550369263, 0.5555701851844788, 0.0), (0.8314696550369263, -0.5555701851844788, 0.0), (-0.8314696550369263, 0.5555701851844788, 0.0), (-0.8314696550369263, -0.5555701851844788, 0.0), (0.9238795042037964, 0.3826834261417389, 0.0), (0.9238795042037964, -0.3826834261417389, 0.0), (-0.9238795042037964, 0.3826834261417389, 0.0), (-0.9238795042037964, -0.3826834261417389, 0.0), (0.9807852506637573, 0.19509035348892212, 0.0), (0.9807852506637573, -0.19509035348892212, 0.0), (-0.9807852506637573, 0.19509035348892212, 0.0), (-0.9807852506637573, -0.19509035348892212, 0.0), (0.19509197771549225, 0.9807849526405334, 0.0), (0.19509197771549225, -0.9807849526405334, 0.0), (-0.19509197771549225, 0.9807849526405334, 0.0), (-0.19509197771549225, -0.9807849526405334, 0.0), (0.3826850652694702, 0.9238788485527039, 0.0), (0.3826850652694702, -0.9238788485527039, 0.0), (-0.3826850652694702, 0.9238788485527039, 0.0), (-0.3826850652694702, -0.9238788485527039, 0.0), (0.5555717945098877, 0.8314685821533203, 0.0), (0.5555717945098877, -0.8314685821533203, 0.0), (-0.5555717945098877, 0.8314685821533203, 0.0), (-0.5555717945098877, -0.8314685821533203, 0.0), (0.19509197771549225, 1.2807848453521729, 0.0), (0.19509197771549225, -1.2807848453521729, 0.0), (-0.19509197771549225, 1.2807848453521729, 0.0), (-0.19509197771549225, -1.2807848453521729, 0.0), (1.280785322189331, 0.19509035348892212, 0.0), (1.280785322189331, -0.19509035348892212, 0.0), (-1.280785322189331, 0.19509035348892212, 0.0), (-1.280785322189331, -0.19509035348892212, 0.0), (0.3950919806957245, 1.2807848453521729, 0.0), (0.3950919806957245, -1.2807848453521729, 0.0), (-0.3950919806957245, 1.2807848453521729, 0.0), (-0.3950919806957245, -1.2807848453521729, 0.0), (1.280785322189331, 0.39509034156799316, 0.0), (1.280785322189331, -0.39509034156799316, 0.0), (-1.280785322189331, 0.39509034156799316, 0.0), (-1.280785322189331, -0.39509034156799316, 0.0), (0.0, 1.5807849168777466, 0.0), (0.0, -1.5807849168777466, 0.0), (1.5807852745056152, 0.0, 0.0), (-1.5807852745056152, 0.0, 0.0)]
        edges = [(0, 4), (1, 5), (2, 6), (3, 7), (4, 8), (5, 9), (6, 10), (7, 11), (8, 12), (9, 13), (10, 14), (11, 15), (16, 20), (17, 21), (18, 22), (19, 23), (20, 24), (21, 25), (22, 26), (23, 27), (0, 24), (1, 25), (2, 26), (3, 27), (16, 28), (17, 29), (18, 30), (19, 31), (12, 32), (13, 33), (14, 34), (15, 35), (28, 36), (29, 37), (30, 38), (31, 39), (32, 40), (33, 41), (34, 42), (35, 43), (36, 44), (37, 45), (38, 44), (39, 45), (40, 46), (41, 46), (42, 47), (43, 47)]
        mesh = obj.data
        mesh.from_pydata(verts, edges, [])
        mesh.update()


def create_neck_bend_widget(rig, bone_name, radius=1.0, head_tail=0.0, bone_transform_name=None):
    obj = create_widget(rig, bone_name, bone_transform_name)
    size = 2.0
    if obj != None:
        v = [(-0.08855080604553223 * size, 0.7388765811920166 * size, -0.3940150737762451 * size),
                 (0.08855044841766357 * size, 0.7388765811920166 * size, -0.3940150737762451 * size),
                 (0.17710095643997192 * size, 0.5611097812652588 * size, -0.6478927135467529 * size),
                 (-4.0892032870942785e-07 * size, 0.4087378978729248 * size, -0.865501880645752 * size),
                 (-0.17710143327713013 * size, 0.5611097812652588 * size, -0.6478922367095947 * size),
                 (0.08855026960372925 * size, 0.5611097812652588 * size, -0.6478924751281738 * size),
                 (-0.08855092525482178 * size, 0.5611097812652588 * size, -0.6478927135467529 * size),
                 (-0.6478927135467529 * size, 0.5611097812652588 * size, 0.08855098485946655 * size),
                 (-0.6478927135467529 * size, 0.5611097812652588 * size, -0.08855020999908447 * size),
                 (-0.6478924751281738 * size, 0.5611097812652588 * size, 0.17710155248641968 * size),
                 (-0.865501880645752 * size, 0.4087378978729248 * size, 4.6876743908796925e-07 * size),
                 (-0.647892951965332 * size, 0.5611097812652588 * size, -0.17710083723068237 * size),
                 (-0.39401543140411377 * size, 0.7388765811920166 * size, -0.08855029940605164 * size),
                 (-0.39401543140411377 * size, 0.7388765811920166 * size, 0.08855095505714417 * size),
                 (0.6478927135467529 * size, 0.5611097812652588 * size, -0.08855059742927551 * size),
                 (0.6478927135467529 * size, 0.5611097812652588 * size, 0.08855065703392029 * size),
                 (0.6478924751281738 * size, 0.5611097812652588 * size, -0.17710113525390625 * size),
                 (0.865501880645752 * size, 0.4087378978729248 * size, -3.264514703005261e-08 * size),
                 (0.647892951965332 * size, 0.5611097812652588 * size, 0.1771012544631958 * size),
                 (0.08855065703392029 * size, 0.7388765811920166 * size, 0.3940155506134033 * size),
                 (-0.08855056762695312 * size, 0.7388765811920166 * size, 0.3940155506134033 * size),
                 (-0.17710107564926147 * size, 0.5611097812652588 * size, 0.647892951965332 * size),
                 (2.244429140318971e-07 * size, 0.4087378978729248 * size, 0.865502119064331 * size),
                 (0.17710131406784058 * size, 0.5611097812652588 * size, 0.6478927135467529 * size),
                 (-0.08855044841766357 * size, 0.5611097812652588 * size, 0.647892951965332 * size),
                 (0.08855074644088745 * size, 0.5611097812652588 * size, 0.647892951965332 * size),
                 (0.3940153121948242 * size, 0.7388765811920166 * size, 0.08855071663856506 * size),
                 (0.39401519298553467 * size, 0.7388765811920166 * size, -0.08855047821998596 * size),
                 (-8.416645869147032e-08 * size, 0.8255770206451416 * size, -0.2656517028808594 * size),
                 (-0.06875583529472351 * size, 0.8255770206451416 * size, -0.2565997838973999 * size),
                 (-0.13282597064971924 * size, 0.8255770206451416 * size, -0.2300611138343811 * size),
                 (-0.18784427642822266 * size, 0.8255770206451416 * size, -0.18784409761428833 * size),
                 (-0.2300613522529602 * size, 0.8255770206451416 * size, -0.1328257918357849 * size),
                 (-0.256600022315979 * size, 0.8255770206451416 * size, -0.06875564157962799 * size),
                 (-0.2656519412994385 * size, 0.8255770206451416 * size, 9.328307726264029e-08 * size),
                 (-0.25660014152526855 * size, 0.8255770206451416 * size, 0.06875583529472351 * size),
                 (-0.2300613522529602 * size, 0.8255770206451416 * size, 0.13282597064971924 * size),
                 (-0.18784433603286743 * size, 0.8255770206451416 * size, 0.18784421682357788 * size),
                 (-0.1328260898590088 * size, 0.8255770206451416 * size, 0.23006129264831543 * size),
                 (-0.06875592470169067 * size, 0.8255770206451416 * size, 0.256600022315979 * size),
                 (-1.8761508613351907e-07 * size, 0.8255770206451416 * size, 0.2656519412994385 * size),
                 (0.06875556707382202 * size, 0.8255770206451416 * size, 0.2566000819206238 * size),
                 (0.13282573223114014 * size, 0.8255770206451416 * size, 0.23006141185760498 * size),
                 (0.18784403800964355 * size, 0.8255770206451416 * size, 0.1878443956375122 * size),
                 (0.23006105422973633 * size, 0.8255770206451416 * size, 0.1328260898590088 * size),
                 (0.25659990310668945 * size, 0.8255770206451416 * size, 0.06875596940517426 * size),
                 (0.2656517028808594 * size, 0.8255770206451416 * size, 2.3684407324253698e-07 * size),
                 (0.25659990310668945 * size, 0.8255770206451416 * size, -0.06875550746917725 * size),
                 (0.23006117343902588 * size, 0.8255770206451416 * size, -0.13282567262649536 * size),
                 (0.18784427642822266 * size, 0.8255770206451416 * size, -0.18784397840499878 * size),
                 (0.13282597064971924 * size, 0.8255770206451416 * size, -0.23006099462509155 * size),
                 (0.0687558501958847 * size, 0.8255770206451416 * size, -0.2565997838973999 * size), ]
        edges = [(1, 0), (3, 2), (5, 2), (4, 3), (6, 4), (1, 5), (0, 6), (13, 7), (12, 8), (7, 9), (9, 10), (8, 11),
                 (27, 14), (26, 15), (14, 16), (16, 17), (15, 18), (17, 18), (10, 11), (12, 13), (20, 19), (22, 21),
                 (24, 21), (23, 22), (29, 28), (30, 29), (31, 30), (32, 31), (33, 32), (34, 33), (35, 34), (36, 35),
                 (37, 36), (38, 37), (39, 38), (40, 39), (41, 40), (42, 41), (43, 42), (44, 43), (45, 44), (46, 45),
                 (47, 46), (48, 47), (49, 48), (50, 49), (51, 50), (28, 51), (26, 27), (25, 23), (20, 24),
                 (19, 25), ]

        verts = [(a[0] * radius, head_tail, a[2] * radius) for a in v]
        mesh = obj.data
        mesh.from_pydata(verts, edges, [])
        mesh.update()


def create_neck_tweak_widget(rig, bone_name, size=1.0, bone_transform_name=None):
    obj = create_widget(rig, bone_name, bone_transform_name)

    if obj != None:
        verts = [(0.3535533845424652 * size, 0.3535533845424652 * size, 0.0 * size),
                 (0.4619397521018982 * size, 0.19134171307086945 * size, 0.0 * size),
                 (0.5 * size, -2.1855694143368964e-08 * size, 0.0 * size),
                 (0.4619397521018982 * size, -0.19134175777435303 * size, 0.0 * size),
                 (0.3535533845424652 * size, -0.3535533845424652 * size, 0.0 * size),
                 (0.19134174287319183 * size, -0.4619397521018982 * size, 0.0 * size),
                 (7.549790126404332e-08 * size, -0.5 * size, 0.0 * size),
                 (-0.1913416087627411 * size, -0.46193981170654297 * size, 0.0 * size),
                 (-0.35355329513549805 * size, -0.35355350375175476 * size, 0.0 * size),
                 (-0.4619397521018982 * size, -0.19134178757667542 * size, 0.0 * size),
                 (-0.5 * size, 5.962440319251527e-09 * size, 0.0 * size),
                 (-0.4619397222995758 * size, 0.1913418024778366 * size, 0.0 * size),
                 (-0.35355326533317566 * size, 0.35355350375175476 * size, 0.0 * size),
                 (-0.19134148955345154 * size, 0.46193987131118774 * size, 0.0 * size),
                 (3.2584136988589307e-07 * size, 0.5 * size, 0.0 * size),
                 (0.1913420855998993 * size, 0.46193960309028625 * size, 0.0 * size),
                 (7.450580596923828e-08 * size, 0.46193960309028625 * size, 0.19134199619293213 * size),
                 (5.9254205098113744e-08 * size, 0.5 * size, 2.323586443253589e-07 * size),
                 (4.470348358154297e-08 * size, 0.46193987131118774 * size, -0.1913415789604187 * size),
                 (2.9802322387695312e-08 * size, 0.35355350375175476 * size, -0.3535533547401428 * size),
                 (2.9802322387695312e-08 * size, 0.19134178757667542 * size, -0.46193981170654297 * size),
                 (5.960464477539063e-08 * size, -1.1151834122813398e-08 * size, -0.5000000596046448 * size),
                 (5.960464477539063e-08 * size, -0.1913418024778366 * size, -0.46193984150886536 * size),
                 (5.960464477539063e-08 * size, -0.35355350375175476 * size, -0.3535533845424652 * size),
                 (7.450580596923828e-08 * size, -0.46193981170654297 * size, -0.19134166836738586 * size),
                 (9.348272556053416e-08 * size, -0.5 * size, 1.624372103492533e-08 * size),
                 (1.043081283569336e-07 * size, -0.4619397521018982 * size, 0.19134168326854706 * size),
                 (1.1920928955078125e-07 * size, -0.3535533845424652 * size, 0.35355329513549805 * size),
                 (1.1920928955078125e-07 * size, -0.19134174287319183 * size, 0.46193966269493103 * size),
                 (1.1920928955078125e-07 * size, -4.7414250303745575e-09 * size, 0.49999991059303284 * size),
                 (1.1920928955078125e-07 * size, 0.19134172797203064 * size, 0.46193966269493103 * size),
                 (8.940696716308594e-08 * size, 0.3535533845424652 * size, 0.35355329513549805 * size),
                 (0.3535534739494324 * size, 0.0 * size, 0.35355329513549805 * size),
                 (0.1913418173789978 * size, -2.9802322387695312e-08 * size, 0.46193966269493103 * size),
                 (8.303572940349113e-08 * size, -5.005858838558197e-08 * size, 0.49999991059303284 * size),
                 (-0.19134165346622467 * size, -5.960464477539063e-08 * size, 0.46193966269493103 * size),
                 (-0.35355329513549805 * size, -8.940696716308594e-08 * size, 0.35355329513549805 * size),
                 (-0.46193963289260864 * size, -5.960464477539063e-08 * size, 0.19134168326854706 * size),
                 (-0.49999991059303284 * size, -5.960464477539063e-08 * size, 1.624372103492533e-08 * size),
                 (-0.4619397521018982 * size, -2.9802322387695312e-08 * size, -0.19134166836738586 * size),
                 (-0.3535534143447876 * size, -2.9802322387695312e-08 * size, -0.3535533845424652 * size),
                 (-0.19134171307086945 * size, 0.0 * size, -0.46193984150886536 * size),
                 (7.662531942287387e-08 * size, 9.546055501630235e-09 * size, -0.5000000596046448 * size),
                 (0.19134187698364258 * size, 5.960464477539063e-08 * size, -0.46193981170654297 * size),
                 (0.3535535931587219 * size, 5.960464477539063e-08 * size, -0.3535533547401428 * size),
                 (0.4619399905204773 * size, 5.960464477539063e-08 * size, -0.1913415789604187 * size),
                 (0.5000000596046448 * size, 5.960464477539063e-08 * size, 2.323586443253589e-07 * size),
                 (0.4619396924972534 * size, 2.9802322387695312e-08 * size, 0.19134199619293213 * size),
                 (1.563460111618042 * size, 2.778762819843905e-08 * size, 1.5634593963623047 * size),
                 (0.8461387157440186 * size, -1.0400220418205208e-07 * size, 2.0427582263946533 * size),
                 (7.321979467178608e-08 * size, -1.9357810288056498e-07 * size, 2.2110657691955566 * size),
                 (-0.8461385369300842 * size, -2.3579201524626114e-07 * size, 2.0427582263946533 * size),
                 (-1.5634597539901733 * size, -3.67581861837607e-07 * size, 1.5634593963623047 * size),
                 (-2.0427584648132324 * size, -2.3579204366797057e-07 * size, 0.8461383581161499 * size),
                 (-2.211066246032715 * size, -2.3579204366797057e-07 * size, 9.972505665700737e-08 * size),
                 (-2.0427589416503906 * size, -1.0400223260376151e-07 * size, -0.8461381196975708 * size),
                 (-1.5634604692459106 * size, -1.040022183929068e-07 * size, -1.563459873199463 * size),
                 (-0.8461387753486633 * size, 2.77876033294433e-08 * size, -2.042759418487549 * size),
                 (4.4872678017782164e-08 * size, 7.00015263532805e-08 * size, -2.211066484451294 * size),
                 (0.8461388349533081 * size, 2.913672290105751e-07 * size, -2.0427591800689697 * size),
                 (1.5634608268737793 * size, 2.9136725743228453e-07 * size, -1.563459873199463 * size),
                 (2.042759895324707 * size, 2.9136725743228453e-07 * size, -0.8461377024650574 * size),
                 (2.211066722869873 * size, 2.9136725743228453e-07 * size, 1.0554133496043505e-06 * size),
                 (2.0427587032318115 * size, 1.5957746768435754e-07 * size, 0.8461397886276245 * size), ]
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11),
                 (11, 12), (12, 13), (13, 14), (14, 15), (0, 15), (16, 31), (16, 17), (17, 18), (18, 19), (19, 20),
                 (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 27), (27, 28), (28, 29), (29, 30),
                 (30, 31), (32, 33), (33, 34), (34, 35), (35, 36), (36, 37), (37, 38), (38, 39), (39, 40), (40, 41),
                 (41, 42), (42, 43), (43, 44), (44, 45), (45, 46), (46, 47), (32, 47), (48, 49), (49, 50), (50, 51),
                 (51, 52), (52, 53), (53, 54), (54, 55), (55, 56), (56, 57), (57, 58), (58, 59), (59, 60), (60, 61),
                 (61, 62), (62, 63), (48, 63), (21, 58), (10, 54), (29, 50), (2, 62), ]

        mesh = obj.data
        mesh.from_pydata(verts, edges, [])
        mesh.update()