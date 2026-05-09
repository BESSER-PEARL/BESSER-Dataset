





import java.util.List;
import java.util.ArrayList;

public class UML2_ProtocolTransition extends Transition {






    private List<UML2_Operation> uml2_operations;




    private UML2_Constraint uml2_constraint;




    private UML2_Constraint uml2_constraint;


    public UML2_ProtocolTransition(
    ) {
        super(
        );
        this.uml2_operations = new ArrayList<>();
    }

    public UML2_ProtocolTransition(
        ArrayList<UML2_Operation> uml2_operations    ) {
        this.uml2_operations = uml2_operations;
    }


    public List<UML2_Operation> getUml2_operations() {
        return uml2_operations;
    }

    public void addUml2_operation(Uml2_operation uml2_operation) {
        this.uml2_operations.add(uml2_operation);
    }
    public UML2_Constraint getUml2_constraint() {
        return uml2_constraint;
    }

    public void setUml2_constraint(UML2_Constraint uml2_constraint) {
        this.uml2_constraint = uml2_constraint;
    }
    public UML2_Constraint getUml2_constraint() {
        return uml2_constraint;
    }

    public void setUml2_constraint(UML2_Constraint uml2_constraint) {
        this.uml2_constraint = uml2_constraint;
    }

}