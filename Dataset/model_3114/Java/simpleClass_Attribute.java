





import java.util.List;
import java.util.ArrayList;

public class simpleClass_Attribute  {

    private boolean id;
    private String name;





    private simpleClass_Class simpleclass_class;




    private simpleClass_Classifier simpleclass_classifier;


    public simpleClass_Attribute(
        boolean id,        String name    ) {
        this.id = id;
        this.name = name;
    }


    public boolean getId() {
        return id;
    }

    public void setId(boolean id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simpleClass_Class getSimpleclass_class() {
        return simpleclass_class;
    }

    public void setSimpleclass_class(simpleClass_Class simpleclass_class) {
        this.simpleclass_class = simpleclass_class;
    }
    public simpleClass_Classifier getSimpleclass_classifier() {
        return simpleclass_classifier;
    }

    public void setSimpleclass_classifier(simpleClass_Classifier simpleclass_classifier) {
        this.simpleclass_classifier = simpleclass_classifier;
    }

}