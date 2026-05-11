





import java.util.List;
import java.util.ArrayList;

public class ClassMM_Attribute  {

    private String name;
    private String is_primary;





    private ClassMM_Classifier classmm_classifier;




    private ClassMM_Class classmm_class;


    public ClassMM_Attribute(
        String name,        String is_primary    ) {
        this.name = name;
        this.is_primary = is_primary;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIs_primary() {
        return is_primary;
    }

    public void setIs_primary(String is_primary) {
        this.is_primary = is_primary;
    }

    public ClassMM_Classifier getClassmm_classifier() {
        return classmm_classifier;
    }

    public void setClassmm_classifier(ClassMM_Classifier classmm_classifier) {
        this.classmm_classifier = classmm_classifier;
    }
    public ClassMM_Class getClassmm_class() {
        return classmm_class;
    }

    public void setClassmm_class(ClassMM_Class classmm_class) {
        this.classmm_class = classmm_class;
    }

}