





import java.util.List;
import java.util.ArrayList;

public class class_Class extends Classifier {

    private boolean isAbstract;





    private List<class_Attribute> class_attributes;




    private class_Class class_class;




    private class_Package class_package;




    private class_Attribute class_attribute;


    public class_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.class_attributes = new ArrayList<>();
    }

    public class_Class(
        boolean isAbstract        ArrayList<class_Attribute> class_attributes    ) {
        this.isAbstract = isAbstract;
        this.class_attributes = class_attributes;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<class_Attribute> getClass_attributes() {
        return class_attributes;
    }

    public void addClass_attribute(Class_attribute class_attribute) {
        this.class_attributes.add(class_attribute);
    }
    public class_Class getClass_class() {
        return class_class;
    }

    public void setClass_class(class_Class class_class) {
        this.class_class = class_class;
    }
    public class_Package getClass_package() {
        return class_package;
    }

    public void setClass_package(class_Package class_package) {
        this.class_package = class_package;
    }
    public class_Attribute getClass_attribute() {
        return class_attribute;
    }

    public void setClass_attribute(class_Attribute class_attribute) {
        this.class_attribute = class_attribute;
    }

}