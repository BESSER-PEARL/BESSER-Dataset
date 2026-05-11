





import java.util.List;
import java.util.ArrayList;

public class ClockRDL_statements_LoopStmt extends Statement {






    private kernel_Expression kernel_expression;




    private statements_BlockStmt statements_blockstmt;


    public ClockRDL_statements_LoopStmt(
    ) {
        super(
        );
    }



    public kernel_Expression getKernel_expression() {
        return kernel_expression;
    }

    public void setKernel_expression(kernel_Expression kernel_expression) {
        this.kernel_expression = kernel_expression;
    }
    public statements_BlockStmt getStatements_blockstmt() {
        return statements_blockstmt;
    }

    public void setStatements_blockstmt(statements_BlockStmt statements_blockstmt) {
        this.statements_blockstmt = statements_blockstmt;
    }

}