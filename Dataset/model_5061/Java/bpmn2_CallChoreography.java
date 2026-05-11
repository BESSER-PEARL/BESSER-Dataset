





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CallChoreography extends ChoreographyActivity {






    private List<bpmn2_ParticipantAssociation> bpmn2_participantassociations;




    private bpmn2_Choreography bpmn2_choreography;


    public bpmn2_CallChoreography(
    ) {
        super(
        );
        this.bpmn2_participantassociations = new ArrayList<>();
    }

    public bpmn2_CallChoreography(
        ArrayList<bpmn2_ParticipantAssociation> bpmn2_participantassociations    ) {
        this.bpmn2_participantassociations = bpmn2_participantassociations;
    }


    public List<bpmn2_ParticipantAssociation> getBpmn2_participantassociations() {
        return bpmn2_participantassociations;
    }

    public void addBpmn2_participantassociation(Bpmn2_participantassociation bpmn2_participantassociation) {
        this.bpmn2_participantassociations.add(bpmn2_participantassociation);
    }
    public bpmn2_Choreography getBpmn2_choreography() {
        return bpmn2_choreography;
    }

    public void setBpmn2_choreography(bpmn2_Choreography bpmn2_choreography) {
        this.bpmn2_choreography = bpmn2_choreography;
    }

}