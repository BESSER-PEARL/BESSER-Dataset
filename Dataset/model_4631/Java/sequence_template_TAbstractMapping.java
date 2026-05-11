





import java.util.List;
import java.util.ArrayList;

public class sequence_template_TAbstractMapping extends TTransformer {

    private String name;
    private String semanticCandidatesExpression;
    private String domainClass;



    public sequence_template_TAbstractMapping(
        String name,        String semanticCandidatesExpression,        String domainClass    ) {
        super(
        );
        this.name = name;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.domainClass = domainClass;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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