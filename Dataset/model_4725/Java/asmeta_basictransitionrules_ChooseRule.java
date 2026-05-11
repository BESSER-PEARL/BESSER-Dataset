





import java.util.List;
import java.util.ArrayList;

public class asmeta_basictransitionrules_ChooseRule extends BasicRule {

    private String ranges;





    private List<basicterms_VariableTerm> basicterms_variableterms;




    private basicterms_Term basicterms_term;




    private basictransitionrules_Rule basictransitionrules_rule;




    private basictransitionrules_Rule basictransitionrules_rule;


    public asmeta_basictransitionrules_ChooseRule(
        String ranges    ) {
        super(
        );
        this.ranges = ranges;
        this.basicterms_variableterms = new ArrayList<>();
    }

    public asmeta_basictransitionrules_ChooseRule(
        String ranges        ArrayList<basicterms_VariableTerm> basicterms_variableterms    ) {
        this.ranges = ranges;
        this.basicterms_variableterms = basicterms_variableterms;
    }

    public String getRanges() {
        return ranges;
    }

    public void setRanges(String ranges) {
        this.ranges = ranges;
    }

    public List<basicterms_VariableTerm> getBasicterms_variableterms() {
        return basicterms_variableterms;
    }

    public void addBasicterms_variableterm(Basicterms_variableterm basicterms_variableterm) {
        this.basicterms_variableterms.add(basicterms_variableterm);
    }
    public basicterms_Term getBasicterms_term() {
        return basicterms_term;
    }

    public void setBasicterms_term(basicterms_Term basicterms_term) {
        this.basicterms_term = basicterms_term;
    }
    public basictransitionrules_Rule getBasictransitionrules_rule() {
        return basictransitionrules_rule;
    }

    public void setBasictransitionrules_rule(basictransitionrules_Rule basictransitionrules_rule) {
        this.basictransitionrules_rule = basictransitionrules_rule;
    }
    public basictransitionrules_Rule getBasictransitionrules_rule() {
        return basictransitionrules_rule;
    }

    public void setBasictransitionrules_rule(basictransitionrules_Rule basictransitionrules_rule) {
        this.basictransitionrules_rule = basictransitionrules_rule;
    }

}