





import java.util.List;
import java.util.ArrayList;

public class esper_Select  {

    private boolean asterisk;
    private String alias;





    private esper_RuleParts esper_ruleparts;


    public esper_Select(
        boolean asterisk,        String alias    ) {
        this.asterisk = asterisk;
        this.alias = alias;
    }


    public boolean getAsterisk() {
        return asterisk;
    }

    public void setAsterisk(boolean asterisk) {
        this.asterisk = asterisk;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }

    public esper_RuleParts getEsper_ruleparts() {
        return esper_ruleparts;
    }

    public void setEsper_ruleparts(esper_RuleParts esper_ruleparts) {
        this.esper_ruleparts = esper_ruleparts;
    }

}