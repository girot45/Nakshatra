import matplotlib.pyplot as plt
import numpy as np
import matplotlib.transforms as transforms
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


#### Colors for grahas ####
#Sun - Surya - Red - circle 
#Moon - Chandra - White - semicircle
#Mars - Mangala - Red - triangle
#Mercury - Budha - Green - bow (dhanusha)
#Jupiter - Guru - Yellow - lotus
#Venus - Shukra - White - square
#Saturn - Shani - Black - snake
#Rahu - Blue - crocodile
#Ketu - Grey - sword



def plot_moon_phase(day,drawing_origin,radius,fig,ax):
    center = np.array([0,0]) 
    trans = (fig.dpi_scale_trans + transforms.ScaledTranslation(drawing_origin[0],drawing_origin[1], ax.transData))

    image_path = "../../../img/moon.png"
    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=radius )
    ab = AnnotationBbox(imagebox, (0, 0), xybox=drawing_origin,
                        xycoords='data',
                        frameon=False)

    ax.add_artist(ab)

    # if (0 < day <= 7.5):
    #     circle = mpatches.Circle(center,radius,ec="darkslategrey",fc="w",lw=0.5,transform=trans,clip_on=False,zorder=10)
    #     ellipse = mpatches.Ellipse(center,2*radius*np.sin(np.pi/2 - day*12*np.pi/180),2*radius,fc="darkslategrey",ec=None,transform=trans,clip_on=False,zorder=10)
    #     wedge = mpatches.Wedge(center,radius,90,270,fc="darkslategrey",ec=None,transform=trans,clip_on=False,zorder=10)
    #     ax.add_patch(circle)
    #     ax.add_patch(wedge)
    #     ax.add_patch(ellipse)
    #
    # if (7.5 < day <= 15):
    #     circle = mpatches.Circle(center,radius,ec="darkslategrey",fc="w",lw=0.5,transform=trans,clip_on=False,zorder=10)
    #     ellipse = mpatches.Ellipse(center,2*radius*np.sin(np.pi/2 - day*12*np.pi/180),2*radius,fc="w",ec=None,transform=trans,clip_on=False,zorder=10)
    #     wedge = mpatches.Wedge(center,radius,90,270,fc="darkslategrey",ec=None,transform=trans,clip_on=False,zorder=10)
    #     ax.add_patch(circle)
    #     ax.add_patch(wedge)
    #     ax.add_patch(ellipse)
    #
    # if (15 < day <= 22.5):
    #     circle = mpatches.Circle(center,radius,ec="darkslategrey",fc="darkslategrey",lw=0.5,transform=trans,clip_on=False,zorder=10)
    #     ellipse = mpatches.Ellipse(center,2*radius*np.sin(np.pi/2 - (day-15)*12*np.pi/180),2*radius,fc="w",ec=None,transform=trans,clip_on=False,zorder=10)
    #     wedge = mpatches.Wedge(center,radius,90,270,fc="w",ec=None,transform=trans,clip_on=False,zorder=10)
    #     ax.add_patch(circle)
    #     ax.add_patch(wedge)
    #     ax.add_patch(ellipse)
    #
    # if (22.5 < day <= 30):
    #     circle = mpatches.Circle(center,radius,ec="darkslategrey",fc="darkslategrey",lw=0.5,transform=trans,clip_on=False,zorder=10)
    #     ellipse = mpatches.Ellipse(center,2*radius*np.sin(np.pi/2 - (day-15)*12*np.pi/180),2*radius,fc="darkslategrey",ec=None,transform=trans,clip_on=False,zorder=10)
    #     wedge = mpatches.Wedge(center,radius,90,270,fc="w",ec=None,transform=trans,clip_on=False,zorder=10)
    #     ax.add_patch(circle)
    #     ax.add_patch(wedge)
    #     ax.add_patch(ellipse)
    
    return 0


