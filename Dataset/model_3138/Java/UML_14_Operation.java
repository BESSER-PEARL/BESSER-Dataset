





import java.util.List;
import java.util.ArrayList;

public class UML_14_Operation extends BehavioralFeature {

    private boolean isRoot;
    private String specification;
    private boolean isAbstract;
    private boolean isLeaf;



    public UML_14_Operation(
        boolean isRoot,        String specification,        boolean isAbstract,        boolean isLeaf    ) {
        super(
        );
        this.isRoot = isRoot;
        this.specification = specification;
        this.isAbstract = isAbstract;
        this.isLeaf = isLeaf;
    }


    public boolean getIsroot() {
        return isRoot;
    }

    public void setIsroot(boolean isRoot) {
        this.isRoot = isRoot;
    }
    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }
    public boolean getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(boolean isLeaf) {
        this.isLeaf = isLeaf;
    }


}