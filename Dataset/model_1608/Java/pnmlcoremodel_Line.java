





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_Line  {

    private String shape;
    private String color;
    private String width;
    private String style;





    private pnmlcoremodel_NodeGraphics pnmlcoremodel_nodegraphics;




    private pnmlcoremodel_NodeGraphics pnmlcoremodel_nodegraphics;


    public pnmlcoremodel_Line(
        String shape,        String color,        String width,        String style    ) {
        this.shape = shape;
        this.color = color;
        this.width = width;
        this.style = style;
    }


    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
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