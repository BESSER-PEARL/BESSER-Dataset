





import java.util.List;
import java.util.ArrayList;

public class notation_MindMapNode extends Node {

    private int side;
    private boolean expanded;
    private boolean hasChildren;



    public notation_MindMapNode(
        int side,        boolean expanded,        boolean hasChildren    ) {
        super(
        );
        this.side = side;
        this.expanded = expanded;
        this.hasChildren = hasChildren;
    }


    public int getSide() {
        return side;
    }

    public void setSide(int side) {
        this.side = side;
    }
    public boolean getExpanded() {
        return expanded;
    }

    public void setExpanded(boolean expanded) {
        this.expanded = expanded;
    }
    public boolean getHaschildren() {
        return hasChildren;
    }

    public void setHaschildren(boolean hasChildren) {
        this.hasChildren = hasChildren;
    }


}