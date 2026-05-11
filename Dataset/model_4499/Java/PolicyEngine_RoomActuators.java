





import java.util.List;
import java.util.ArrayList;

public class PolicyEngine_RoomActuators extends Expression {






    private PolicyEngine_Room policyengine_room;




    private PolicyEngine_ActuatorComponent policyengine_actuatorcomponent;


    public PolicyEngine_RoomActuators(
    ) {
        super(
        );
    }



    public PolicyEngine_Room getPolicyengine_room() {
        return policyengine_room;
    }

    public void setPolicyengine_room(PolicyEngine_Room policyengine_room) {
        this.policyengine_room = policyengine_room;
    }
    public PolicyEngine_ActuatorComponent getPolicyengine_actuatorcomponent() {
        return policyengine_actuatorcomponent;
    }

    public void setPolicyengine_actuatorcomponent(PolicyEngine_ActuatorComponent policyengine_actuatorcomponent) {
        this.policyengine_actuatorcomponent = policyengine_actuatorcomponent;
    }

}