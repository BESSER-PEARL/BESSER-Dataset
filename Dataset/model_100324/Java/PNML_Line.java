





import java.util.List;
import java.util.ArrayList;

public class PNML_Line  {

    private String shape;
    private String width;
    private String style;





    private AnnotationGraphics annotationgraphics;




    private EdgeGraphics edgegraphics;




    private NodeGraphics nodegraphics;


    public PNML_Line(
        String shape,        String width,        String style    ) {
        this.shape = shape;
        this.width = width;
        this.style = style;
    }


    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
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

    public AnnotationGraphics getAnnotationgraphics() {
        return annotationgraphics;
    }

    public void setAnnotationgraphics(AnnotationGraphics annotationgraphics) {
        this.annotationgraphics = annotationgraphics;
    }
    public EdgeGraphics getEdgegraphics() {
        return edgegraphics;
    }

    public void setEdgegraphics(EdgeGraphics edgegraphics) {
        this.edgegraphics = edgegraphics;
    }
    public NodeGraphics getNodegraphics() {
        return nodegraphics;
    }

    public void setNodegraphics(NodeGraphics nodegraphics) {
        this.nodegraphics = nodegraphics;
    }

}