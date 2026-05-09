





import java.util.List;
import java.util.ArrayList;

public class classes_Class extends NamedElement {






    private classes_Package classes_package;




    private List<classes_Operation> classes_operations;




    private List<classes_Property> classes_propertys;




    private classes_Class classes_class;


    public classes_Class(
    ) {
        super(
        );
        this.classes_operations = new ArrayList<>();
        this.classes_propertys = new ArrayList<>();
    }

    public classes_Class(
        ArrayList<classes_Operation> classes_operations,        ArrayList<classes_Property> classes_propertys    ) {
        this.classes_operations = classes_operations;
        this.classes_propertys = classes_propertys;
    }


    public classes_Package getClasses_package() {
        return classes_package;
    }

    public void setClasses_package(classes_Package classes_package) {
        this.classes_package = classes_package;
    }
    public List<classes_Operation> getClasses_operations() {
        return classes_operations;
    }

    public void addClasses_operation(Classes_operation classes_operation) {
        this.classes_operations.add(classes_operation);
    }
    public List<classes_Property> getClasses_propertys() {
        return classes_propertys;
    }

    public void addClasses_property(Classes_property classes_property) {
        this.classes_propertys.add(classes_property);
    }
    public classes_Class getClasses_class() {
        return classes_class;
    }

    public void setClasses_class(classes_Class classes_class) {
        this.classes_class = classes_class;
    }

}