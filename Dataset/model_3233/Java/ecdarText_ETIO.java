





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETIO  {

    private String type;





    private ecdarText_ETEdge ecdartext_etedge;




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

    public ecdarText_ETEdge getEcdartext_etedge() {
        return ecdartext_etedge;
    }

    public void setEcdartext_etedge(ecdarText_ETEdge ecdartext_etedge) {
        this.ecdartext_etedge = ecdartext_etedge;
    }
    public ecdarText_ETExpression getEcdartext_etexpression() {
        return ecdartext_etexpression;
    }

    public void setEcdartext_etexpression(ecdarText_ETExpression ecdartext_etexpression) {
        this.ecdartext_etexpression = ecdartext_etexpression;
    }

}