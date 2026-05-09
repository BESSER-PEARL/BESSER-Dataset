





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_InstanceSpecification extends DeployedArtifact, DeploymentTarget, PackageableElement {






    private uml3_0_0_Slot uml3_0_0_slot;




    private List<uml3_0_0_Classifier> uml3_0_0_classifiers;




    private List<uml3_0_0_Slot> uml3_0_0_slots;


    public uml3_0_0_InstanceSpecification(
    ) {
        super(
        );
        this.uml3_0_0_classifiers = new ArrayList<>();
        this.uml3_0_0_slots = new ArrayList<>();
    }

    public uml3_0_0_InstanceSpecification(
        ArrayList<uml3_0_0_Classifier> uml3_0_0_classifiers,        ArrayList<uml3_0_0_Slot> uml3_0_0_slots    ) {
        this.uml3_0_0_classifiers = uml3_0_0_classifiers;
        this.uml3_0_0_slots = uml3_0_0_slots;
    }


    public uml3_0_0_Slot getUml3_0_0_slot() {
        return uml3_0_0_slot;
    }

    public void setUml3_0_0_slot(uml3_0_0_Slot uml3_0_0_slot) {
        this.uml3_0_0_slot = uml3_0_0_slot;
    }
    public List<uml3_0_0_Classifier> getUml3_0_0_classifiers() {
        return uml3_0_0_classifiers;
    }

    public void addUml3_0_0_classifier(Uml3_0_0_classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifiers.add(uml3_0_0_classifier);
    }
    public List<uml3_0_0_Slot> getUml3_0_0_slots() {
        return uml3_0_0_slots;
    }

    public void addUml3_0_0_slot(Uml3_0_0_slot uml3_0_0_slot) {
        this.uml3_0_0_slots.add(uml3_0_0_slot);
    }

}