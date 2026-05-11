





import java.util.List;
import java.util.ArrayList;

public class classes_Slot extends Element {






    private classes_StructuralFeature classes_structuralfeature;




    private classes_InstanceSpecification classes_instancespecification;




    private List<classes_ValueSpecification> classes_valuespecifications;




    private classes_InstanceSpecification classes_instancespecification;


    public classes_Slot(
    ) {
        super(
        );
        this.classes_valuespecifications = new ArrayList<>();
    }

    public classes_Slot(
        ArrayList<classes_ValueSpecification> classes_valuespecifications    ) {
        this.classes_valuespecifications = classes_valuespecifications;
    }


    public classes_StructuralFeature getClasses_structuralfeature() {
        return classes_structuralfeature;
    }

    public void setClasses_structuralfeature(classes_StructuralFeature classes_structuralfeature) {
        this.classes_structuralfeature = classes_structuralfeature;
    }
    public classes_InstanceSpecification getClasses_instancespecification() {
        return classes_instancespecification;
    }

    public void setClasses_instancespecification(classes_InstanceSpecification classes_instancespecification) {
        this.classes_instancespecification = classes_instancespecification;
    }
    public List<classes_ValueSpecification> getClasses_valuespecifications() {
        return classes_valuespecifications;
    }

    public void addClasses_valuespecification(Classes_valuespecification classes_valuespecification) {
        this.classes_valuespecifications.add(classes_valuespecification);
    }
    public classes_InstanceSpecification getClasses_instancespecification() {
        return classes_instancespecification;
    }

    public void setClasses_instancespecification(classes_InstanceSpecification classes_instancespecification) {
        this.classes_instancespecification = classes_instancespecification;
    }

}