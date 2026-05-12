





import java.util.List;
import java.util.ArrayList;

public class sml_Message  {






    private sml_ConstraintBlock sml_constraintblock;




    private sml_ConstraintBlock sml_constraintblock;




    private sml_ConstraintBlock sml_constraintblock;




    private sml_SmlETypedElement sml_smletypedelement;




    private sml_Role sml_role;




    private List<sml_ParameterBinding> sml_parameterbindings;




    private sml_ConstraintBlock sml_constraintblock;




    private sml_Role sml_role;


    public sml_Message(
    ) {
        this.sml_parameterbindings = new ArrayList<>();
    }

    public sml_Message(
        ArrayList<sml_ParameterBinding> sml_parameterbindings    ) {
        this.sml_parameterbindings = sml_parameterbindings;
    }


    public sml_ConstraintBlock getSml_constraintblock() {
        return sml_constraintblock;
    }

    public void setSml_constraintblock(sml_ConstraintBlock sml_constraintblock) {
        this.sml_constraintblock = sml_constraintblock;
    }
    public sml_ConstraintBlock getSml_constraintblock() {
        return sml_constraintblock;
    }

    public void setSml_constraintblock(sml_ConstraintBlock sml_constraintblock) {
        this.sml_constraintblock = sml_constraintblock;
    }
    public sml_ConstraintBlock getSml_constraintblock() {
        return sml_constraintblock;
    }

    public void setSml_constraintblock(sml_ConstraintBlock sml_constraintblock) {
        this.sml_constraintblock = sml_constraintblock;
    }
    public sml_SmlETypedElement getSml_smletypedelement() {
        return sml_smletypedelement;
    }

    public void setSml_smletypedelement(sml_SmlETypedElement sml_smletypedelement) {
        this.sml_smletypedelement = sml_smletypedelement;
    }
    public sml_Role getSml_role() {
        return sml_role;
    }

    public void setSml_role(sml_Role sml_role) {
        this.sml_role = sml_role;
    }
    public List<sml_ParameterBinding> getSml_parameterbindings() {
        return sml_parameterbindings;
    }

    public void addSml_parameterbinding(Sml_parameterbinding sml_parameterbinding) {
        this.sml_parameterbindings.add(sml_parameterbinding);
    }
    public sml_ConstraintBlock getSml_constraintblock() {
        return sml_constraintblock;
    }

    public void setSml_constraintblock(sml_ConstraintBlock sml_constraintblock) {
        this.sml_constraintblock = sml_constraintblock;
    }
    public sml_Role getSml_role() {
        return sml_role;
    }

    public void setSml_role(sml_Role sml_role) {
        this.sml_role = sml_role;
    }

}