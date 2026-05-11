





import java.util.List;
import java.util.ArrayList;

public class dbl_VariableAccess extends ElementAccess {






    private dbl_Assignment dbl_assignment;




    private dbl_SwitchStatement dbl_switchstatement;


    public dbl_VariableAccess(
    ) {
        super(
        );
    }



    public dbl_Assignment getDbl_assignment() {
        return dbl_assignment;
    }

    public void setDbl_assignment(dbl_Assignment dbl_assignment) {
        this.dbl_assignment = dbl_assignment;
    }
    public dbl_SwitchStatement getDbl_switchstatement() {
        return dbl_switchstatement;
    }

    public void setDbl_switchstatement(dbl_SwitchStatement dbl_switchstatement) {
        this.dbl_switchstatement = dbl_switchstatement;
    }

}