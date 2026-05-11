





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_DiagramLabel extends Node {

    private boolean external;
    private boolean elementIcon;



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


}