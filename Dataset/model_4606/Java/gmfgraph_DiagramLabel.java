





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_DiagramLabel extends Node {

    private boolean elementIcon;
    private boolean external;





    private gmfgraph_Canvas gmfgraph_canvas;


    public gmfgraph_DiagramLabel(
        boolean elementIcon,        boolean external    ) {
        super(
        );
        this.elementIcon = elementIcon;
        this.external = external;
    }


    public boolean getElementicon() {
        return elementIcon;
    }

    public void setElementicon(boolean elementIcon) {
        this.elementIcon = elementIcon;
    }
    public boolean getExternal() {
        return external;
    }

    public void setExternal(boolean external) {
        this.external = external;
    }

    public gmfgraph_Canvas getGmfgraph_canvas() {
        return gmfgraph_canvas;
    }

    public void setGmfgraph_canvas(gmfgraph_Canvas gmfgraph_canvas) {
        this.gmfgraph_canvas = gmfgraph_canvas;
    }

}