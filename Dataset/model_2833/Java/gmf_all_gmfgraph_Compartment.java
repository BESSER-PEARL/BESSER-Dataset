





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_Compartment extends DiagramElement {

    private boolean collapsible;
    private boolean needsTitle;



    public gmf_all_gmfgraph_Compartment(
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


}