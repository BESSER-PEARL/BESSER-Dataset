





import java.util.List;
import java.util.ArrayList;

public class PNML_Line  {

    private String shape;
    private String style;
    private String width;





    private NodeGraphics nodegraphics;




    private EdgeGraphics edgegraphics;




    private AnnotationGraphics annotationgraphics;




    private Color color;


    public PNML_Line(
        String shape,        String style,        String width    ) {
        this.shape = shape;
        this.style = style;
        this.width = width;
    }


    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }

    public NodeGraphics getNodegraphics() {
        return nodegraphics;
    }

    public void setNodegraphics(NodeGraphics nodegraphics) {
        this.nodegraphics = nodegraphics;
    }
    public EdgeGraphics getEdgegraphics() {
        return edgegraphics;
    }

    public void setEdgegraphics(EdgeGraphics edgegraphics) {
        this.edgegraphics = edgegraphics;
    }
    public AnnotationGraphics getAnnotationgraphics() {
        return annotationgraphics;
    }

    public void setAnnotationgraphics(AnnotationGraphics annotationgraphics) {
        this.annotationgraphics = annotationgraphics;
    }
    public Color getColor() {
        return color;
    }

    public void setColor(Color color) {
        this.color = color;
    }

}