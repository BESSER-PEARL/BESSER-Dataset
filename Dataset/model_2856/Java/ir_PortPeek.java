





import java.util.List;
import java.util.ArrayList;

public class ir_PortPeek extends PortAccess {

    private int position;





    private ir_Guard ir_guard;




    private ir_VariableReference ir_variablereference;


    public ir_PortPeek(
        int position    ) {
        super(
        );
        this.position = position;
    }


    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public ir_Guard getIr_guard() {
        return ir_guard;
    }

    public void setIr_guard(ir_Guard ir_guard) {
        this.ir_guard = ir_guard;
    }
    public ir_VariableReference getIr_variablereference() {
        return ir_variablereference;
    }

    public void setIr_variablereference(ir_VariableReference ir_variablereference) {
        this.ir_variablereference = ir_variablereference;
    }

}