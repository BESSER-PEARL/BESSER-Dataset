





import java.util.List;
import java.util.ArrayList;

public class ClassMM_Class extends Classifier {

    private String is_persistent;





    private ClassMM_Association classmm_association;




    private ClassMM_Class classmm_class;




    private ClassMM_Association classmm_association;


    public ClassMM_Class(
        String is_persistent    ) {
        super(
        );
        this.is_persistent = is_persistent;
    }


    public String getIs_persistent() {
        return is_persistent;
    }

    public void setIs_persistent(String is_persistent) {
        this.is_persistent = is_persistent;
    }

    public ClassMM_Association getClassmm_association() {
        return classmm_association;
    }

    public void setClassmm_association(ClassMM_Association classmm_association) {
        this.classmm_association = classmm_association;
    }
    public ClassMM_Class getClassmm_class() {
        return classmm_class;
    }

    public void setClassmm_class(ClassMM_Class classmm_class) {
        this.classmm_class = classmm_class;
    }
    public ClassMM_Association getClassmm_association() {
        return classmm_association;
    }

    public void setClassmm_association(ClassMM_Association classmm_association) {
        this.classmm_association = classmm_association;
    }

}