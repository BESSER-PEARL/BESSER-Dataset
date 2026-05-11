





import java.util.List;
import java.util.ArrayList;

public class ale_VarDecl extends Statement {

    private String name;





    private ale_ExpressionStmt ale_expressionstmt;




    private ale_rType ale_rtype;


    public ale_VarDecl(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ale_ExpressionStmt getAle_expressionstmt() {
        return ale_expressionstmt;
    }

    public void setAle_expressionstmt(ale_ExpressionStmt ale_expressionstmt) {
        this.ale_expressionstmt = ale_expressionstmt;
    }
    public ale_rType getAle_rtype() {
        return ale_rtype;
    }

    public void setAle_rtype(ale_rType ale_rtype) {
        this.ale_rtype = ale_rtype;
    }

}