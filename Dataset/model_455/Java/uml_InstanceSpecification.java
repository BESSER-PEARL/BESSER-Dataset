





import java.util.List;
import java.util.ArrayList;

public class uml_InstanceSpecification extends DeploymentTarget, PackageableElement, DeployedArtifact {






    private List<uml_Slot> uml_slots;




    private List<uml_Classifier> uml_classifiers;




    private uml_Slot uml_slot;


    public uml_InstanceSpecification(
    ) {
        super(
        );
        this.uml_slots = new ArrayList<>();
        this.uml_classifiers = new ArrayList<>();
    }

    public uml_InstanceSpecification(
        ArrayList<uml_Slot> uml_slots,        ArrayList<uml_Classifier> uml_classifiers    ) {
        this.uml_slots = uml_slots;
        this.uml_classifiers = uml_classifiers;
    }


    public List<uml_Slot> getUml_slots() {
        return uml_slots;
    }

    public void addUml_slot(Uml_slot uml_slot) {
        this.uml_slots.add(uml_slot);
    }
    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }
    public uml_Slot getUml_slot() {
        return uml_slot;
    }

    public void setUml_slot(uml_Slot uml_slot) {
        this.uml_slot = uml_slot;
    }

}