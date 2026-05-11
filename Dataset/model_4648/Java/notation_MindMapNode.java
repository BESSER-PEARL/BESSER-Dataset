





import java.util.List;
import java.util.ArrayList;

public class notation_MindMapNode extends Node {

    private int side;
    private boolean hasChildren;
    private boolean expanded;



    public notation_MindMapNode(
        int side,        boolean hasChildren,        boolean expanded    ) {
        super(
        );
        this.side = side;
        this.hasChildren = hasChildren;
        this.expanded = expanded;
    }


    public int getSide() {
        return side;
    }

    public void setSide(int side) {
        this.side = side;
    }
    public boolean getHaschildren() {
        return hasChildren;
    }

    public void setHaschildren(boolean hasChildren) {
        this.hasChildren = hasChildren;
    }
    public boolean getExpanded() {
        return expanded;
    }

    public void setExpanded(boolean expanded) {
        this.expanded = expanded;
    }


}