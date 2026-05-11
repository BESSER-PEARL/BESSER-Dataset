





import java.util.List;
import java.util.ArrayList;

public class wh_ExprNot  {

    private String hasNot;





    private wh_ExprOr wh_expror;


    public wh_ExprNot(
        String hasNot    ) {
        this.hasNot = hasNot;
    }


    public String getHasnot() {
        return hasNot;
    }

    public void setHasnot(String hasNot) {
        this.hasNot = hasNot;
    }

    public wh_ExprOr getWh_expror() {
        return wh_expror;
    }

    public void setWh_expror(wh_ExprOr wh_expror) {
        this.wh_expror = wh_expror;
    }

}