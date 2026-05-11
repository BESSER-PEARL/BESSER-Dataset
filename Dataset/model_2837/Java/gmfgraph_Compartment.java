





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Compartment extends DiagramElement {

    private boolean needsTitle;
    private boolean collapsible;



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


}