





import java.util.List;
import java.util.ArrayList;

public class limp_IfThenElseStatement extends Statement {






    private limp_StatementBlock limp_statementblock;




    private limp_Else limp_else;




    private limp_Expr limp_expr;


    public limp_IfThenElseStatement(
    ) {
        super(
        );
    }



    public limp_StatementBlock getLimp_statementblock() {
        return limp_statementblock;
    }

    public void setLimp_statementblock(limp_StatementBlock limp_statementblock) {
        this.limp_statementblock = limp_statementblock;
    }
    public limp_Else getLimp_else() {
        return limp_else;
    }

    public void setLimp_else(limp_Else limp_else) {
        this.limp_else = limp_else;
    }
    public limp_Expr getLimp_expr() {
        return limp_expr;
    }

    public void setLimp_expr(limp_Expr limp_expr) {
        this.limp_expr = limp_expr;
    }

}