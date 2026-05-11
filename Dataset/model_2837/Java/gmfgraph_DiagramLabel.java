





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_DiagramLabel extends Node {

    private boolean elementIcon;



    public gmfgraph_DiagramLabel(
        boolean elementIcon    ) {
        super(
        );
        this.elementIcon = elementIcon;
    }


    public boolean getElementicon() {
        return elementIcon;
    }

    public void setElementicon(boolean elementIcon) {
        this.elementIcon = elementIcon;
    }


}