





import java.util.List;
import java.util.ArrayList;

public class classdiagram_Class extends Classifier {

    private boolean is_persistent;





    private classdiagram_Class classdiagram_class;




    private classdiagram_Association classdiagram_association;




    private classdiagram_Association classdiagram_association;


    public classdiagram_Class(
        boolean is_persistent    ) {
        super(
        );
        this.is_persistent = is_persistent;
    }


    public boolean getIs_persistent() {
        return is_persistent;
    }

    public void setIs_persistent(boolean is_persistent) {
        this.is_persistent = is_persistent;
    }

    public classdiagram_Class getClassdiagram_class() {
        return classdiagram_class;
    }

    public void setClassdiagram_class(classdiagram_Class classdiagram_class) {
        this.classdiagram_class = classdiagram_class;
    }
    public classdiagram_Association getClassdiagram_association() {
        return classdiagram_association;
    }

    public void setClassdiagram_association(classdiagram_Association classdiagram_association) {
        this.classdiagram_association = classdiagram_association;
    }
    public classdiagram_Association getClassdiagram_association() {
        return classdiagram_association;
    }

    public void setClassdiagram_association(classdiagram_Association classdiagram_association) {
        this.classdiagram_association = classdiagram_association;
    }

}