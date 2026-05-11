





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeItemMapping extends description_StyleUpdater, description_TreeItemUpdater, description_TreeItemMappingContainer, description_TreeMapping {

    private String domainClass;
    private String preconditionExpression;
    private String semanticCandidatesExpression;



    public tree_description_TreeItemMapping(
        String domainClass,        String preconditionExpression,        String semanticCandidatesExpression    ) {
        super(
        );
        this.domainClass = domainClass;
        this.preconditionExpression = preconditionExpression;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
    }


    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }
    public String getSemanticcandidatesexpression() {
        return semanticCandidatesExpression;
    }

    public void setSemanticcandidatesexpression(String semanticCandidatesExpression) {
        this.semanticCandidatesExpression = semanticCandidatesExpression;
    }


}