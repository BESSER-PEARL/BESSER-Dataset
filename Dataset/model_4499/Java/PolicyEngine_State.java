





import java.util.List;
import java.util.ArrayList;

public class PolicyEngine_State extends NamedElement {

    private boolean valueState;





    private PolicyEngine_Model policyengine_model;




    private PolicyEngine_Policy policyengine_policy;




    private PolicyEngine_Policy policyengine_policy;


    public PolicyEngine_State(
        boolean valueState    ) {
        super(
        );
        this.valueState = valueState;
    }


    public boolean getValuestate() {
        return valueState;
    }

    public void setValuestate(boolean valueState) {
        this.valueState = valueState;
    }

    public PolicyEngine_Model getPolicyengine_model() {
        return policyengine_model;
    }

    public void setPolicyengine_model(PolicyEngine_Model policyengine_model) {
        this.policyengine_model = policyengine_model;
    }
    public PolicyEngine_Policy getPolicyengine_policy() {
        return policyengine_policy;
    }

    public void setPolicyengine_policy(PolicyEngine_Policy policyengine_policy) {
        this.policyengine_policy = policyengine_policy;
    }
    public PolicyEngine_Policy getPolicyengine_policy() {
        return policyengine_policy;
    }

    public void setPolicyengine_policy(PolicyEngine_Policy policyengine_policy) {
        this.policyengine_policy = policyengine_policy;
    }

}