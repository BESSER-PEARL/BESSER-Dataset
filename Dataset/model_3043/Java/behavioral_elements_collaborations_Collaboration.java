





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_collaborations_Collaboration extends core_Namespace, core_GeneralizableElement {






    private List<Collaboration> collaborations;




    private Classifier classifier;




    private Operation operation;




    private List<ModelElement> modelelements;




    private List<CollaborationInstanceSet> collaborationinstancesets;


    public behavioral_elements_collaborations_Collaboration(
    ) {
        super(
        );
        this.collaborations = new ArrayList<>();
        this.modelelements = new ArrayList<>();
        this.collaborationinstancesets = new ArrayList<>();
    }

    public behavioral_elements_collaborations_Collaboration(
        ArrayList<Collaboration> collaborations,        ArrayList<ModelElement> modelelements,        ArrayList<CollaborationInstanceSet> collaborationinstancesets    ) {
        this.collaborations = collaborations;
        this.modelelements = modelelements;
        this.collaborationinstancesets = collaborationinstancesets;
    }


    public List<Collaboration> getCollaborations() {
        return collaborations;
    }

    public void addCollaboration(Collaboration collaboration) {
        this.collaborations.add(collaboration);
    }
    public Classifier getClassifier() {
        return classifier;
    }

    public void setClassifier(Classifier classifier) {
        this.classifier = classifier;
    }
    public Operation getOperation() {
        return operation;
    }

    public void setOperation(Operation operation) {
        this.operation = operation;
    }
    public List<ModelElement> getModelelements() {
        return modelelements;
    }

    public void addModelelement(Modelelement modelelement) {
        this.modelelements.add(modelelement);
    }
    public List<CollaborationInstanceSet> getCollaborationinstancesets() {
        return collaborationinstancesets;
    }

    public void addCollaborationinstanceset(Collaborationinstanceset collaborationinstanceset) {
        this.collaborationinstancesets.add(collaborationinstanceset);
    }

}