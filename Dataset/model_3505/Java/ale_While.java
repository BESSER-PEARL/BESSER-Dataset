





import java.util.List;
import java.util.ArrayList;

public class ale_While extends Statement {






    private ale_ExpressionStmt ale_expressionstmt;




    private ale_Block ale_block;


    public ale_While(
    ) {
        super(
        );
    }



    public ale_ExpressionStmt getAle_expressionstmt() {
        return ale_expressionstmt;
    }

    public void setAle_expressionstmt(ale_ExpressionStmt ale_expressionstmt) {
        this.ale_expressionstmt = ale_expressionstmt;
    }
    public ale_Block getAle_block() {
        return ale_block;
    }

    public void setAle_block(ale_Block ale_block) {
        this.ale_block = ale_block;
    }

}