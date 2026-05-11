





import java.util.List;
import java.util.ArrayList;

public class asmeta_derivedtransitionrules_CaseRule extends BasicDerivedRule {

    private String caseBranches;





    private List<basicterms_Term> basicterms_terms;




    private basictransitionrules_Rule basictransitionrules_rule;




    private basicterms_Term basicterms_term;


    public asmeta_derivedtransitionrules_CaseRule(
        String caseBranches    ) {
        super(
        );
        this.caseBranches = caseBranches;
        this.basicterms_terms = new ArrayList<>();
    }

    public asmeta_derivedtransitionrules_CaseRule(
        String caseBranches        ArrayList<basicterms_Term> basicterms_terms    ) {
        this.caseBranches = caseBranches;
        this.basicterms_terms = basicterms_terms;
    }

    public String getCasebranches() {
        return caseBranches;
    }

    public void setCasebranches(String caseBranches) {
        this.caseBranches = caseBranches;
    }

    public List<basicterms_Term> getBasicterms_terms() {
        return basicterms_terms;
    }

    public void addBasicterms_term(Basicterms_term basicterms_term) {
        this.basicterms_terms.add(basicterms_term);
    }
    public basictransitionrules_Rule getBasictransitionrules_rule() {
        return basictransitionrules_rule;
    }

    public void setBasictransitionrules_rule(basictransitionrules_Rule basictransitionrules_rule) {
        this.basictransitionrules_rule = basictransitionrules_rule;
    }
    public basicterms_Term getBasicterms_term() {
        return basicterms_term;
    }

    public void setBasicterms_term(basicterms_Term basicterms_term) {
        this.basicterms_term = basicterms_term;
    }

}