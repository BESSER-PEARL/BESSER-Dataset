





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_Line  {

    private String style;
    private String color;
    private float width;
    private String shape;





    private pnmlcoremodel_AnnotationGraphics pnmlcoremodel_annotationgraphics;




    private pnmlcoremodel_NodeGraphics pnmlcoremodel_nodegraphics;




    private pnmlcoremodel_ArcGraphics pnmlcoremodel_arcgraphics;


    public pnmlcoremodel_Line(
        String style,        String color,        float width,        String shape    ) {
        this.style = style;
        this.color = color;
        this.width = width;
        this.shape = shape;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
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
    public pnmlcoremodel_ArcGraphics getPnmlcoremodel_arcgraphics() {
        return pnmlcoremodel_arcgraphics;
    }

    public void setPnmlcoremodel_arcgraphics(pnmlcoremodel_ArcGraphics pnmlcoremodel_arcgraphics) {
        this.pnmlcoremodel_arcgraphics = pnmlcoremodel_arcgraphics;
    }

}