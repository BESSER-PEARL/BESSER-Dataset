





import java.util.List;
import java.util.ArrayList;

public class RefUML_InstanceSpecification extends PackageableElement {






    private RefUML_Slot refuml_slot;




    private List<RefUML_Classifier> refuml_classifiers;




    private List<RefUML_Slot> refuml_slots;




    private RefUML_ValueSpecification refuml_valuespecification;


    public RefUML_InstanceSpecification(
    ) {
        super(
        );
        this.refuml_classifiers = new ArrayList<>();
        this.refuml_slots = new ArrayList<>();
    }

    public RefUML_InstanceSpecification(
        ArrayList<RefUML_Classifier> refuml_classifiers,        ArrayList<RefUML_Slot> refuml_slots    ) {
        this.refuml_classifiers = refuml_classifiers;
        this.refuml_slots = refuml_slots;
    }


    public RefUML_Slot getRefuml_slot() {
        return refuml_slot;
    }

    public void setRefuml_slot(RefUML_Slot refuml_slot) {
        this.refuml_slot = refuml_slot;
    }
    public List<RefUML_Classifier> getRefuml_classifiers() {
        return refuml_classifiers;
    }

    public void addRefuml_classifier(Refuml_classifier refuml_classifier) {
        this.refuml_classifiers.add(refuml_classifier);
    }
    public List<RefUML_Slot> getRefuml_slots() {
        return refuml_slots;
    }

    public void addRefuml_slot(Refuml_slot refuml_slot) {
        this.refuml_slots.add(refuml_slot);
    }
    public RefUML_ValueSpecification getRefuml_valuespecification() {
        return refuml_valuespecification;
    }

    public void setRefuml_valuespecification(RefUML_ValueSpecification refuml_valuespecification) {
        this.refuml_valuespecification = refuml_valuespecification;
    }

}