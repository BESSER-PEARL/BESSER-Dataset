





import java.util.List;
import java.util.ArrayList;

public class myDsl_ShortVarDecl  {






    private myDsl_IdentifierList mydsl_identifierlist;




    private myDsl_ExpressionList mydsl_expressionlist;


    public myDsl_ShortVarDecl(
    ) {
    }



    public myDsl_IdentifierList getMydsl_identifierlist() {
        return mydsl_identifierlist;
    }

    public void setMydsl_identifierlist(myDsl_IdentifierList mydsl_identifierlist) {
        this.mydsl_identifierlist = mydsl_identifierlist;
    }
    public myDsl_ExpressionList getMydsl_expressionlist() {
        return mydsl_expressionlist;
    }

    public void setMydsl_expressionlist(myDsl_ExpressionList mydsl_expressionlist) {
        this.mydsl_expressionlist = mydsl_expressionlist;
    }

}