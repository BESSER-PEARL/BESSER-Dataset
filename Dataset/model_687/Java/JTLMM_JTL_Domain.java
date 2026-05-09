





import java.util.List;
import java.util.ArrayList;

public class JTLMM_JTL_Domain extends NamedElement {

    private boolean isEnforceable;
    private boolean isCheckable;



    public JTLMM_JTL_Domain(
        boolean isEnforceable,        boolean isCheckable    ) {
        super(
        );
        this.isEnforceable = isEnforceable;
        this.isCheckable = isCheckable;
    }


    public boolean getIsenforceable() {
        return isEnforceable;
    }

    public void setIsenforceable(boolean isEnforceable) {
        this.isEnforceable = isEnforceable;
    }
    public boolean getIscheckable() {
        return isCheckable;
    }

    public void setIscheckable(boolean isCheckable) {
        this.isCheckable = isCheckable;
    }


}