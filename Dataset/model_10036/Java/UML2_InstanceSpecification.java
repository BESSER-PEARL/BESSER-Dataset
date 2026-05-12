





import java.util.List;
import java.util.ArrayList;

public class UML2_InstanceSpecification extends DeployedArtifact, DeploymentTarget, PackageableElement {






    private List<UML2_Slot> uml2_slots;




    private List<UML2_Classifier> uml2_classifiers;


    public UML2_InstanceSpecification(
    ) {
        super(
        );
        this.uml2_slots = new ArrayList<>();
        this.uml2_classifiers = new ArrayList<>();
    }

    public UML2_InstanceSpecification(
        ArrayList<UML2_Slot> uml2_slots,        ArrayList<UML2_Classifier> uml2_classifiers    ) {
        this.uml2_slots = uml2_slots;
        this.uml2_classifiers = uml2_classifiers;
    }


    public List<UML2_Slot> getUml2_slots() {
        return uml2_slots;
    }

    public void addUml2_slot(Uml2_slot uml2_slot) {
        this.uml2_slots.add(uml2_slot);
    }
    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }

}