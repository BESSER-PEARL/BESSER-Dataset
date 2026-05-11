





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Compartment extends DiagramElement {

    private boolean collapsible;
    private boolean needsTitle;





    private gmfgraph_Canvas gmfgraph_canvas;


    public gmfgraph_Compartment(
        boolean collapsible,        boolean needsTitle    ) {
        super(
        );
        this.collapsible = collapsible;
        this.needsTitle = needsTitle;
    }


    public boolean getCollapsible() {
        return collapsible;
    }

    public void setCollapsible(boolean collapsible) {
        this.collapsible = collapsible;
    }
    public boolean getNeedstitle() {
        return needsTitle;
    }

    public void setNeedstitle(boolean needsTitle) {
        this.needsTitle = needsTitle;
    }

    public gmfgraph_Canvas getGmfgraph_canvas() {
        return gmfgraph_canvas;
    }

    public void setGmfgraph_canvas(gmfgraph_Canvas gmfgraph_canvas) {
        this.gmfgraph_canvas = gmfgraph_canvas;
    }

}