





import java.util.List;
import java.util.ArrayList;

public class myDsl_SimpleStmt  {






    private myDsl_ShortVarDecl mydsl_shortvardecl;




    private myDsl_Expression mydsl_expression;




    private myDsl_Statement mydsl_statement;


    public myDsl_SimpleStmt(
    ) {
    }



    public myDsl_ShortVarDecl getMydsl_shortvardecl() {
        return mydsl_shortvardecl;
    }

    public void setMydsl_shortvardecl(myDsl_ShortVarDecl mydsl_shortvardecl) {
        this.mydsl_shortvardecl = mydsl_shortvardecl;
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

}