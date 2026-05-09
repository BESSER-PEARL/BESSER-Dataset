





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_InstanceSpecification extends PackageableElement, DeployedArtifact, DeploymentTarget {






    private UML2WithID_InstanceValue uml2withid_instancevalue;




    private List<UML2WithID_Slot> uml2withid_slots;




    private UML2WithID_ValueSpecification uml2withid_valuespecification;




    private List<UML2WithID_Classifier> uml2withid_classifiers;




    private UML2WithID_Slot uml2withid_slot;


    public UML2WithID_InstanceSpecification(
    ) {
        super(
        );
        this.uml2withid_slots = new ArrayList<>();
        this.uml2withid_classifiers = new ArrayList<>();
    }

    public UML2WithID_InstanceSpecification(
        ArrayList<UML2WithID_Slot> uml2withid_slots,        ArrayList<UML2WithID_Classifier> uml2withid_classifiers    ) {
        this.uml2withid_slots = uml2withid_slots;
        this.uml2withid_classifiers = uml2withid_classifiers;
    }


    public UML2WithID_InstanceValue getUml2withid_instancevalue() {
        return uml2withid_instancevalue;
    }

    public void setUml2withid_instancevalue(UML2WithID_InstanceValue uml2withid_instancevalue) {
        this.uml2withid_instancevalue = uml2withid_instancevalue;
    }
    public List<UML2WithID_Slot> getUml2withid_slots() {
        return uml2withid_slots;
    }

    public void addUml2withid_slot(Uml2withid_slot uml2withid_slot) {
        this.uml2withid_slots.add(uml2withid_slot);
    }
    public UML2WithID_ValueSpecification getUml2withid_valuespecification() {
        return uml2withid_valuespecification;
    }

    public void setUml2withid_valuespecification(UML2WithID_ValueSpecification uml2withid_valuespecification) {
        this.uml2withid_valuespecification = uml2withid_valuespecification;
    }
    public List<UML2WithID_Classifier> getUml2withid_classifiers() {
        return uml2withid_classifiers;
    }

    public void addUml2withid_classifier(Uml2withid_classifier uml2withid_classifier) {
        this.uml2withid_classifiers.add(uml2withid_classifier);
    }
    public UML2WithID_Slot getUml2withid_slot() {
        return uml2withid_slot;
    }

    public void setUml2withid_slot(UML2WithID_Slot uml2withid_slot) {
        this.uml2withid_slot = uml2withid_slot;
    }

}