





import java.util.List;
import java.util.ArrayList;

public class foundation_core_Classifier extends core_GeneralizableElement, core_Namespace {






    private List<Collaboration> collaborations;




    private List<CreateAction> createactions;




    private List<Generalization_> generalization_s;


    public foundation_core_Classifier(
    ) {
        super(
        );
        this.collaborations = new ArrayList<>();
        this.createactions = new ArrayList<>();
        this.generalization_s = new ArrayList<>();
    }

    public foundation_core_Classifier(
        ArrayList<Collaboration> collaborations,        ArrayList<CreateAction> createactions,        ArrayList<Generalization_> generalization_s    ) {
        this.collaborations = collaborations;
        this.createactions = createactions;
        this.generalization_s = generalization_s;
    }


    public List<Collaboration> getCollaborations() {
        return collaborations;
    }

    public void addCollaboration(Collaboration collaboration) {
        this.collaborations.add(collaboration);
    }
    public List<CreateAction> getCreateactions() {
        return createactions;
    }

    public void addCreateaction(Createaction createaction) {
        this.createactions.add(createaction);
    }
    public List<Generalization_> getGeneralization_s() {
        return generalization_s;
    }

    public void addGeneralization_(Generalization_ generalization_) {
        this.generalization_s.add(generalization_);
    }

}