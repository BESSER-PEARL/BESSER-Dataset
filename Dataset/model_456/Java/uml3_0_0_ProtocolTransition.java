





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ProtocolTransition extends Transition {






    private uml3_0_0_Constraint uml3_0_0_constraint;




    private List<uml3_0_0_Operation> uml3_0_0_operations;




    private uml3_0_0_Constraint uml3_0_0_constraint;


    public uml3_0_0_ProtocolTransition(
    ) {
        super(
        );
        this.uml3_0_0_operations = new ArrayList<>();
    }

    public uml3_0_0_ProtocolTransition(
        ArrayList<uml3_0_0_Operation> uml3_0_0_operations    ) {
        this.uml3_0_0_operations = uml3_0_0_operations;
    }


    public uml3_0_0_Constraint getUml3_0_0_constraint() {
        return uml3_0_0_constraint;
    }

    public void setUml3_0_0_constraint(uml3_0_0_Constraint uml3_0_0_constraint) {
        this.uml3_0_0_constraint = uml3_0_0_constraint;
    }
    public List<uml3_0_0_Operation> getUml3_0_0_operations() {
        return uml3_0_0_operations;
    }

    public void addUml3_0_0_operation(Uml3_0_0_operation uml3_0_0_operation) {
        this.uml3_0_0_operations.add(uml3_0_0_operation);
    }
    public uml3_0_0_Constraint getUml3_0_0_constraint() {
        return uml3_0_0_constraint;
    }

    public void setUml3_0_0_constraint(uml3_0_0_Constraint uml3_0_0_constraint) {
        this.uml3_0_0_constraint = uml3_0_0_constraint;
    }

}