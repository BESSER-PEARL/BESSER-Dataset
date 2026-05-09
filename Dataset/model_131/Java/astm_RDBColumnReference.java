





import java.util.List;
import java.util.ArrayList;

public class astm_RDBColumnReference extends IdentifierReference {






    private astm_RDBSelectExpression astm_rdbselectexpression;




    private astm_RDBTableDefinition astm_rdbtabledefinition;




    private astm_Expression astm_expression;


    public astm_RDBColumnReference(
    ) {
        super(
        );
    }



    public astm_RDBSelectExpression getAstm_rdbselectexpression() {
        return astm_rdbselectexpression;
    }

    public void setAstm_rdbselectexpression(astm_RDBSelectExpression astm_rdbselectexpression) {
        this.astm_rdbselectexpression = astm_rdbselectexpression;
    }
    public astm_RDBTableDefinition getAstm_rdbtabledefinition() {
        return astm_rdbtabledefinition;
    }

    public void setAstm_rdbtabledefinition(astm_RDBTableDefinition astm_rdbtabledefinition) {
        this.astm_rdbtabledefinition = astm_rdbtabledefinition;
    }
    public astm_Expression getAstm_expression() {
        return astm_expression;
    }

    public void setAstm_expression(astm_Expression astm_expression) {
        this.astm_expression = astm_expression;
    }

}