





import java.util.List;
import java.util.ArrayList;

public class PolicyEngine_Sensor extends HasIntegerValue {






    private PolicyEngine_AccessControl policyengine_accesscontrol;




    private PolicyEngine_Policy policyengine_policy;




    private PolicyEngine_CTS policyengine_cts;


    public PolicyEngine_Sensor(
    ) {
        super(
        );
    }



    public PolicyEngine_AccessControl getPolicyengine_accesscontrol() {
        return policyengine_accesscontrol;
    }

    public void setPolicyengine_accesscontrol(PolicyEngine_AccessControl policyengine_accesscontrol) {
        this.policyengine_accesscontrol = policyengine_accesscontrol;
    }
    public PolicyEngine_Policy getPolicyengine_policy() {
        return policyengine_policy;
    }

    public void setPolicyengine_policy(PolicyEngine_Policy policyengine_policy) {
        this.policyengine_policy = policyengine_policy;
    }
    public PolicyEngine_CTS getPolicyengine_cts() {
        return policyengine_cts;
    }

    public void setPolicyengine_cts(PolicyEngine_CTS policyengine_cts) {
        this.policyengine_cts = policyengine_cts;
    }

}