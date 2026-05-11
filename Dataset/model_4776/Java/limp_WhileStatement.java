





import java.util.List;
import java.util.ArrayList;

public class limp_WhileStatement extends Statement {






    private limp_Expr limp_expr;




    private limp_StatementBlock limp_statementblock;


    public limp_WhileStatement(
    ) {
        super(
        );
    }



    public limp_Expr getLimp_expr() {
        return limp_expr;
    }

    public void setLimp_expr(limp_Expr limp_expr) {
        this.limp_expr = limp_expr;
    }
    public limp_StatementBlock getLimp_statementblock() {
        return limp_statementblock;
    }

    public void setLimp_statementblock(limp_StatementBlock limp_statementblock) {
        this.limp_statementblock = limp_statementblock;
    }

}