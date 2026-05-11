





import java.util.List;
import java.util.ArrayList;

public class wh_ExprNot  {

    private String not_;





    private wh_ExprEq wh_expreq;




    private wh_ExprOr wh_expror;




    private wh_ExprOr wh_expror;


    public wh_ExprNot(
        String not_    ) {
        this.not_ = not_;
    }


    public String getNot_() {
        return not_;
    }

    public void setNot_(String not_) {
        this.not_ = not_;
    }

    public wh_ExprEq getWh_expreq() {
        return wh_expreq;
    }

    public void setWh_expreq(wh_ExprEq wh_expreq) {
        this.wh_expreq = wh_expreq;
    }
    public wh_ExprOr getWh_expror() {
        return wh_expror;
    }

    public void setWh_expror(wh_ExprOr wh_expror) {
        this.wh_expror = wh_expror;
    }
    public wh_ExprOr getWh_expror() {
        return wh_expror;
    }

    public void setWh_expror(wh_ExprOr wh_expror) {
        this.wh_expror = wh_expror;
    }

}