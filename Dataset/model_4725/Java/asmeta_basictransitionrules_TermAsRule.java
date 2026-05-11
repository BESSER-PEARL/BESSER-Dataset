





import java.util.List;
import java.util.ArrayList;

public class asmeta_basictransitionrules_TermAsRule extends Rule {

    private String parameters;





    private basicterms_Term basicterms_term;


    public asmeta_basictransitionrules_TermAsRule(
        String parameters    ) {
        super(
        );
        this.parameters = parameters;
    }


    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }

    public basicterms_Term getBasicterms_term() {
        return basicterms_term;
    }

    public void setBasicterms_term(basicterms_Term basicterms_term) {
        this.basicterms_term = basicterms_term;
    }

}