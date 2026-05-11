





import java.util.List;
import java.util.ArrayList;

public class table_description_ElementColumnMapping extends description_ColumnMapping, description_StyleUpdater {

    private String domainClass;
    private String semanticCandidatesExpression;



    public table_description_ElementColumnMapping(
        String domainClass,        String semanticCandidatesExpression    ) {
        super(
        );
        this.domainClass = domainClass;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
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