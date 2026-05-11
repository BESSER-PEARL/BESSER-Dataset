





import java.util.List;
import java.util.ArrayList;

public class dSLPolicies_GraphElement  {

    private String name;





    private dSLPolicies_StopCondition dslpolicies_stopcondition;


    public dSLPolicies_GraphElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dSLPolicies_StopCondition getDslpolicies_stopcondition() {
        return dslpolicies_stopcondition;
    }

    public void setDslpolicies_stopcondition(dSLPolicies_StopCondition dslpolicies_stopcondition) {
        this.dslpolicies_stopcondition = dslpolicies_stopcondition;
    }

}