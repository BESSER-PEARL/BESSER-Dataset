





import java.util.List;
import java.util.ArrayList;

public class ClassMM_Class extends Classifier {

    private String is_persistent;





    private ClassMM_Class classmm_class;




    private List<ClassMM_Attribute> classmm_attributes;


    public ClassMM_Class(
        String is_persistent    ) {
        super(
        );
        this.is_persistent = is_persistent;
        this.classmm_attributes = new ArrayList<>();
    }

    public ClassMM_Class(
        String is_persistent        ArrayList<ClassMM_Attribute> classmm_attributes    ) {
        this.is_persistent = is_persistent;
        this.classmm_attributes = classmm_attributes;
    }

    public String getIs_persistent() {
        return is_persistent;
    }

    public void setIs_persistent(String is_persistent) {
        this.is_persistent = is_persistent;
    }

    public ClassMM_Class getClassmm_class() {
        return classmm_class;
    }

    public void setClassmm_class(ClassMM_Class classmm_class) {
        this.classmm_class = classmm_class;
    }
    public List<ClassMM_Attribute> getClassmm_attributes() {
        return classmm_attributes;
    }

    public void addClassmm_attribute(Classmm_attribute classmm_attribute) {
        this.classmm_attributes.add(classmm_attribute);
    }

}