





import java.util.List;
import java.util.ArrayList;

public class UML_14_GeneralizableElement extends ModelElement {

    private boolean isRoot;
    private boolean isLeaf;
    private boolean isAbstract;



    public UML_14_GeneralizableElement(
        boolean isRoot,        boolean isLeaf,        boolean isAbstract    ) {
        super(
        );
        this.isRoot = isRoot;
        this.isLeaf = isLeaf;
        this.isAbstract = isAbstract;
    }


    public boolean getIsroot() {
        return isRoot;
    }

    public void setIsroot(boolean isRoot) {
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


}