





import java.util.List;
import java.util.ArrayList;

public class Core_GeneralizableElement extends ModelElement {

    private String isAbstract;
    private String isRoot;
    private String isLeaf;



    public Core_GeneralizableElement(
        String isAbstract,        String isRoot,        String isLeaf    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.isRoot = isRoot;
        this.isLeaf = isLeaf;
    }


    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getIsroot() {
        return isRoot;
    }

    public void setIsroot(String isRoot) {
        this.isRoot = isRoot;
    }
    public String getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(String isLeaf) {
        this.isLeaf = isLeaf;
    }


}