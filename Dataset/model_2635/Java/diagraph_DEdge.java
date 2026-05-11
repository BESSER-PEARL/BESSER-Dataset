





import java.util.List;
import java.util.ArrayList;

public class diagraph_DEdge extends DGraphElement {

    private boolean propagated;



    public diagraph_DEdge(
        boolean propagated    ) {
        super(
        );
        this.propagated = propagated;
    }


    public boolean getPropagated() {
        return propagated;
    }

    public void setPropagated(boolean propagated) {
        this.propagated = propagated;
    }


}