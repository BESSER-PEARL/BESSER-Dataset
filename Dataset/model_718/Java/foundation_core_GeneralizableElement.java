





import java.util.List;
import java.util.ArrayList;

public class foundation_core_GeneralizableElement extends ModelElement {

    private String isRoot;
    private String isLeaf;
    private String isAbstract;



    public foundation_core_GeneralizableElement(
        String isRoot,        String isLeaf,        String isAbstract    ) {
        super(
        );
        this.isRoot = isRoot;
        this.isLeaf = isLeaf;
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
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }


}