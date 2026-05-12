





import java.util.List;
import java.util.ArrayList;

public class Core_Operation extends BehavioralFeature {

    private String specification;
    private String concurrency;
    private String isRoot;
    private String isLeaf;
    private String isAbstract;



    public Core_Operation(
        String specification,        String concurrency,        String isRoot,        String isLeaf,        String isAbstract    ) {
        super(
        );
        this.specification = specification;
        this.concurrency = concurrency;
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
    public String getConcurrency() {
        return concurrency;
    }

    public void setConcurrency(String concurrency) {
        this.concurrency = concurrency;
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