





import java.util.List;
import java.util.ArrayList;

public class mMDSL_WhileLoop  {






    private mMDSL_LoopStatement mmdsl_loopstatement;




    private mMDSL_Expr mmdsl_expr;




    private List<mMDSL_Statement> mmdsl_statements;


    public mMDSL_WhileLoop(
    ) {
        this.mmdsl_statements = new ArrayList<>();
    }

    public mMDSL_WhileLoop(
        ArrayList<mMDSL_Statement> mmdsl_statements    ) {
        this.mmdsl_statements = mmdsl_statements;
    }


    public mMDSL_LoopStatement getMmdsl_loopstatement() {
        return mmdsl_loopstatement;
    }

    public void setMmdsl_loopstatement(mMDSL_LoopStatement mmdsl_loopstatement) {
        this.mmdsl_loopstatement = mmdsl_loopstatement;
    }
    public mMDSL_Expr getMmdsl_expr() {
        return mmdsl_expr;
    }

    public void setMmdsl_expr(mMDSL_Expr mmdsl_expr) {
        this.mmdsl_expr = mmdsl_expr;
    }
    public List<mMDSL_Statement> getMmdsl_statements() {
        return mmdsl_statements;
    }

    public void addMmdsl_statement(Mmdsl_statement mmdsl_statement) {
        this.mmdsl_statements.add(mmdsl_statement);
    }

}