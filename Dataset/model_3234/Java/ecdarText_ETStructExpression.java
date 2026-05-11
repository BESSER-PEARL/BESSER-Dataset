





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETStructExpression extends ETExpression {

    private String right;





    private ecdarText_ETExpression ecdartext_etexpression;


    public ecdarText_ETStructExpression(
        String right    ) {
        super(
        );
        this.right = right;
    }


    public String getRight() {
        return right;
    }

    public void setRight(String right) {
        this.right = right;
    }

    public ecdarText_ETExpression getEcdartext_etexpression() {
        return ecdartext_etexpression;
    }

    public void setEcdartext_etexpression(ecdarText_ETExpression ecdartext_etexpression) {
        this.ecdartext_etexpression = ecdartext_etexpression;
    }

}