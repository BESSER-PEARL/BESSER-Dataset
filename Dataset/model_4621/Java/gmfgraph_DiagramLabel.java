





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_DiagramLabel extends Node {

    private boolean external;
    private boolean elementIcon;





    private gmfgraph_ChildAccess gmfgraph_childaccess;




    private gmfgraph_ChildAccess gmfgraph_childaccess;


    public gmfgraph_DiagramLabel(
        boolean external,        boolean elementIcon    ) {
        super(
        );
        this.external = external;
        this.elementIcon = elementIcon;
    }


    public boolean getExternal() {
        return external;
    }

    public void setExternal(boolean external) {
        this.external = external;
    }
    public boolean getElementicon() {
        return elementIcon;
    }

    public void setElementicon(boolean elementIcon) {
        this.elementIcon = elementIcon;
    }

    public gmfgraph_ChildAccess getGmfgraph_childaccess() {
        return gmfgraph_childaccess;
    }

    public void setGmfgraph_childaccess(gmfgraph_ChildAccess gmfgraph_childaccess) {
        this.gmfgraph_childaccess = gmfgraph_childaccess;
    }
    public gmfgraph_ChildAccess getGmfgraph_childaccess() {
        return gmfgraph_childaccess;
    }

    public void setGmfgraph_childaccess(gmfgraph_ChildAccess gmfgraph_childaccess) {
        this.gmfgraph_childaccess = gmfgraph_childaccess;
    }

}