





import java.util.List;
import java.util.ArrayList;

public class cmof_InstanceSpecification extends PackageableElement {






    private List<cmof_Slot> cmof_slots;




    private List<cmof_Classifier> cmof_classifiers;




    private cmof_Slot cmof_slot;




    private cmof_ValueSpecification cmof_valuespecification;


    public cmof_InstanceSpecification(
    ) {
        super(
        );
        this.cmof_slots = new ArrayList<>();
        this.cmof_classifiers = new ArrayList<>();
    }

    public cmof_InstanceSpecification(
        ArrayList<cmof_Slot> cmof_slots,        ArrayList<cmof_Classifier> cmof_classifiers    ) {
        this.cmof_slots = cmof_slots;
        this.cmof_classifiers = cmof_classifiers;
    }


    public List<cmof_Slot> getCmof_slots() {
        return cmof_slots;
    }

    public void addCmof_slot(Cmof_slot cmof_slot) {
        this.cmof_slots.add(cmof_slot);
    }
    public List<cmof_Classifier> getCmof_classifiers() {
        return cmof_classifiers;
    }

    public void addCmof_classifier(Cmof_classifier cmof_classifier) {
        this.cmof_classifiers.add(cmof_classifier);
    }
    public cmof_Slot getCmof_slot() {
        return cmof_slot;
    }

    public void setCmof_slot(cmof_Slot cmof_slot) {
        this.cmof_slot = cmof_slot;
    }
    public cmof_ValueSpecification getCmof_valuespecification() {
        return cmof_valuespecification;
    }

    public void setCmof_valuespecification(cmof_ValueSpecification cmof_valuespecification) {
        this.cmof_valuespecification = cmof_valuespecification;
    }

}