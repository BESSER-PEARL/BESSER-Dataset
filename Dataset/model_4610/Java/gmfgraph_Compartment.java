





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Compartment extends DiagramElement {

    private boolean needsTitle;
    private boolean collapsible;





    private gmfgraph_ChildAccess gmfgraph_childaccess;


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

    public gmfgraph_ChildAccess getGmfgraph_childaccess() {
        return gmfgraph_childaccess;
    }

    public void setGmfgraph_childaccess(gmfgraph_ChildAccess gmfgraph_childaccess) {
        this.gmfgraph_childaccess = gmfgraph_childaccess;
    }

}