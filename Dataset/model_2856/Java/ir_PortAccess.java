





import java.util.List;
import java.util.ArrayList;

public class ir_PortAccess extends Node {






    private ir_Expression ir_expression;




    private ir_Port ir_port;


    public ir_PortAccess(
    ) {
        super(
        );
    }



    public ir_Expression getIr_expression() {
        return ir_expression;
    }

    public void setIr_expression(ir_Expression ir_expression) {
        this.ir_expression = ir_expression;
    }
    public ir_Port getIr_port() {
        return ir_port;
    }

    public void setIr_port(ir_Port ir_port) {
        this.ir_port = ir_port;
    }

}