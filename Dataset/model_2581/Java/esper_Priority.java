





import java.util.List;
import java.util.ArrayList;

public class esper_Priority  {

    private int priorityInt;





    private esper_RuleParts esper_ruleparts;


    public esper_Priority(
        int priorityInt    ) {
        this.priorityInt = priorityInt;
    }


    public int getPriorityint() {
        return priorityInt;
    }

    public void setPriorityint(int priorityInt) {
        this.priorityInt = priorityInt;
    }

    public esper_RuleParts getEsper_ruleparts() {
        return esper_ruleparts;
    }

    public void setEsper_ruleparts(esper_RuleParts esper_ruleparts) {
        this.esper_ruleparts = esper_ruleparts;
    }

}