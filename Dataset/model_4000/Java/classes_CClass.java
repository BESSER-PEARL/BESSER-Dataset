





import java.util.List;
import java.util.ArrayList;

public class classes_CClass extends Classifier {

    private boolean abstract;





    private classes_CClass classes_cclass;




    private classes_CClass classes_cclass;




    private List<classes_Attribute> classes_attributes;


    public classes_CClass(
        boolean abstract    ) {
        super(
        );
        this.abstract = abstract;
        this.classes_attributes = new ArrayList<>();
    }

    public classes_CClass(
        boolean abstract        ArrayList<classes_Attribute> classes_attributes    ) {
        this.abstract = abstract;
        this.classes_attributes = classes_attributes;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public classes_CClass getClasses_cclass() {
        return classes_cclass;
    }

    public void setClasses_cclass(classes_CClass classes_cclass) {
        this.classes_cclass = classes_cclass;
    }
    public classes_CClass getClasses_cclass() {
        return classes_cclass;
    }

    public void setClasses_cclass(classes_CClass classes_cclass) {
        this.classes_cclass = classes_cclass;
    }
    public List<classes_Attribute> getClasses_attributes() {
        return classes_attributes;
    }

    public void addClasses_attribute(Classes_attribute classes_attribute) {
        this.classes_attributes.add(classes_attribute);
    }

}