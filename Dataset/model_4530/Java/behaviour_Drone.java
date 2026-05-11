





import java.util.List;
import java.util.ArrayList;

public class behaviour_Drone extends NamedElement {

    private String travelMode;
    private String typeName;





    private behaviour_Behaviour behaviour_behaviour;


    public behaviour_Drone(
        String travelMode,        String typeName    ) {
        super(
        );
        this.travelMode = travelMode;
        this.typeName = typeName;
    }


    public String getTravelmode() {
        return travelMode;
    }

    public void setTravelmode(String travelMode) {
        this.travelMode = travelMode;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }

    public behaviour_Behaviour getBehaviour_behaviour() {
        return behaviour_behaviour;
    }

    public void setBehaviour_behaviour(behaviour_Behaviour behaviour_behaviour) {
        this.behaviour_behaviour = behaviour_behaviour;
    }

}