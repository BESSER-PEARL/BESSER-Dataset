





import java.util.List;
import java.util.ArrayList;

public class myDsl_BreakStmt  {

    private String break_;





    private myDsl_Statement mydsl_statement;


    public myDsl_BreakStmt(
        String break_    ) {
        this.break_ = break_;
    }


    public String getBreak_() {
        return break_;
    }

    public void setBreak_(String break_) {
        this.break_ = break_;
    }

    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }

}