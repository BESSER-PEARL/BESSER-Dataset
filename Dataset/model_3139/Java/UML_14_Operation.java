





import java.util.List;
import java.util.ArrayList;

public class UML_14_Operation extends BehavioralFeature {

    private boolean isAbstract;
    private boolean isRoot;
    private boolean isLeaf;
    private String specification;



    public UML_14_Operation(
        boolean isAbstract,        boolean isRoot,        boolean isLeaf,        String specification    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.isRoot = isRoot;
        this.isLeaf = isLeaf;
        this.specification = specification;
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
    public boolean getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(boolean isLeaf) {
        this.isLeaf = isLeaf;
    }
    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }


}