





import java.util.List;
import java.util.ArrayList;

public class classes_Association extends Classifier {

    private boolean derived;





    private classes_Property classes_property;




    private List<classes_Type> classes_types;




    private classes_Property classes_property;




    private List<classes_Property> classes_propertys;




    private List<classes_Property> classes_propertys;




    private List<classes_Property> classes_propertys;


    public classes_Association(
        boolean derived    ) {
        super(
        );
        this.derived = derived;
        this.classes_types = new ArrayList<>();
        this.classes_propertys = new ArrayList<>();
        this.classes_propertys = new ArrayList<>();
        this.classes_propertys = new ArrayList<>();
    }

    public classes_Association(
        boolean derived        ArrayList<classes_Type> classes_types,        ArrayList<classes_Property> classes_propertys,        ArrayList<classes_Property> classes_propertys,        ArrayList<classes_Property> classes_propertys    ) {
        this.derived = derived;
        this.classes_types = classes_types;
        this.classes_propertys = classes_propertys;
        this.classes_propertys = classes_propertys;
        this.classes_propertys = classes_propertys;
    }

    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }

    public classes_Property getClasses_property() {
        return classes_property;
    }

    public void setClasses_property(classes_Property classes_property) {
        this.classes_property = classes_property;
    }
    public List<classes_Type> getClasses_types() {
        return classes_types;
    }

    public void addClasses_type(Classes_type classes_type) {
        this.classes_types.add(classes_type);
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
    public List<classes_Property> getClasses_propertys() {
        return classes_propertys;
    }

    public void addClasses_property(Classes_property classes_property) {
        this.classes_propertys.add(classes_property);
    }
    public List<classes_Property> getClasses_propertys() {
        return classes_propertys;
    }

    public void addClasses_property(Classes_property classes_property) {
        this.classes_propertys.add(classes_property);
    }

}