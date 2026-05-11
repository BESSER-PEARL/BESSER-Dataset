





import java.util.List;
import java.util.ArrayList;

public class ClassMM_Association  {

    private String name;





    private ClassMM_Class classmm_class;




    private ClassMM_ClassModel classmm_classmodel;




    private ClassMM_Class classmm_class;


    public ClassMM_Association(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ClassMM_Class getClassmm_class() {
        return classmm_class;
    }

    public void setClassmm_class(ClassMM_Class classmm_class) {
        this.classmm_class = classmm_class;
    }
    public ClassMM_ClassModel getClassmm_classmodel() {
        return classmm_classmodel;
    }

    public void setClassmm_classmodel(ClassMM_ClassModel classmm_classmodel) {
        this.classmm_classmodel = classmm_classmodel;
    }
    public ClassMM_Class getClassmm_class() {
        return classmm_class;
    }

    public void setClassmm_class(ClassMM_Class classmm_class) {
        this.classmm_class = classmm_class;
    }

}