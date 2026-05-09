





import java.util.List;
import java.util.ArrayList;

public class astm_TypeReference extends Type {






    private astm_FunctionType astm_functiontype;




    private astm_Expression astm_expression;


    public astm_TypeReference(
    ) {
        super(
        );
    }



    public astm_FunctionType getAstm_functiontype() {
        return astm_functiontype;
    }

    public void setAstm_functiontype(astm_FunctionType astm_functiontype) {
        this.astm_functiontype = astm_functiontype;
    }
    public astm_Expression getAstm_expression() {
        return astm_expression;
    }

    public void setAstm_expression(astm_Expression astm_expression) {
        this.astm_expression = astm_expression;
    }

}