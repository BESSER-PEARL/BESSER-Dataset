





import java.util.List;
import java.util.ArrayList;

public class dronesStructure_Scenario extends NamedElement {

    private float safeCommunicationDistance;
    private float maximumCommunicationDistance;





    private dronesStructure_DronesStructure dronesstructure_dronesstructure;


    public dronesStructure_Scenario(
        float safeCommunicationDistance,        float maximumCommunicationDistance    ) {
        super(
        );
        this.safeCommunicationDistance = safeCommunicationDistance;
        this.maximumCommunicationDistance = maximumCommunicationDistance;
    }


    public float getSafecommunicationdistance() {
        return safeCommunicationDistance;
    }

    public void setSafecommunicationdistance(float safeCommunicationDistance) {
        this.safeCommunicationDistance = safeCommunicationDistance;
    }
    public float getMaximumcommunicationdistance() {
        return maximumCommunicationDistance;
    }

    public void setMaximumcommunicationdistance(float maximumCommunicationDistance) {
        this.maximumCommunicationDistance = maximumCommunicationDistance;
    }

    public dronesStructure_DronesStructure getDronesstructure_dronesstructure() {
        return dronesstructure_dronesstructure;
    }

    public void setDronesstructure_dronesstructure(dronesStructure_DronesStructure dronesstructure_dronesstructure) {
        this.dronesstructure_dronesstructure = dronesstructure_dronesstructure;
    }

}