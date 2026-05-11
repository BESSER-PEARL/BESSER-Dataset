





import java.util.List;
import java.util.ArrayList;

public class myDsl_ReturnStmt  {

    private String return_;





    private myDsl_ExpressionList mydsl_expressionlist;




    private myDsl_Statement mydsl_statement;


    public myDsl_ReturnStmt(
        String return_    ) {
        this.return_ = return_;
    }


    public String getReturn_() {
        return return_;
    }

    public void setReturn_(String return_) {
        this.return_ = return_;
    }

    public myDsl_ExpressionList getMydsl_expressionlist() {
        return mydsl_expressionlist;
    }

    public void setMydsl_expressionlist(myDsl_ExpressionList mydsl_expressionlist) {
        this.mydsl_expressionlist = mydsl_expressionlist;
    }
    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }

}