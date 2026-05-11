





import java.util.List;
import java.util.ArrayList;

public class myDsl_GotoStmt  {

    private String goto;





    private myDsl_Statement mydsl_statement;


    public myDsl_GotoStmt(
        String goto    ) {
        this.goto = goto;
    }


    public String getGoto() {
        return goto;
    }

    public void setGoto(String goto) {
        this.goto = goto;
    }

    public myDsl_Statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_Statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }

}