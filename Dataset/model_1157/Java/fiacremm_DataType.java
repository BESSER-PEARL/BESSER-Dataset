





import java.util.List;
import java.util.ArrayList;

public class fiacremm_DataType extends EModelElement {

    private String Name;





    private fiacremm_Variable fiacremm_variable;


    public fiacremm_DataType(
        String Name    ) {
        super(
        );
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public fiacremm_Variable getFiacremm_variable() {
        return fiacremm_variable;
    }

    public void setFiacremm_variable(fiacremm_Variable fiacremm_variable) {
        this.fiacremm_variable = fiacremm_variable;
    }

}