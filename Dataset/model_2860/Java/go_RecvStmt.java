





import java.util.List;
import java.util.ArrayList;

public class go_RecvStmt  {






    private go_ExpressionList go_expressionlist;




    private go_IdentifierList go_identifierlist;




    private go_CommCase go_commcase;


    public go_RecvStmt(
    ) {
    }



    public go_ExpressionList getGo_expressionlist() {
        return go_expressionlist;
    }

    public void setGo_expressionlist(go_ExpressionList go_expressionlist) {
        this.go_expressionlist = go_expressionlist;
    }
    public go_IdentifierList getGo_identifierlist() {
        return go_identifierlist;
    }

    public void setGo_identifierlist(go_IdentifierList go_identifierlist) {
        this.go_identifierlist = go_identifierlist;
    }
    public go_CommCase getGo_commcase() {
        return go_commcase;
    }

    public void setGo_commcase(go_CommCase go_commcase) {
        this.go_commcase = go_commcase;
    }

}