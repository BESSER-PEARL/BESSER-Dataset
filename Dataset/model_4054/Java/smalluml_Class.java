





import java.util.List;
import java.util.ArrayList;

public class smalluml_Class extends Entity {

    private boolean abstract;





    private smalluml_Class smalluml_class;




    private List<smalluml_Operation> smalluml_operations;




    private smalluml_Association smalluml_association;




    private smalluml_Association smalluml_association;


    public smalluml_Class(
        boolean abstract    ) {
        super(
        );
        this.abstract = abstract;
        this.smalluml_operations = new ArrayList<>();
    }

    public smalluml_Class(
        boolean abstract        ArrayList<smalluml_Operation> smalluml_operations    ) {
        this.abstract = abstract;
        this.smalluml_operations = smalluml_operations;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public smalluml_Class getSmalluml_class() {
        return smalluml_class;
    }

    public void setSmalluml_class(smalluml_Class smalluml_class) {
        this.smalluml_class = smalluml_class;
    }
    public List<smalluml_Operation> getSmalluml_operations() {
        return smalluml_operations;
    }

    public void addSmalluml_operation(Smalluml_operation smalluml_operation) {
        this.smalluml_operations.add(smalluml_operation);
    }
    public smalluml_Association getSmalluml_association() {
        return smalluml_association;
    }

    public void setSmalluml_association(smalluml_Association smalluml_association) {
        this.smalluml_association = smalluml_association;
    }
    public smalluml_Association getSmalluml_association() {
        return smalluml_association;
    }

    public void setSmalluml_association(smalluml_Association smalluml_association) {
        this.smalluml_association = smalluml_association;
    }

}