





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ProtocolTransition extends Transition {






    private List<UML2WithID_Operation> uml2withid_operations;




    private UML2WithID_Constraint uml2withid_constraint;




    private UML2WithID_Constraint uml2withid_constraint;


    public UML2WithID_ProtocolTransition(
    ) {
        super(
        );
        this.uml2withid_operations = new ArrayList<>();
    }

    public UML2WithID_ProtocolTransition(
        ArrayList<UML2WithID_Operation> uml2withid_operations    ) {
        this.uml2withid_operations = uml2withid_operations;
    }


    public List<UML2WithID_Operation> getUml2withid_operations() {
        return uml2withid_operations;
    }

    public void addUml2withid_operation(Uml2withid_operation uml2withid_operation) {
        this.uml2withid_operations.add(uml2withid_operation);
    }
    public UML2WithID_Constraint getUml2withid_constraint() {
        return uml2withid_constraint;
    }

    public void setUml2withid_constraint(UML2WithID_Constraint uml2withid_constraint) {
        this.uml2withid_constraint = uml2withid_constraint;
    }
    public UML2WithID_Constraint getUml2withid_constraint() {
        return uml2withid_constraint;
    }

    public void setUml2withid_constraint(UML2WithID_Constraint uml2withid_constraint) {
        this.uml2withid_constraint = uml2withid_constraint;
    }

}