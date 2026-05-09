





import java.util.List;
import java.util.ArrayList;

public class astm_ArrayAccess extends Expression {






    private astm_Expression astm_expression;




    private List<astm_Expression> astm_expressions;


    public astm_ArrayAccess(
    ) {
        super(
        );
        this.astm_expressions = new ArrayList<>();
    }

    public astm_ArrayAccess(
        ArrayList<astm_Expression> astm_expressions    ) {
        this.astm_expressions = astm_expressions;
    }


    public astm_Expression getAstm_expression() {
        return astm_expression;
    }

    public void setAstm_expression(astm_Expression astm_expression) {
        this.astm_expression = astm_expression;
    }
    public List<astm_Expression> getAstm_expressions() {
        return astm_expressions;
    }

    public void addAstm_expression(Astm_expression astm_expression) {
        this.astm_expressions.add(astm_expression);
    }

}