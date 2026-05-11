





import java.util.List;
import java.util.ArrayList;

public class UML_14_Operation extends BehavioralFeature {

    private String specification;
    private boolean isRoot;
    private boolean isLeaf;
    private boolean isAbstract;



    public UML_14_Operation(
        String specification,        boolean isRoot,        boolean isLeaf,        boolean isAbstract    ) {
        super(
        );
        this.specification = specification;
        this.isRoot = isRoot;
        this.isLeaf = isLeaf;
        this.isAbstract = isAbstract;
    }


    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
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