def plot_sun(drawing_origin,radius,fig,ax):
    # center = np.array([0,0])
    # trans = (fig.dpi_scale_trans + transforms.ScaledTranslation(drawing_origin[0],drawing_origin[1], ax.transData))

    # circle = mpatches.Circle(center,radius,ec="orange",fc="yellow",transform=trans,clip_on=False)
    # ax.add_patch(circle)
    image_path = "../../../img/sun.png"
    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=radius * 2)
    ab = AnnotationBbox(imagebox, (0, 0), xybox=drawing_origin,
                        xycoords='data',
                        frameon=False)

    ax.add_artist(ab)

    
    return 0

def plot_inner_graha_phase(graha,angle_to_sun,drawing_origin,radius,fig,ax):
    center = np.array([0,0])
    trans = (fig.dpi_scale_trans + transforms.ScaledTranslation(drawing_origin[0],drawing_origin[1], ax.transData))
    
    if (graha == "mercuri"):
        image_path = "../../../img/mercuri.png"

    elif (graha == "venus"):
        image_path = "../../../img/venus.png"

    else:
        print("That is not an inner graha! Use the outer graha function to plot ",graha)
        return
    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=radius * 2)
    ab = AnnotationBbox(imagebox, (0, 0), xybox=drawing_origin,
                        xycoords='data',
                        frameon=False)

    ax.add_artist(ab)

    # if (0 < (angle_to_sun/12) <= 7.5):
    #     circle = mpatches.Circle(center,radius,ec=dark_side_color,fc=bright_side_color,lw=0.5,transform=trans,clip_on=False)
    #     ellipse = mpatches.Ellipse(center,2*radius*np.sin(np.pi/2 - (angle_to_sun/12)*12*np.pi/180),2*radius,fc=dark_side_color,ec=None,transform=trans,clip_on=False)
    #     wedge = mpatches.Wedge(center,radius,90,270,fc=dark_side_color,ec=None,transform=trans,clip_on=False)
    #     ax.add_patch(circle)
    #     ax.add_patch(wedge)
    #     ax.add_patch(ellipse)
    #
    # if (7.5 < (angle_to_sun/12) <= 15):
    #     circle = mpatches.Circle(center,radius,ec=dark_side_color,fc=bright_side_color,lw=0.5,transform=trans,clip_on=False)
    #     ellipse = mpatches.Ellipse(center,2*radius*np.sin(np.pi/2 - (angle_to_sun/12)*12*np.pi/180),2*radius,fc=bright_side_color,ec=None,transform=trans,clip_on=False)
    #     wedge = mpatches.Wedge(center,radius,90,270,fc=dark_side_color,ec=None,transform=trans,clip_on=False)
    #     ax.add_patch(circle)
    #     ax.add_patch(wedge)
    #     ax.add_patch(ellipse)
    #
    # if (15 < (angle_to_sun/12) <= 22.5):
    #     circle = mpatches.Circle(center,radius,ec=dark_side_color,fc=bright_side_color,lw=0.5,transform=trans,clip_on=False)
    #     ellipse = mpatches.Ellipse(center,2*radius*np.sin(np.pi/2 - ((angle_to_sun/12)-15)*12*np.pi/180),2*radius,fc=bright_side_color,ec=None,transform=trans,clip_on=False)
    #     wedge = mpatches.Wedge(center,radius,270,90,fc=dark_side_color,ec=None,transform=trans,clip_on=False)
    #     ax.add_patch(circle)
    #     ax.add_patch(wedge)
    #     ax.add_patch(ellipse)
    #
    # if (22.5 < (angle_to_sun/12) <= 30):
    #     circle = mpatches.Circle(center,radius,ec=dark_side_color,fc=bright_side_color,lw=0.5,transform=trans,clip_on=False)
    #     ellipse = mpatches.Ellipse(center,2*radius*np.sin(np.pi/2 - ((angle_to_sun/12)-15)*12*np.pi/180),2*radius,fc=dark_side_color,ec=None,transform=trans,clip_on=False)
    #     wedge = mpatches.Wedge(center,radius,270,90,fc=dark_side_color,ec=None,transform=trans,clip_on=False)
    #     ax.add_patch(circle)
    #     ax.add_patch(wedge)
    #     ax.add_patch(ellipse)

    return 0

