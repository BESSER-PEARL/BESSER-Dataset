





import java.util.List;
import java.util.ArrayList;

public class model_classes_Class extends PackageElement {






    private List<classes_Attribute> classes_attributes;


    public model_classes_Class(
    ) {
        super(
        );
        this.classes_attributes = new ArrayList<>();
    }

    public model_classes_Class(
        ArrayList<classes_Attribute> classes_attributes    ) {
        this.classes_attributes = classes_attributes;
    }


    public List<classes_Attribute> getClasses_attributes() {
        return classes_attributes;
    }

    public void addClasses_attribute(Classes_attribute classes_attribute) {
        this.classes_attributes.add(classes_attribute);
    }

}