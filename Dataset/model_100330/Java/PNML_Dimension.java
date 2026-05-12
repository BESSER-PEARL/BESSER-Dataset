





import java.util.List;
import java.util.ArrayList;

public class PNML_Dimension  {

    private String width;
    private String height;





    private NodeGraphics nodegraphics;


    public PNML_Dimension(
        String width,        String height    ) {
        this.width = width;
        this.height = height;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public NodeGraphics getNodegraphics() {
        return nodegraphics;
    }

    public void setNodegraphics(NodeGraphics nodegraphics) {
        this.nodegraphics = nodegraphics;
    }

}