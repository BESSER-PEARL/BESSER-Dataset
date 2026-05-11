





import java.util.List;
import java.util.ArrayList;

public class myDsl_UnaryExpr  {






    private myDsl_Expression mydsl_expression;




    private myDsl_PrimaryExpr mydsl_primaryexpr;


    public myDsl_UnaryExpr(
    ) {
    }



    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public myDsl_PrimaryExpr getMydsl_primaryexpr() {
        return mydsl_primaryexpr;
    }

    public void setMydsl_primaryexpr(myDsl_PrimaryExpr mydsl_primaryexpr) {
        this.mydsl_primaryexpr = mydsl_primaryexpr;
    }

}