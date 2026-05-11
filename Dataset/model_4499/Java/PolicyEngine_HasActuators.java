





import java.util.List;
import java.util.ArrayList;

public class PolicyEngine_HasActuators  {






    private List<PolicyEngine_Actuator> policyengine_actuators;


    public PolicyEngine_HasActuators(
    ) {
        this.policyengine_actuators = new ArrayList<>();
    }

    public PolicyEngine_HasActuators(
        ArrayList<PolicyEngine_Actuator> policyengine_actuators    ) {
        this.policyengine_actuators = policyengine_actuators;
    }


    public List<PolicyEngine_Actuator> getPolicyengine_actuators() {
        return policyengine_actuators;
    }

    public void addPolicyengine_actuator(Policyengine_actuator policyengine_actuator) {
        this.policyengine_actuators.add(policyengine_actuator);
    }

}