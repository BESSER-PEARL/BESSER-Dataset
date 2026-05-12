





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_constraints_Constraint extends SQLObject {

    private boolean deferrable;
    private boolean initiallyDeferred;
    private boolean enforced;



    public sqlmodel_constraints_Constraint(
        boolean deferrable,        boolean initiallyDeferred,        boolean enforced    ) {
        super(
        );
        this.deferrable = deferrable;
        this.initiallyDeferred = initiallyDeferred;
        this.enforced = enforced;
    }


    public boolean getDeferrable() {
        return deferrable;
    }

    public void setDeferrable(boolean deferrable) {
        this.deferrable = deferrable;
    }
    public boolean getInitiallydeferred() {
        return initiallyDeferred;
    }

    public void setInitiallydeferred(boolean initiallyDeferred) {
        this.initiallyDeferred = initiallyDeferred;
    }
    public boolean getEnforced() {
        return enforced;
    }

    public void setEnforced(boolean enforced) {
        this.enforced = enforced;
    }


}