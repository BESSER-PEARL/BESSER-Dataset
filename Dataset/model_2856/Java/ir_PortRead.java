





import java.util.List;
import java.util.ArrayList;

public class ir_PortRead extends PortAccess {






    private List<ir_VariableReference> ir_variablereferences;




    private ir_Action ir_action;


    public ir_PortRead(
    ) {
        super(
        );
        this.ir_variablereferences = new ArrayList<>();
    }

    public ir_PortRead(
        ArrayList<ir_VariableReference> ir_variablereferences    ) {
        this.ir_variablereferences = ir_variablereferences;
    }


    public List<ir_VariableReference> getIr_variablereferences() {
        return ir_variablereferences;
    }

    public void addIr_variablereference(Ir_variablereference ir_variablereference) {
        this.ir_variablereferences.add(ir_variablereference);
    }
    public ir_Action getIr_action() {
        return ir_action;
    }

    public void setIr_action(ir_Action ir_action) {
        this.ir_action = ir_action;
    }

}