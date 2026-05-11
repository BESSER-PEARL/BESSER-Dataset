





import java.util.List;
import java.util.ArrayList;

public class ClassM_Classifier  {

    private String name;





    private ClassM_Attribute classm_attribute;




    private ClassM_Model classm_model;


    public ClassM_Classifier(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ClassM_Attribute getClassm_attribute() {
        return classm_attribute;
    }

    public void setClassm_attribute(ClassM_Attribute classm_attribute) {
        this.classm_attribute = classm_attribute;
    }
    public ClassM_Model getClassm_model() {
        return classm_model;
    }

    public void setClassm_model(ClassM_Model classm_model) {
        this.classm_model = classm_model;
    }

}