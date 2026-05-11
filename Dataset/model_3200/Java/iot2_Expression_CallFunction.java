





import java.util.List;
import java.util.ArrayList;

public class iot2_Expression_CallFunction extends Expression {






    private iot2_Functioncall_Arguments iot2_functioncall_arguments;




    private iot2_Expression iot2_expression;


    public iot2_Expression_CallFunction(
    ) {
        super(
        );
    }



    public iot2_Functioncall_Arguments getIot2_functioncall_arguments() {
        return iot2_functioncall_arguments;
    }

    public void setIot2_functioncall_arguments(iot2_Functioncall_Arguments iot2_functioncall_arguments) {
        this.iot2_functioncall_arguments = iot2_functioncall_arguments;
    }
    public iot2_Expression getIot2_expression() {
        return iot2_expression;
    }

    public void setIot2_expression(iot2_Expression iot2_expression) {
        this.iot2_expression = iot2_expression;
    }

}