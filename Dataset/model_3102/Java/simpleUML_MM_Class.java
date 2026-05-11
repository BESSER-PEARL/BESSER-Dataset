





import java.util.List;
import java.util.ArrayList;

public class simpleUML_MM_Class extends Classifier {

    private boolean is_persistent;





    private simpleUML_MM_Association simpleuml_mm_association;




    private simpleUML_MM_Class simpleuml_mm_class;




    private simpleUML_MM_Association simpleuml_mm_association;


    public simpleUML_MM_Class(
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

    public simpleUML_MM_Association getSimpleuml_mm_association() {
        return simpleuml_mm_association;
    }

    public void setSimpleuml_mm_association(simpleUML_MM_Association simpleuml_mm_association) {
        this.simpleuml_mm_association = simpleuml_mm_association;
    }
    public simpleUML_MM_Class getSimpleuml_mm_class() {
        return simpleuml_mm_class;
    }

    public void setSimpleuml_mm_class(simpleUML_MM_Class simpleuml_mm_class) {
        this.simpleuml_mm_class = simpleuml_mm_class;
    }
    public simpleUML_MM_Association getSimpleuml_mm_association() {
        return simpleuml_mm_association;
    }

    public void setSimpleuml_mm_association(simpleUML_MM_Association simpleuml_mm_association) {
        this.simpleuml_mm_association = simpleuml_mm_association;
    }

}