





import java.util.List;
import java.util.ArrayList;

public class core_DefineVariable extends Statement, Variable {






    private core_Expression core_expression;


    public core_DefineVariable(
    ) {
        super(
        );
    }



    public core_Expression getCore_expression() {
        return core_expression;
    }

    public void setCore_expression(core_Expression core_expression) {
        this.core_expression = core_expression;
    }

}