





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_InstanceSpecification extends PackageableElement {






    private RefOntoUML_ValueSpecification refontouml_valuespecification;




    private List<RefOntoUML_Classifier> refontouml_classifiers;




    private List<RefOntoUML_Slot> refontouml_slots;




    private RefOntoUML_Slot refontouml_slot;


    public RefOntoUML_InstanceSpecification(
    ) {
        super(
        );
        this.refontouml_classifiers = new ArrayList<>();
        this.refontouml_slots = new ArrayList<>();
    }

    public RefOntoUML_InstanceSpecification(
        ArrayList<RefOntoUML_Classifier> refontouml_classifiers,        ArrayList<RefOntoUML_Slot> refontouml_slots    ) {
        this.refontouml_classifiers = refontouml_classifiers;
        this.refontouml_slots = refontouml_slots;
    }


    public RefOntoUML_ValueSpecification getRefontouml_valuespecification() {
        return refontouml_valuespecification;
    }

    public void setRefontouml_valuespecification(RefOntoUML_ValueSpecification refontouml_valuespecification) {
        this.refontouml_valuespecification = refontouml_valuespecification;
    }
    public List<RefOntoUML_Classifier> getRefontouml_classifiers() {
        return refontouml_classifiers;
    }

    public void addRefontouml_classifier(Refontouml_classifier refontouml_classifier) {
        this.refontouml_classifiers.add(refontouml_classifier);
    }
    public List<RefOntoUML_Slot> getRefontouml_slots() {
        return refontouml_slots;
    }

    public void addRefontouml_slot(Refontouml_slot refontouml_slot) {
        this.refontouml_slots.add(refontouml_slot);
    }
    public RefOntoUML_Slot getRefontouml_slot() {
        return refontouml_slot;
    }

    public void setRefontouml_slot(RefOntoUML_Slot refontouml_slot) {
        this.refontouml_slot = refontouml_slot;
    }

}