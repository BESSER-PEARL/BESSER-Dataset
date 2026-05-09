





import java.util.List;
import java.util.ArrayList;

public class astm_SwitchStatement extends Statement {






    private astm_SwitchCase astm_switchcase;




    private astm_Expression astm_expression;


    public astm_SwitchStatement(
    ) {
        super(
        );
    }



    public astm_SwitchCase getAstm_switchcase() {
        return astm_switchcase;
    }

    public void setAstm_switchcase(astm_SwitchCase astm_switchcase) {
        this.astm_switchcase = astm_switchcase;
    }
    public astm_Expression getAstm_expression() {
        return astm_expression;
    }

    public void setAstm_expression(astm_Expression astm_expression) {
        this.astm_expression = astm_expression;
    }

}