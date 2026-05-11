





import java.util.List;
import java.util.ArrayList;

public class diagraph_DLabel  {

    private boolean propagated;
    private boolean abztract;
    private boolean inferred;



    public diagraph_DLabel(
        boolean propagated,        boolean abztract,        boolean inferred    ) {
        this.propagated = propagated;
        this.abztract = abztract;
        this.inferred = inferred;
    }


    public boolean getPropagated() {
        return propagated;
    }

    public void setPropagated(boolean propagated) {
        this.propagated = propagated;
    }
    public boolean getAbztract() {
        return abztract;
    }

    public void setAbztract(boolean abztract) {
        this.abztract = abztract;
    }
    public boolean getInferred() {
        return inferred;
    }

    public void setInferred(boolean inferred) {
        this.inferred = inferred;
    }


}