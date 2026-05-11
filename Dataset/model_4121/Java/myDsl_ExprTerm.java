





import java.util.List;
import java.util.ArrayList;

public class myDsl_ExprTerm  {

    private String termSym;
    private String termVar;





    private myDsl_Expr mydsl_expr;


    public myDsl_ExprTerm(
        String termSym,        String termVar    ) {
        this.termSym = termSym;
        this.termVar = termVar;
    }


    public String getTermsym() {
        return termSym;
    }

    public void setTermsym(String termSym) {
        this.termSym = termSym;
    }
    public String getTermvar() {
        return termVar;
    }

    public void setTermvar(String termVar) {
        this.termVar = termVar;
    }

    public myDsl_Expr getMydsl_expr() {
        return mydsl_expr;
    }

    public void setMydsl_expr(myDsl_Expr mydsl_expr) {
        this.mydsl_expr = mydsl_expr;
    }

}