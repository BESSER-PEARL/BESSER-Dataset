





import java.util.List;
import java.util.ArrayList;

public class go_RangeClause  {






    private go_IdentifierList go_identifierlist;




    private go_Expression go_expression;




    private go_ExpressionList go_expressionlist;




    private go_ForStmt go_forstmt;


    public go_RangeClause(
    ) {
    }



    public go_IdentifierList getGo_identifierlist() {
        return go_identifierlist;
    }

    public void setGo_identifierlist(go_IdentifierList go_identifierlist) {
        this.go_identifierlist = go_identifierlist;
    }
    public go_Expression getGo_expression() {
        return go_expression;
    }

    public void setGo_expression(go_Expression go_expression) {
        this.go_expression = go_expression;
    }
    public go_ExpressionList getGo_expressionlist() {
        return go_expressionlist;
    }

    public void setGo_expressionlist(go_ExpressionList go_expressionlist) {
        this.go_expressionlist = go_expressionlist;
    }
    public go_ForStmt getGo_forstmt() {
        return go_forstmt;
    }

    public void setGo_forstmt(go_ForStmt go_forstmt) {
        this.go_forstmt = go_forstmt;
    }

}