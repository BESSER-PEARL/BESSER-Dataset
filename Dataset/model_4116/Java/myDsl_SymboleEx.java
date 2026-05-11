





import java.util.List;
import java.util.ArrayList;

public class myDsl_SymboleEx  {

    private String p;





    private myDsl_ExprSimple mydsl_exprsimple;


    public myDsl_SymboleEx(
        String p    ) {
        this.p = p;
    }


    public String getP() {
        return p;
    }

    public void setP(String p) {
        this.p = p;
    }

    public myDsl_ExprSimple getMydsl_exprsimple() {
        return mydsl_exprsimple;
    }

    public void setMydsl_exprsimple(myDsl_ExprSimple mydsl_exprsimple) {
        this.mydsl_exprsimple = mydsl_exprsimple;
    }

}