





import java.util.List;
import java.util.ArrayList;

public class esper_Having  {

    private String operator;





    private esper_RuleParts esper_ruleparts;


    public esper_Having(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public esper_RuleParts getEsper_ruleparts() {
        return esper_ruleparts;
    }

    public void setEsper_ruleparts(esper_RuleParts esper_ruleparts) {
        this.esper_ruleparts = esper_ruleparts;
    }

}