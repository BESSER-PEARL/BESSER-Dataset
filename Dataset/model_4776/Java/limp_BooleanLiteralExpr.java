





import java.util.List;
import java.util.ArrayList;

public class limp_BooleanLiteralExpr extends Expr {

    private String boolVal;



    public limp_BooleanLiteralExpr(
        String boolVal    ) {
        super(
        );
        this.boolVal = boolVal;
    }


    public String getBoolval() {
        return boolVal;
    }

    public void setBoolval(String boolVal) {
        this.boolVal = boolVal;
    }


}