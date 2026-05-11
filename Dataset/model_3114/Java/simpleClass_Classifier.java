





import java.util.List;
import java.util.ArrayList;

public class simpleClass_Classifier  {

    private String name;





    private simpleClass_ClassModel simpleclass_classmodel;


    public simpleClass_Classifier(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simpleClass_ClassModel getSimpleclass_classmodel() {
        return simpleclass_classmodel;
    }

    public void setSimpleclass_classmodel(simpleClass_ClassModel simpleclass_classmodel) {
        this.simpleclass_classmodel = simpleclass_classmodel;
    }

}