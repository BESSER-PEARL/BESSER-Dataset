





import java.util.List;
import java.util.ArrayList;

public class atlext_OCL_PropertyCallExp extends OclExpression {

    private boolean isStaticCall;



    public atlext_OCL_PropertyCallExp(
        boolean isStaticCall    ) {
        super(
        );
        this.isStaticCall = isStaticCall;
    }


    public boolean getIsstaticcall() {
        return isStaticCall;
    }

    public void setIsstaticcall(boolean isStaticCall) {
        this.isStaticCall = isStaticCall;
    }


}