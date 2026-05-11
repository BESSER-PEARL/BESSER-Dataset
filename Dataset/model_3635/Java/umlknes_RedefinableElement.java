





import java.util.List;
import java.util.ArrayList;

public class umlknes_RedefinableElement extends NamedElement {

    private boolean isLeaf;



    public umlknes_RedefinableElement(
        boolean isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
    }


    public boolean getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(boolean isLeaf) {
        this.isLeaf = isLeaf;
    }


}