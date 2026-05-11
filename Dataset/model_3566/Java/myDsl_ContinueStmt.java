





import java.util.List;
import java.util.ArrayList;

public class myDsl_ContinueStmt  {

    private String continue_;





    private myDsl_Statement mydsl_statement;


    public myDsl_ContinueStmt(
        String continue_    ) {
        this.continue_ = continue_;
    }


    public String getContinue_() {
        return continue_;
    }

    public void setContinue_(String continue_) {
        this.continue_ = continue_;
    }

    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }

}