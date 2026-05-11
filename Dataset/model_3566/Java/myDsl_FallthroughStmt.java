





import java.util.List;
import java.util.ArrayList;

public class myDsl_FallthroughStmt  {

    private String fallthrough;





    private myDsl_Statement mydsl_statement;


    public myDsl_FallthroughStmt(
        String fallthrough    ) {
        this.fallthrough = fallthrough;
    }


    public String getFallthrough() {
        return fallthrough;
    }

    public void setFallthrough(String fallthrough) {
        this.fallthrough = fallthrough;
    }

    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }

}