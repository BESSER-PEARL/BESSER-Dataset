





import java.util.List;
import java.util.ArrayList;

public class myDsl_Field  {

    private String name;





    private myDsl_Expr mydsl_expr;




    private myDsl_BObject mydsl_bobject;


    public myDsl_Field(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_Expr getMydsl_expr() {
        return mydsl_expr;
    }

    public void setMydsl_expr(myDsl_Expr mydsl_expr) {
        this.mydsl_expr = mydsl_expr;
    }
    public myDsl_BObject getMydsl_bobject() {
        return mydsl_bobject;
    }

    public void setMydsl_bobject(myDsl_BObject mydsl_bobject) {
        this.mydsl_bobject = mydsl_bobject;
    }

}