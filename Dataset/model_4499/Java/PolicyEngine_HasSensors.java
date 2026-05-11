





import java.util.List;
import java.util.ArrayList;

public class PolicyEngine_HasSensors  {






    private List<PolicyEngine_Sensor> policyengine_sensors;


    public PolicyEngine_HasSensors(
    ) {
        this.policyengine_sensors = new ArrayList<>();
    }

    public PolicyEngine_HasSensors(
        ArrayList<PolicyEngine_Sensor> policyengine_sensors    ) {
        this.policyengine_sensors = policyengine_sensors;
    }


    public List<PolicyEngine_Sensor> getPolicyengine_sensors() {
        return policyengine_sensors;
    }

    public void addPolicyengine_sensor(Policyengine_sensor policyengine_sensor) {
        this.policyengine_sensors.add(policyengine_sensor);
    }

}