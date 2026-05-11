





import java.util.List;
import java.util.ArrayList;

public class myDsl_MethodExpr  {






    private myDsl_MethodName mydsl_methodname;




    private myDsl_PrimaryExpr mydsl_primaryexpr;


    public myDsl_MethodExpr(
    ) {
    }



    public myDsl_MethodName getMydsl_methodname() {
        return mydsl_methodname;
    }

    public void setMydsl_methodname(myDsl_MethodName mydsl_methodname) {
        this.mydsl_methodname = mydsl_methodname;
    }
    public myDsl_PrimaryExpr getMydsl_primaryexpr() {
        return mydsl_primaryexpr;
    }

    public void setMydsl_primaryexpr(myDsl_PrimaryExpr mydsl_primaryexpr) {
        this.mydsl_primaryexpr = mydsl_primaryexpr;
    }

}