





import java.util.List;
import java.util.ArrayList;

public class myDsl_GoStmt  {

    private String go;





    private myDsl_Statement mydsl_statement;




    private myDsl_Expression mydsl_expression;


    public myDsl_GoStmt(
        String go    ) {
        this.go = go;
    }


    public String getGo() {
        return go;
    }

    public void setGo(String go) {
        this.go = go;
    }

    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }
    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }

}