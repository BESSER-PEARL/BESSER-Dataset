





import java.util.List;
import java.util.ArrayList;

public class myDsl_Let extends TopLevelCmd, Expr {

    private String name;





    private myDsl_Expr mydsl_expr;




    private myDsl_Expr mydsl_expr;


    public myDsl_Let(
        String name    ) {
        super(
        );
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
    public myDsl_Expr getMydsl_expr() {
        return mydsl_expr;
    }

    public void setMydsl_expr(myDsl_Expr mydsl_expr) {
        this.mydsl_expr = mydsl_expr;
    }

}