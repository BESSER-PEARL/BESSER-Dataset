





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETIO  {

    private String type;





    private ecdarText_ETExpression ecdartext_etexpression;


    public ecdarText_ETIO(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ecdarText_ETExpression getEcdartext_etexpression() {
        return ecdartext_etexpression;
    }

    public void setEcdartext_etexpression(ecdarText_ETExpression ecdartext_etexpression) {
        this.ecdartext_etexpression = ecdartext_etexpression;
    }

}