





import java.util.List;
import java.util.ArrayList;

public class class_Class extends Classifier {

    private boolean isAbstract;





    private class_Attribute class_attribute;




    private List<class_Attribute> class_attributes;




    private List<class_Class> class_classs;


    public class_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.class_attributes = new ArrayList<>();
        this.class_classs = new ArrayList<>();
    }

    public class_Class(
        boolean isAbstract        ArrayList<class_Attribute> class_attributes,        ArrayList<class_Class> class_classs    ) {
        this.isAbstract = isAbstract;
        this.class_attributes = class_attributes;
        this.class_classs = class_classs;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public class_Attribute getClass_attribute() {
        return class_attribute;
    }

    public void setClass_attribute(class_Attribute class_attribute) {
        this.class_attribute = class_attribute;
    }
    public List<class_Attribute> getClass_attributes() {
        return class_attributes;
    }

    public void addClass_attribute(Class_attribute class_attribute) {
        this.class_attributes.add(class_attribute);
    }
    public List<class_Class> getClass_classs() {
        return class_classs;
    }

    public void addClass_class(Class_class class_class) {
        this.class_classs.add(class_class);
    }

}