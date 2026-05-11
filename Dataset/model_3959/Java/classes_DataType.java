





import java.util.List;
import java.util.ArrayList;

public class classes_DataType extends Classifier {






    private classes_Property classes_property;




    private List<classes_Property> classes_propertys;


    public classes_DataType(
    ) {
        super(
        );
        this.classes_propertys = new ArrayList<>();
    }

    public classes_DataType(
        ArrayList<classes_Property> classes_propertys    ) {
        this.classes_propertys = classes_propertys;
    }


    public classes_Property getClasses_property() {
        return classes_property;
    }

    public void setClasses_property(classes_Property classes_property) {
        this.classes_property = classes_property;
    }
    public List<classes_Property> getClasses_propertys() {
        return classes_propertys;
    }

    public void addClasses_property(Classes_property classes_property) {
        this.classes_propertys.add(classes_property);
    }

}