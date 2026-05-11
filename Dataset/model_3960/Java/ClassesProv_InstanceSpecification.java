





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_InstanceSpecification extends PackageableElement {






    private List<ClassesProv_Classifier> classesprov_classifiers;




    private ClassesProv_Slot classesprov_slot;




    private List<ClassesProv_Slot> classesprov_slots;


    public ClassesProv_InstanceSpecification(
    ) {
        super(
        );
        this.classesprov_classifiers = new ArrayList<>();
        this.classesprov_slots = new ArrayList<>();
    }

    public ClassesProv_InstanceSpecification(
        ArrayList<ClassesProv_Classifier> classesprov_classifiers,        ArrayList<ClassesProv_Slot> classesprov_slots    ) {
        this.classesprov_classifiers = classesprov_classifiers;
        this.classesprov_slots = classesprov_slots;
    }


    public List<ClassesProv_Classifier> getClassesprov_classifiers() {
        return classesprov_classifiers;
    }

    public void addClassesprov_classifier(Classesprov_classifier classesprov_classifier) {
        this.classesprov_classifiers.add(classesprov_classifier);
    }
    public ClassesProv_Slot getClassesprov_slot() {
        return classesprov_slot;
    }

    public void setClassesprov_slot(ClassesProv_Slot classesprov_slot) {
        this.classesprov_slot = classesprov_slot;
    }
    public List<ClassesProv_Slot> getClassesprov_slots() {
        return classesprov_slots;
    }

    public void addClassesprov_slot(Classesprov_slot classesprov_slot) {
        this.classesprov_slots.add(classesprov_slot);
    }

}