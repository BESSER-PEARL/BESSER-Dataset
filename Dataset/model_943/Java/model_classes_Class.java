





import java.util.List;
import java.util.ArrayList;

public class model_classes_Class extends PackageElement {






    private List<classes_Association> classes_associations;




    private List<classes_Attribute> classes_attributes;




    private List<classes_Association> classes_associations;


    public model_classes_Class(
    ) {
        super(
        );
        this.classes_associations = new ArrayList<>();
        this.classes_attributes = new ArrayList<>();
        this.classes_associations = new ArrayList<>();
    }

    public model_classes_Class(
        ArrayList<classes_Association> classes_associations,        ArrayList<classes_Attribute> classes_attributes,        ArrayList<classes_Association> classes_associations    ) {
        this.classes_associations = classes_associations;
        this.classes_attributes = classes_attributes;
        this.classes_associations = classes_associations;
    }


    public List<classes_Association> getClasses_associations() {
        return classes_associations;
    }

    public void addClasses_association(Classes_association classes_association) {
        this.classes_associations.add(classes_association);
    }
    public List<classes_Attribute> getClasses_attributes() {
        return classes_attributes;
    }

    public void addClasses_attribute(Classes_attribute classes_attribute) {
        this.classes_attributes.add(classes_attribute);
    }
    public List<classes_Association> getClasses_associations() {
        return classes_associations;
    }

    public void addClasses_association(Classes_association classes_association) {
        this.classes_associations.add(classes_association);
    }

}