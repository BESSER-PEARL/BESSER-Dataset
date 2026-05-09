





import java.util.List;
import java.util.ArrayList;

public class foundation_core_Operation extends BehavioralFeature {

    private String concurrency;
    private String isLeaf;
    private String isRoot;
    private String specification;
    private String isAbstract;





    private List<Collaboration> collaborations;


    public foundation_core_Operation(
        String concurrency,        String isLeaf,        String isRoot,        String specification,        String isAbstract    ) {
        super(
        );
        this.concurrency = concurrency;
        this.isLeaf = isLeaf;
        this.isRoot = isRoot;
        this.specification = specification;
        this.isAbstract = isAbstract;
        this.collaborations = new ArrayList<>();
    }

    public foundation_core_Operation(
        String concurrency,        String isLeaf,        String isRoot,        String specification,        String isAbstract        ArrayList<Collaboration> collaborations    ) {
        this.concurrency = concurrency;
        this.isLeaf = isLeaf;
        this.isRoot = isRoot;
        this.specification = specification;
        this.isAbstract = isAbstract;
        this.collaborations = collaborations;
    }

    public String getConcurrency() {
        return concurrency;
    }

    public void setConcurrency(String concurrency) {
        this.concurrency = concurrency;
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
    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<Collaboration> getCollaborations() {
        return collaborations;
    }

    public void addCollaboration(Collaboration collaboration) {
        this.collaborations.add(collaboration);
    }

}