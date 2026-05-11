





import java.util.List;
import java.util.ArrayList;

public class esper_Name  {

    private String name;





    private esper_RuleParts esper_ruleparts;


    public esper_Name(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public esper_RuleParts getEsper_ruleparts() {
        return esper_ruleparts;
    }

    public void setEsper_ruleparts(esper_RuleParts esper_ruleparts) {
        this.esper_ruleparts = esper_ruleparts;
    }

}