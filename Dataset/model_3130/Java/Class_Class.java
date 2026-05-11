





import java.util.List;
import java.util.ArrayList;

public class Class_Class extends Classifier {

    private boolean isAbstract;





    private Class_Attribute class_attribute;




    private Class_Class class_class;




    private List<Class_Attribute> class_attributes;


    public Class_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.class_attributes = new ArrayList<>();
    }

    public Class_Class(
        boolean isAbstract        ArrayList<Class_Attribute> class_attributes    ) {
        this.isAbstract = isAbstract;
        this.class_attributes = class_attributes;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public Class_Attribute getClass_attribute() {
        return class_attribute;
    }

    public void setClass_attribute(Class_Attribute class_attribute) {
        this.class_attribute = class_attribute;
    }
    public Class_Class getClass_class() {
        return class_class;
    }

    public void setClass_class(Class_Class class_class) {
        this.class_class = class_class;
    }
    public List<Class_Attribute> getClass_attributes() {
        return class_attributes;
    }

    public void addClass_attribute(Class_attribute class_attribute) {
        this.class_attributes.add(class_attribute);
    }

}