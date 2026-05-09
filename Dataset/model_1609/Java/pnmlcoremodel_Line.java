





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_Line  {

    private String width;
    private String color;
    private String style;
    private String shape;





    private pnmlcoremodel_NodeGraphics pnmlcoremodel_nodegraphics;




    private pnmlcoremodel_NodeGraphics pnmlcoremodel_nodegraphics;


    public pnmlcoremodel_Line(
        String width,        String color,        String style,        String shape    ) {
        this.width = width;
        this.color = color;
        this.style = style;
        this.shape = shape;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }

    public pnmlcoremodel_NodeGraphics getPnmlcoremodel_nodegraphics() {
        return pnmlcoremodel_nodegraphics;
    }

    public void setPnmlcoremodel_nodegraphics(pnmlcoremodel_NodeGraphics pnmlcoremodel_nodegraphics) {
        this.pnmlcoremodel_nodegraphics = pnmlcoremodel_nodegraphics;
    }
    public pnmlcoremodel_NodeGraphics getPnmlcoremodel_nodegraphics() {
        return pnmlcoremodel_nodegraphics;
    }

    public void setPnmlcoremodel_nodegraphics(pnmlcoremodel_NodeGraphics pnmlcoremodel_nodegraphics) {
        this.pnmlcoremodel_nodegraphics = pnmlcoremodel_nodegraphics;
    }

}