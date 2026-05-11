





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeItemMapping extends description_StyleUpdater, description_TreeMapping, description_TreeItemUpdater, description_TreeItemMappingContainer {

    private String preconditionExpression;
    private String domainClass;
    private String semanticCandidatesExpression;



    public tree_description_TreeItemMapping(
        String preconditionExpression,        String domainClass,        String semanticCandidatesExpression    ) {
        super(
        );
        this.preconditionExpression = preconditionExpression;
        this.domainClass = domainClass;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
    }


    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }
    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }
    public String getSemanticcandidatesexpression() {
        return semanticCandidatesExpression;
    }

    public void setSemanticcandidatesexpression(String semanticCandidatesExpression) {
        this.semanticCandidatesExpression = semanticCandidatesExpression;
    }


}