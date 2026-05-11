





import java.util.List;
import java.util.ArrayList;

public class diagraph_DLabel  {

    private boolean propagated;
    private boolean inferred;
    private boolean abztract;





    private diagraph_DLabeledElement diagraph_dlabeledelement;


    public diagraph_DLabel(
        boolean propagated,        boolean inferred,        boolean abztract    ) {
        this.propagated = propagated;
        this.inferred = inferred;
        this.abztract = abztract;
    }


    public boolean getPropagated() {
        return propagated;
    }

    public void setPropagated(boolean propagated) {
        this.propagated = propagated;
    }
    public boolean getInferred() {
        return inferred;
    }

    public void setInferred(boolean inferred) {
        this.inferred = inferred;
    }
    public boolean getAbztract() {
        return abztract;
    }

    public void setAbztract(boolean abztract) {
        this.abztract = abztract;
    }

    public diagraph_DLabeledElement getDiagraph_dlabeledelement() {
        return diagraph_dlabeledelement;
    }

    public void setDiagraph_dlabeledelement(diagraph_DLabeledElement diagraph_dlabeledelement) {
        this.diagraph_dlabeledelement = diagraph_dlabeledelement;
    }

}