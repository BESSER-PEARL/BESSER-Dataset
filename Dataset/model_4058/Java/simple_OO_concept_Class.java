





import java.util.List;
import java.util.ArrayList;

public class simple_OO_concept_Class extends NamedElement {

    private boolean isAbstract;





    private List<simple_OO_concept_Attribute> simple_oo_concept_attributes;




    private simple_OO_concept_Attribute simple_oo_concept_attribute;




    private List<simple_OO_concept_Operation> simple_oo_concept_operations;




    private List<simple_OO_concept_Class> simple_oo_concept_classs;




    private simple_OO_concept_Package simple_oo_concept_package;


    public simple_OO_concept_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.simple_oo_concept_attributes = new ArrayList<>();
        this.simple_oo_concept_operations = new ArrayList<>();
        this.simple_oo_concept_classs = new ArrayList<>();
    }

    public simple_OO_concept_Class(
        boolean isAbstract        ArrayList<simple_OO_concept_Attribute> simple_oo_concept_attributes,        ArrayList<simple_OO_concept_Operation> simple_oo_concept_operations,        ArrayList<simple_OO_concept_Class> simple_oo_concept_classs    ) {
        this.isAbstract = isAbstract;
        this.simple_oo_concept_attributes = simple_oo_concept_attributes;
        this.simple_oo_concept_operations = simple_oo_concept_operations;
        this.simple_oo_concept_classs = simple_oo_concept_classs;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<simple_OO_concept_Attribute> getSimple_oo_concept_attributes() {
        return simple_oo_concept_attributes;
    }

    public void addSimple_oo_concept_attribute(Simple_oo_concept_attribute simple_oo_concept_attribute) {
        this.simple_oo_concept_attributes.add(simple_oo_concept_attribute);
    }
    public simple_OO_concept_Attribute getSimple_oo_concept_attribute() {
        return simple_oo_concept_attribute;
    }

    public void setSimple_oo_concept_attribute(simple_OO_concept_Attribute simple_oo_concept_attribute) {
        this.simple_oo_concept_attribute = simple_oo_concept_attribute;
    }
    public List<simple_OO_concept_Operation> getSimple_oo_concept_operations() {
        return simple_oo_concept_operations;
    }

    public void addSimple_oo_concept_operation(Simple_oo_concept_operation simple_oo_concept_operation) {
        this.simple_oo_concept_operations.add(simple_oo_concept_operation);
    }
    public List<simple_OO_concept_Class> getSimple_oo_concept_classs() {
        return simple_oo_concept_classs;
    }

    public void addSimple_oo_concept_class(Simple_oo_concept_class simple_oo_concept_class) {
        this.simple_oo_concept_classs.add(simple_oo_concept_class);
    }
    public simple_OO_concept_Package getSimple_oo_concept_package() {
        return simple_oo_concept_package;
    }

    public void setSimple_oo_concept_package(simple_OO_concept_Package simple_oo_concept_package) {
        this.simple_oo_concept_package = simple_oo_concept_package;
    }

}