





import java.util.List;
import java.util.ArrayList;

public class UML2_RedefinableElement extends NamedElement {

    private boolean isLeaf;



    public UML2_RedefinableElement(
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