





import java.util.List;
import java.util.ArrayList;

public class astm_SwitchStatement extends Statement {






    private astm_Expression astm_expression;




    private List<astm_SwitchCase> astm_switchcases;


    public astm_SwitchStatement(
    ) {
        super(
        );
        this.astm_switchcases = new ArrayList<>();
    }

    public astm_SwitchStatement(
        ArrayList<astm_SwitchCase> astm_switchcases    ) {
        this.astm_switchcases = astm_switchcases;
    }


    public astm_Expression getAstm_expression() {
        return astm_expression;
    }

    public void setAstm_expression(astm_Expression astm_expression) {
        this.astm_expression = astm_expression;
    }
    public List<astm_SwitchCase> getAstm_switchcases() {
        return astm_switchcases;
    }

    public void addAstm_switchcase(Astm_switchcase astm_switchcase) {
        this.astm_switchcases.add(astm_switchcase);
    }

}