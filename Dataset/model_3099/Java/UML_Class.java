





import java.util.List;
import java.util.ArrayList;

public class UML_Class extends Classifier {

    private boolean is_persistent;





    private UML_Association uml_association;




    private UML_Association uml_association;




    private UML_Class uml_class;


    public UML_Class(
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

    public UML_Association getUml_association() {
        return uml_association;
    }

    public void setUml_association(UML_Association uml_association) {
        this.uml_association = uml_association;
    }
    public UML_Association getUml_association() {
        return uml_association;
    }

    public void setUml_association(UML_Association uml_association) {
        this.uml_association = uml_association;
    }
    public UML_Class getUml_class() {
        return uml_class;
    }

    public void setUml_class(UML_Class uml_class) {
        this.uml_class = uml_class;
    }

}