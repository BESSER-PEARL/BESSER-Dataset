





import java.util.List;
import java.util.ArrayList;

public class ClockRDL_declarations_TransitionDecl extends Declaration {






    private kernel_Expression kernel_expression;




    private kernel_Statement kernel_statement;


    public ClockRDL_declarations_TransitionDecl(
    ) {
        super(
        );
    }



    public kernel_Expression getKernel_expression() {
        return kernel_expression;
    }

    public void setKernel_expression(kernel_Expression kernel_expression) {
        this.kernel_expression = kernel_expression;
    }
    public kernel_Statement getKernel_statement() {
        return kernel_statement;
    }

    public void setKernel_statement(kernel_Statement kernel_statement) {
        this.kernel_statement = kernel_statement;
    }

}