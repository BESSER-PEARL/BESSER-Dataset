





import java.util.List;
import java.util.ArrayList;

public class ir_PortWrite extends Block, PortAccess {






    private List<ir_Expression> ir_expressions;




    private ir_Action ir_action;


    public ir_PortWrite(
    ) {
        super(
        );
        this.ir_expressions = new ArrayList<>();
    }

    public ir_PortWrite(
        ArrayList<ir_Expression> ir_expressions    ) {
        this.ir_expressions = ir_expressions;
    }


    public List<ir_Expression> getIr_expressions() {
        return ir_expressions;
    }

    public void addIr_expression(Ir_expression ir_expression) {
        this.ir_expressions.add(ir_expression);
    }
    public ir_Action getIr_action() {
        return ir_action;
    }

    public void setIr_action(ir_Action ir_action) {
        this.ir_action = ir_action;
    }

}