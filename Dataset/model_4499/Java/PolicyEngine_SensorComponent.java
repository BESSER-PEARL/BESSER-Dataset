





import java.util.List;
import java.util.ArrayList;

public class PolicyEngine_SensorComponent extends HasSensors, NamedElement {






    private PolicyEngine_Room policyengine_room;


    public PolicyEngine_SensorComponent(
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

}