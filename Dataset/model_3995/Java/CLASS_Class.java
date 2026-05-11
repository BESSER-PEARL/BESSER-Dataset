





import java.util.List;
import java.util.ArrayList;

public class CLASS_Class extends Classifier {

    private boolean isAbstract;





    private CLASS_Attribute class_attribute;




    private List<CLASS_Attribute> class_attributes;




    private CLASS_Class class_class;


    public CLASS_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.class_attributes = new ArrayList<>();
    }

    public CLASS_Class(
        boolean isAbstract        ArrayList<CLASS_Attribute> class_attributes    ) {
        this.isAbstract = isAbstract;
        this.class_attributes = class_attributes;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public CLASS_Attribute getClass_attribute() {
        return class_attribute;
    }

    public void setClass_attribute(CLASS_Attribute class_attribute) {
        this.class_attribute = class_attribute;
    }
    public List<CLASS_Attribute> getClass_attributes() {
        return class_attributes;
    }

    public void addClass_attribute(Class_attribute class_attribute) {
        this.class_attributes.add(class_attribute);
    }
    public CLASS_Class getClass_class() {
        return class_class;
    }

    public void setClass_class(CLASS_Class class_class) {
        this.class_class = class_class;
    }

}