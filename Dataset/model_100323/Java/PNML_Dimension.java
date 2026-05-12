





import java.util.List;
import java.util.ArrayList;

public class PNML_Dimension  {

    private String height;
    private String width;





    private NodeGraphics nodegraphics;


    public PNML_Dimension(
        String height,        String width    ) {
        this.height = height;
        this.width = width;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
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

}