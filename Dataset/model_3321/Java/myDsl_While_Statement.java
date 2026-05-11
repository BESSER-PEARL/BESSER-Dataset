





import java.util.List;
import java.util.ArrayList;

public class myDsl_While_Statement  {

    private String rparent;





    private myDsl_Expression mydsl_expression;




    private myDsl_Statement mydsl_statement;




    private myDsl_Statement mydsl_statement;


    public myDsl_While_Statement(
        String rparent    ) {
        this.rparent = rparent;
    }


    public String getRparent() {
        return rparent;
    }

    public void setRparent(String rparent) {
        this.rparent = rparent;
    }

    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }
    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }

}