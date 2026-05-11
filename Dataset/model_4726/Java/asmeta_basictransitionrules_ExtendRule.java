





import java.util.List;
import java.util.ArrayList;

public class asmeta_basictransitionrules_ExtendRule extends BasicRule {






    private List<basicterms_VariableTerm> basicterms_variableterms;




    private basictransitionrules_Rule basictransitionrules_rule;




    private domains_Domain domains_domain;


    public asmeta_basictransitionrules_ExtendRule(
    ) {
        super(
        );
        this.basicterms_variableterms = new ArrayList<>();
    }

    public asmeta_basictransitionrules_ExtendRule(
        ArrayList<basicterms_VariableTerm> basicterms_variableterms    ) {
        this.basicterms_variableterms = basicterms_variableterms;
    }


    public List<basicterms_VariableTerm> getBasicterms_variableterms() {
        return basicterms_variableterms;
    }

    public void addBasicterms_variableterm(Basicterms_variableterm basicterms_variableterm) {
        this.basicterms_variableterms.add(basicterms_variableterm);
    }
    public basictransitionrules_Rule getBasictransitionrules_rule() {
        return basictransitionrules_rule;
    }

    public void setBasictransitionrules_rule(basictransitionrules_Rule basictransitionrules_rule) {
        this.basictransitionrules_rule = basictransitionrules_rule;
    }
    public domains_Domain getDomains_domain() {
        return domains_domain;
    }

    public void setDomains_domain(domains_Domain domains_domain) {
        this.domains_domain = domains_domain;
    }

}