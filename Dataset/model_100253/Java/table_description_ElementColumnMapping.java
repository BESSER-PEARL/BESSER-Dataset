





import java.util.List;
import java.util.ArrayList;

public class table_description_ElementColumnMapping extends description_StyleUpdater, description_ColumnMapping {

    private String semanticCandidatesExpression;
    private String domainClass;



    public table_description_ElementColumnMapping(
        String semanticCandidatesExpression,        String domainClass    ) {
        super(
        );
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.domainClass = domainClass;
    }


    public String getSemanticcandidatesexpression() {
        return semanticCandidatesExpression;
    }

    public void setSemanticcandidatesexpression(String semanticCandidatesExpression) {
        this.semanticCandidatesExpression = semanticCandidatesExpression;
    }
    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }


}