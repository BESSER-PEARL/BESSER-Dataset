





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Compartment extends DiagramElement {

    private boolean needsTitle;
    private boolean collapsible;





    private gmfgraph_Canvas gmfgraph_canvas;


    public gmfgraph_Compartment(
        boolean needsTitle,        boolean collapsible    ) {
        super(
        );
        this.needsTitle = needsTitle;
        this.collapsible = collapsible;
    }


    public boolean getNeedstitle() {
        return needsTitle;
    }

    public void setNeedstitle(boolean needsTitle) {
        this.needsTitle = needsTitle;
    }
    public boolean getCollapsible() {
        return collapsible;
    }

    public void setCollapsible(boolean collapsible) {
        this.collapsible = collapsible;
    }

    public gmfgraph_Canvas getGmfgraph_canvas() {
        return gmfgraph_canvas;
    }

    public void setGmfgraph_canvas(gmfgraph_Canvas gmfgraph_canvas) {
        this.gmfgraph_canvas = gmfgraph_canvas;
    }

}