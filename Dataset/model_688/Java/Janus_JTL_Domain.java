





import java.util.List;
import java.util.ArrayList;

public class Janus_JTL_Domain extends NamedElement {

    private boolean isCheckable;
    private boolean isEnforceable;



    public Janus_JTL_Domain(
        boolean isCheckable,        boolean isEnforceable    ) {
        super(
        );
        this.isCheckable = isCheckable;
        this.isEnforceable = isEnforceable;
    }


    public boolean getIscheckable() {
        return isCheckable;
    }

    public void setIscheckable(boolean isCheckable) {
        this.isCheckable = isCheckable;
    }
    public boolean getIsenforceable() {
        return isEnforceable;
    }

    public void setIsenforceable(boolean isEnforceable) {
        this.isEnforceable = isEnforceable;
    }


}