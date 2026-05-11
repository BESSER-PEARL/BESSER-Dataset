





import java.util.List;
import java.util.ArrayList;

public class whileDsl_ExprNot  {

    private boolean negation;





    private whileDsl_ExprOr whiledsl_expror;


    public whileDsl_ExprNot(
        boolean negation    ) {
        this.negation = negation;
    }


    public boolean getNegation() {
        return negation;
    }

    public void setNegation(boolean negation) {
        this.negation = negation;
    }

    public whileDsl_ExprOr getWhiledsl_expror() {
        return whiledsl_expror;
    }

    public void setWhiledsl_expror(whileDsl_ExprOr whiledsl_expror) {
        this.whiledsl_expror = whiledsl_expror;
    }

}