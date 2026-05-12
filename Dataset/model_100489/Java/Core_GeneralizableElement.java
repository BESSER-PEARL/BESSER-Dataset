





import java.util.List;
import java.util.ArrayList;

public class Core_GeneralizableElement extends ModelElement {

    private String isLeaf;
    private String isRoot;
    private String isAbstract;



    public Core_GeneralizableElement(
        String isLeaf,        String isRoot,        String isAbstract    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.isRoot = isRoot;
        this.isAbstract = isAbstract;
    }


    public String getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(String isLeaf) {
        this.isLeaf = isLeaf;
    }
    public String getIsroot() {
        return isRoot;
    }

    public void setIsroot(String isRoot) {
        this.isRoot = isRoot;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }


}