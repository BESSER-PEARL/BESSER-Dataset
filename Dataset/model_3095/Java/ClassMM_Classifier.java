





import java.util.List;
import java.util.ArrayList;

public class ClassMM_Classifier  {

    private String name;





    private ClassMM_Attribute classmm_attribute;


    public ClassMM_Classifier(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ClassMM_Attribute getClassmm_attribute() {
        return classmm_attribute;
    }

    public void setClassmm_attribute(ClassMM_Attribute classmm_attribute) {
        this.classmm_attribute = classmm_attribute;
    }

}