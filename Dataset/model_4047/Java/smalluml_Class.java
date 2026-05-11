





import java.util.List;
import java.util.ArrayList;

public class smalluml_Class extends SuperType {

    private boolean isAbstract;





    private List<smalluml_Attribute> smalluml_attributes;




    private smalluml_Role smalluml_role;




    private smalluml_Class smalluml_class;




    private List<smalluml_Operation> smalluml_operations;


    public smalluml_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.smalluml_attributes = new ArrayList<>();
        this.smalluml_operations = new ArrayList<>();
    }

    public smalluml_Class(
        boolean isAbstract        ArrayList<smalluml_Attribute> smalluml_attributes,        ArrayList<smalluml_Operation> smalluml_operations    ) {
        this.isAbstract = isAbstract;
        this.smalluml_attributes = smalluml_attributes;
        this.smalluml_operations = smalluml_operations;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<smalluml_Attribute> getSmalluml_attributes() {
        return smalluml_attributes;
    }

    public void addSmalluml_attribute(Smalluml_attribute smalluml_attribute) {
        this.smalluml_attributes.add(smalluml_attribute);
    }
    public smalluml_Role getSmalluml_role() {
        return smalluml_role;
    }

    public void setSmalluml_role(smalluml_Role smalluml_role) {
        this.smalluml_role = smalluml_role;
    }
    public smalluml_Class getSmalluml_class() {
        return smalluml_class;
    }

    public void setSmalluml_class(smalluml_Class smalluml_class) {
        this.smalluml_class = smalluml_class;
    }
    public List<smalluml_Operation> getSmalluml_operations() {
        return smalluml_operations;
    }

    public void addSmalluml_operation(Smalluml_operation smalluml_operation) {
        this.smalluml_operations.add(smalluml_operation);
    }

}