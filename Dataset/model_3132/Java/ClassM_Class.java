





import java.util.List;
import java.util.ArrayList;

public class ClassM_Class extends Classifier {






    private ClassM_Class classm_class;




    private List<ClassM_Class> classm_classs;


    public ClassM_Class(
    ) {
        super(
        );
        this.classm_classs = new ArrayList<>();
    }

    public ClassM_Class(
        ArrayList<ClassM_Class> classm_classs    ) {
        this.classm_classs = classm_classs;
    }


    public ClassM_Class getClassm_class() {
        return classm_class;
    }

    public void setClassm_class(ClassM_Class classm_class) {
        this.classm_class = classm_class;
    }
    public List<ClassM_Class> getClassm_classs() {
        return classm_classs;
    }

    public void addClassm_class(Classm_class classm_class) {
        this.classm_classs.add(classm_class);
    }

}