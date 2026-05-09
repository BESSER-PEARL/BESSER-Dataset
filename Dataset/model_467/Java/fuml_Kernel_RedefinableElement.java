





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_RedefinableElement extends NamedElement {

    private boolean leaf;



    public fuml_Kernel_RedefinableElement(
        boolean leaf    ) {
        super(
        );
        this.leaf = leaf;
    }


    public boolean getLeaf() {
        return leaf;
    }

    public void setLeaf(boolean leaf) {
        this.leaf = leaf;
    }


}