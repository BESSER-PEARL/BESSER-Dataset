





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_common_behavior_Reception extends BehavioralFeature {

    private String isLeaf;
    private String isRoot;
    private String isAbstract;
    private String specification;



    public behavioral_elements_common_behavior_Reception(
        String isLeaf,        String isRoot,        String isAbstract,        String specification    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.isRoot = isRoot;
        this.isAbstract = isAbstract;
        this.specification = specification;
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
    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }


}