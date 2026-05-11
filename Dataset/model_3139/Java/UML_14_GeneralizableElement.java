





import java.util.List;
import java.util.ArrayList;

public class UML_14_GeneralizableElement extends ModelElement {

    private boolean isLeaf;
    private boolean isAbstract;
    private boolean isRoot;



    public UML_14_GeneralizableElement(
        boolean isLeaf,        boolean isAbstract,        boolean isRoot    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.isAbstract = isAbstract;
        this.isRoot = isRoot;
    }


    public boolean getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(boolean isLeaf) {
        this.isLeaf = isLeaf;
    }
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }
    public boolean getIsroot() {
        return isRoot;
    }

    public void setIsroot(boolean isRoot) {
        this.isRoot = isRoot;
    }


}