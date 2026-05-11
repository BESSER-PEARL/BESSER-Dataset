





import java.util.List;
import java.util.ArrayList;

public class asmeta_definitions_RuleDeclaration extends Classifier {

    private String arity;





    private List<basicterms_VariableTerm> basicterms_variableterms;




    private Body body;




    private basictransitionrules_Rule basictransitionrules_rule;


    public asmeta_definitions_RuleDeclaration(
        String arity    ) {
        super(
        );
        this.arity = arity;
        this.basicterms_variableterms = new ArrayList<>();
    }

    public asmeta_definitions_RuleDeclaration(
        String arity        ArrayList<basicterms_VariableTerm> basicterms_variableterms    ) {
        this.arity = arity;
        this.basicterms_variableterms = basicterms_variableterms;
    }

    public String getArity() {
        return arity;
    }

    public void setArity(String arity) {
        this.arity = arity;
    }

    public List<basicterms_VariableTerm> getBasicterms_variableterms() {
        return basicterms_variableterms;
    }

    public void addBasicterms_variableterm(Basicterms_variableterm basicterms_variableterm) {
        this.basicterms_variableterms.add(basicterms_variableterm);
    }
    public Body getBody() {
        return body;
    }

    public void setBody(Body body) {
        this.body = body;
    }
    public basictransitionrules_Rule getBasictransitionrules_rule() {
        return basictransitionrules_rule;
    }

    public void setBasictransitionrules_rule(basictransitionrules_Rule basictransitionrules_rule) {
        this.basictransitionrules_rule = basictransitionrules_rule;
    }

}