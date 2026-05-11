





import java.util.List;
import java.util.ArrayList;

public class asmeta_basictransitionrules_LetRule extends BasicRule {






    private basictransitionrules_Rule basictransitionrules_rule;




    private List<basicterms_Term> basicterms_terms;




    private List<basicterms_VariableTerm> basicterms_variableterms;


    public asmeta_basictransitionrules_LetRule(
    ) {
        super(
        );
        this.basicterms_terms = new ArrayList<>();
        this.basicterms_variableterms = new ArrayList<>();
    }

    public asmeta_basictransitionrules_LetRule(
        ArrayList<basicterms_Term> basicterms_terms,        ArrayList<basicterms_VariableTerm> basicterms_variableterms    ) {
        this.basicterms_terms = basicterms_terms;
        this.basicterms_variableterms = basicterms_variableterms;
    }


    public basictransitionrules_Rule getBasictransitionrules_rule() {
        return basictransitionrules_rule;
    }

    public void setBasictransitionrules_rule(basictransitionrules_Rule basictransitionrules_rule) {
        this.basictransitionrules_rule = basictransitionrules_rule;
    }
    public List<basicterms_Term> getBasicterms_terms() {
        return basicterms_terms;
    }

    public void addBasicterms_term(Basicterms_term basicterms_term) {
        this.basicterms_terms.add(basicterms_term);
    }
    public List<basicterms_VariableTerm> getBasicterms_variableterms() {
        return basicterms_variableterms;
    }

    public void addBasicterms_variableterm(Basicterms_variableterm basicterms_variableterm) {
        this.basicterms_variableterms.add(basicterms_variableterm);
    }

}