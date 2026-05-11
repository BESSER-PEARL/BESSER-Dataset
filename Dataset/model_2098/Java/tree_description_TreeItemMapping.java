





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeItemMapping extends description_TreeMapping, description_StyleUpdater, description_TreeItemUpdater, description_TreeItemMappingContainer {

    private String semanticCandidatesExpression;
    private String preconditionExpression;
    private String domainClass;



    public tree_description_TreeItemMapping(
        String semanticCandidatesExpression,        String preconditionExpression,        String domainClass    ) {
        super(
        );
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.preconditionExpression = preconditionExpression;
        this.domainClass = domainClass;
    }


    public String getSemanticcandidatesexpression() {
        return semanticCandidatesExpression;
    }

    public void setSemanticcandidatesexpression(String semanticCandidatesExpression) {
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


}