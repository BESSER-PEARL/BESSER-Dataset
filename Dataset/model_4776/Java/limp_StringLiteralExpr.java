





import java.util.List;
import java.util.ArrayList;

public class limp_StringLiteralExpr extends Expr {

    private String stringVal;



    public limp_StringLiteralExpr(
        String stringVal    ) {
        super(
        );
        this.stringVal = stringVal;
    }


    public String getStringval() {
        return stringVal;
    }

    public void setStringval(String stringVal) {
        this.stringVal = stringVal;
    }


}