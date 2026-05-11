





import java.util.List;
import java.util.ArrayList;

public class dSLPolicies_Severity  {

    private String level;





    private dSLPolicies_Policies dslpolicies_policies;


    public dSLPolicies_Severity(
        String level    ) {
        this.level = level;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }

    public dSLPolicies_Policies getDslpolicies_policies() {
        return dslpolicies_policies;
    }

    public void setDslpolicies_policies(dSLPolicies_Policies dslpolicies_policies) {
        this.dslpolicies_policies = dslpolicies_policies;
    }

}