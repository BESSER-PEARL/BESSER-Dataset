





import java.util.List;
import java.util.ArrayList;

public class calculatrice_VarCall extends CalcExpr {

    private String varCall;



    public calculatrice_VarCall(
        String varCall    ) {
        super(
        );
        this.varCall = varCall;
    }


    public String getVarcall() {
        return varCall;
    }

    public void setVarcall(String varCall) {
        this.varCall = varCall;
    }


}