def plot_outer_graha(graha,drawing_origin,radius,fig,ax):
    
    center = np.array([0,0])
    trans = (fig.dpi_scale_trans + transforms.ScaledTranslation(drawing_origin[0],drawing_origin[1], ax.transData))
    
    if (graha == "mars"):
        image_path = "../../../img/mars.png"
    elif (graha == "jupiter"):
        image_path = "../../../img/jupiter.png"
    elif (graha == "saturn"):
        image_path = "../../../img/saturn.png"
    else:
        print("That is not an outer graha! Use the inner graha function to plot",graha)
        return

    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=radius * 2)
    ab = AnnotationBbox(imagebox, (0, 0), xybox=drawing_origin,
                        xycoords='data',
                        frameon=False)

    ax.add_artist(ab)

    # circle = mpatches.Circle(center,radius,ec="w",fc=mcolor,lw=0.5,transform=trans,clip_on=False)
    # ax.add_patch(circle)

    return 0

def plot_rahu(drawing_origin,scale,fig,ax):
    
    center = np.array([0,0])
    trans = (transforms.Affine2D().scale(scale) + transforms.ScaledTranslation(drawing_origin[0],drawing_origin[1], ax.transData))
    # Загрузка изображения
    image_path = "../../../img/rahu.png"
    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=0.1)

    # Добавляем смещение
    ab = AnnotationBbox(imagebox, (0, 0), xybox=drawing_origin,
                        xycoords='data',
                        frameon=False)
    ax.add_artist(ab)
    
    # from matplotlib.path import Path
    #
    # verts = [
    # (-1, 1),    # Vert1
    # (1., 1.),   # Vert2
    # (1., -1.),  # Pivot1
    # (0, -1.),   # Vert3
    # (-1., -1.), # Pivot2
    # (-1., 1.),
    # (-1., 1.),
    # ]
    #
    # codes = [
    #     Path.MOVETO,
    #     Path.LINETO,
    #     Path.CURVE3,
    #     Path.LINETO,
    #     Path.CURVE3,
    #     Path.LINETO,
    #     Path.CLOSEPOLY,
    # ]
    #
    # path = Path(verts, codes)
    #
    # patch = mpatches.PathPatch(path, facecolor='blue',edgecolor='lightblue',lw=0.5*scale/5,transform=trans,clip_on=False)
    # ax.add_patch(patch)

    return 0

def plot_ketu(drawing_origin,scale,fig,ax):

    center = np.array([0,0])
    trans = (transforms.Affine2D().scale(scale) + transforms.ScaledTranslation(drawing_origin[0],drawing_origin[1], ax.transData))

    image_path = "../../../img/ketu.png"
    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=0.1)

    # Добавляем смещение
    ab = AnnotationBbox(imagebox, (0, 0), xybox=drawing_origin,
                        xycoords='data',
                        frameon=False)
    ax.add_artist(ab)

    # from matplotlib.path import Path
    #
    # verts = [
    # (-1, 1),    # Vert1
    # (1., 1.),   # Vert2
    # (1., -1.),  # Vert3
    # (-1., -1.), # Vert4
    # (0, 0),     # Vert5
    # (-1., 1.),  # Vert6
    # (-1., 1.),
    # ]
    #
    # codes = [
    #     Path.MOVETO,
    #     Path.LINETO,
    #     Path.LINETO,
    #     Path.LINETO,
    #     Path.LINETO,
    #     Path.LINETO,
    #     Path.CLOSEPOLY,
    # ]
    #
    # path = Path(verts, codes)
    #
    # patch = mpatches.PathPatch(path, facecolor='dimgrey',edgecolor='lightgrey',lw=0.5*scale/5,transform=trans,clip_on=False)
    # ax.add_patch(patch)

    return 0

