





import java.util.List;
import java.util.ArrayList;

public class wh_ExprSimple extends Expr {

    private String sym;
    private String str;
    private String varSimple;





    private wh_ExprOr wh_expror;


    public wh_ExprSimple(
        String sym,        String str,        String varSimple    ) {
        super(
        );
        this.sym = sym;
        this.str = str;
        this.varSimple = varSimple;
    }


    public String getSym() {
        return sym;
    }

    public void setSym(String sym) {
        this.sym = sym;
    }
    public String getStr() {
        return str;
    }

    public void setStr(String str) {
        this.str = str;
    }
    public String getVarsimple() {
        return varSimple;
    }

    public void setVarsimple(String varSimple) {
        this.varSimple = varSimple;
    }

    public wh_ExprOr getWh_expror() {
        return wh_expror;
    }

    public void setWh_expror(wh_ExprOr wh_expror) {
        this.wh_expror = wh_expror;
    }

}