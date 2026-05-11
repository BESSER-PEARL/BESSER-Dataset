





import java.util.List;
import java.util.ArrayList;

public class SimpleClass_Attribute  {

    private String name;
    private boolean is_primary;





    private SimpleClass_Classifier simpleclass_classifier;




    private SimpleClass_Class simpleclass_class;


    public SimpleClass_Attribute(
        String name,        boolean is_primary    ) {
        this.name = name;
        this.is_primary = is_primary;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIs_primary() {
        return is_primary;
    }

    public void setIs_primary(boolean is_primary) {
        this.is_primary = is_primary;
    }

    public SimpleClass_Classifier getSimpleclass_classifier() {
        return simpleclass_classifier;
    }

    public void setSimpleclass_classifier(SimpleClass_Classifier simpleclass_classifier) {
        this.simpleclass_classifier = simpleclass_classifier;
    }
    public SimpleClass_Class getSimpleclass_class() {
        return simpleclass_class;
    }

    public void setSimpleclass_class(SimpleClass_Class simpleclass_class) {
        this.simpleclass_class = simpleclass_class;
    }

}