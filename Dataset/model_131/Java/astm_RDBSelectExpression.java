





import java.util.List;
import java.util.ArrayList;

public class astm_RDBSelectExpression extends Expression {






    private astm_RDBSelectStatement astm_rdbselectstatement;




    private List<astm_Expression> astm_expressions;


    public astm_RDBSelectExpression(
    ) {
        super(
        );
        this.astm_expressions = new ArrayList<>();
    }

    public astm_RDBSelectExpression(
        ArrayList<astm_Expression> astm_expressions    ) {
        this.astm_expressions = astm_expressions;
    }


    public astm_RDBSelectStatement getAstm_rdbselectstatement() {
        return astm_rdbselectstatement;
    }

    public void setAstm_rdbselectstatement(astm_RDBSelectStatement astm_rdbselectstatement) {
        this.astm_rdbselectstatement = astm_rdbselectstatement;
    }
    public List<astm_Expression> getAstm_expressions() {
        return astm_expressions;
    }

    public void addAstm_expression(Astm_expression astm_expression) {
        this.astm_expressions.add(astm_expression);
    }

}