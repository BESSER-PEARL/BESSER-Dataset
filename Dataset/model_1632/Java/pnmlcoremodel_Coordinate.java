





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_Coordinate  {

    private float y;
    private float x;





    private pnmlcoremodel_NodeGraphics pnmlcoremodel_nodegraphics;




    private pnmlcoremodel_ArcGraphics pnmlcoremodel_arcgraphics;




    private pnmlcoremodel_AnnotationGraphics pnmlcoremodel_annotationgraphics;




    private pnmlcoremodel_NodeGraphics pnmlcoremodel_nodegraphics;


    public pnmlcoremodel_Coordinate(
        float y,        float x    ) {
        this.y = y;
        this.x = x;
    }


    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }

    public pnmlcoremodel_NodeGraphics getPnmlcoremodel_nodegraphics() {
        return pnmlcoremodel_nodegraphics;
    }

    public void setPnmlcoremodel_nodegraphics(pnmlcoremodel_NodeGraphics pnmlcoremodel_nodegraphics) {
        this.pnmlcoremodel_nodegraphics = pnmlcoremodel_nodegraphics;
    }
    public pnmlcoremodel_ArcGraphics getPnmlcoremodel_arcgraphics() {
        return pnmlcoremodel_arcgraphics;
    }

    public void setPnmlcoremodel_arcgraphics(pnmlcoremodel_ArcGraphics pnmlcoremodel_arcgraphics) {
        this.pnmlcoremodel_arcgraphics = pnmlcoremodel_arcgraphics;
    }
    public pnmlcoremodel_AnnotationGraphics getPnmlcoremodel_annotationgraphics() {
        return pnmlcoremodel_annotationgraphics;
    }

    public void setPnmlcoremodel_annotationgraphics(pnmlcoremodel_AnnotationGraphics pnmlcoremodel_annotationgraphics) {
        this.pnmlcoremodel_annotationgraphics = pnmlcoremodel_annotationgraphics;
    }
    public pnmlcoremodel_NodeGraphics getPnmlcoremodel_nodegraphics() {
        return pnmlcoremodel_nodegraphics;
    }

    public void setPnmlcoremodel_nodegraphics(pnmlcoremodel_NodeGraphics pnmlcoremodel_nodegraphics) {
        this.pnmlcoremodel_nodegraphics = pnmlcoremodel_nodegraphics;
    }

}