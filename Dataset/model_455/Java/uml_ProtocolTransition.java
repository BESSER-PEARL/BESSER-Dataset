





import java.util.List;
import java.util.ArrayList;

public class uml_ProtocolTransition extends Transition {






    private uml_Constraint uml_constraint;




    private uml_Constraint uml_constraint;




    private List<uml_Operation> uml_operations;


    public uml_ProtocolTransition(
    ) {
        super(
        );
        this.uml_operations = new ArrayList<>();
    }

    public uml_ProtocolTransition(
        ArrayList<uml_Operation> uml_operations    ) {
        this.uml_operations = uml_operations;
    }


    public uml_Constraint getUml_constraint() {
        return uml_constraint;
    }

    public void setUml_constraint(uml_Constraint uml_constraint) {
        this.uml_constraint = uml_constraint;
    }
    public uml_Constraint getUml_constraint() {
        return uml_constraint;
    }

    public void setUml_constraint(uml_Constraint uml_constraint) {
        this.uml_constraint = uml_constraint;
    }
    public List<uml_Operation> getUml_operations() {
        return uml_operations;
    }

    public void addUml_operation(Uml_operation uml_operation) {
        this.uml_operations.add(uml_operation);
    }

}