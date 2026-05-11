





import java.util.List;
import java.util.ArrayList;

public class limp_RealLiteralExpr extends Expr {

    private String realVal;



    public limp_RealLiteralExpr(
        String realVal    ) {
        super(
        );
        this.realVal = realVal;
    }


    public String getRealval() {
        return realVal;
    }

    public void setRealval(String realVal) {
        this.realVal = realVal;
    }


}