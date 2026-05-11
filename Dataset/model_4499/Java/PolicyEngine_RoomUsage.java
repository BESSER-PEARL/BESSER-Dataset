





import java.util.List;
import java.util.ArrayList;

public class PolicyEngine_RoomUsage extends Expression {






    private PolicyEngine_Actuator policyengine_actuator;




    private PolicyEngine_State policyengine_state;




    private PolicyEngine_Sensor policyengine_sensor;


    public PolicyEngine_RoomUsage(
    ) {
        super(
        );
    }



    public PolicyEngine_Actuator getPolicyengine_actuator() {
        return policyengine_actuator;
    }

    public void setPolicyengine_actuator(PolicyEngine_Actuator policyengine_actuator) {
        this.policyengine_actuator = policyengine_actuator;
    }
    public PolicyEngine_State getPolicyengine_state() {
        return policyengine_state;
    }

    public void setPolicyengine_state(PolicyEngine_State policyengine_state) {
        this.policyengine_state = policyengine_state;
    }
    public PolicyEngine_Sensor getPolicyengine_sensor() {
        return policyengine_sensor;
    }

    public void setPolicyengine_sensor(PolicyEngine_Sensor policyengine_sensor) {
        this.policyengine_sensor = policyengine_sensor;
    }

}