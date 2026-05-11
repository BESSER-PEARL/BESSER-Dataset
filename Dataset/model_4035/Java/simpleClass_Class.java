





import java.util.List;
import java.util.ArrayList;

public class simpleClass_Class extends NamedElement {

    private boolean persistent;





    private simpleClass_Package simpleclass_package;




    private simpleClass_Association simpleclass_association;




    private List<simpleClass_Attribute> simpleclass_attributes;




    private simpleClass_Association simpleclass_association;




    private List<simpleClass_Class> simpleclass_classs;


    public simpleClass_Class(
        boolean persistent    ) {
        super(
        );
        this.persistent = persistent;
        this.simpleclass_attributes = new ArrayList<>();
        this.simpleclass_classs = new ArrayList<>();
    }

    public simpleClass_Class(
        boolean persistent        ArrayList<simpleClass_Attribute> simpleclass_attributes,        ArrayList<simpleClass_Class> simpleclass_classs    ) {
        this.persistent = persistent;
        this.simpleclass_attributes = simpleclass_attributes;
        this.simpleclass_classs = simpleclass_classs;
    }

    public boolean getPersistent() {
        return persistent;
    }

    public void setPersistent(boolean persistent) {
        this.persistent = persistent;
    }

    public simpleClass_Package getSimpleclass_package() {
        return simpleclass_package;
    }

    public void setSimpleclass_package(simpleClass_Package simpleclass_package) {
        this.simpleclass_package = simpleclass_package;
    }
    public simpleClass_Association getSimpleclass_association() {
        return simpleclass_association;
    }

    public void setSimpleclass_association(simpleClass_Association simpleclass_association) {
        this.simpleclass_association = simpleclass_association;
    }
    public List<simpleClass_Attribute> getSimpleclass_attributes() {
        return simpleclass_attributes;
    }

    public void addSimpleclass_attribute(Simpleclass_attribute simpleclass_attribute) {
        this.simpleclass_attributes.add(simpleclass_attribute);
    }
    public simpleClass_Association getSimpleclass_association() {
        return simpleclass_association;
    }

    public void setSimpleclass_association(simpleClass_Association simpleclass_association) {
        this.simpleclass_association = simpleclass_association;
    }
    public List<simpleClass_Class> getSimpleclass_classs() {
        return simpleclass_classs;
    }

    public void addSimpleclass_class(Simpleclass_class simpleclass_class) {
        this.simpleclass_classs.add(simpleclass_class);
    }

}