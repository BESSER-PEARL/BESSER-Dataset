





import java.util.List;
import java.util.ArrayList;

public class diagraph_DLabeledEdge extends DLabeledElement, DLineEdge, DOwnedEdge {






    private diagraph_EReference diagraph_ereference;


    public diagraph_DLabeledEdge(
    ) {
        super(
        );
    }



    public diagraph_EReference getDiagraph_ereference() {
        return diagraph_ereference;
    }

    public void setDiagraph_ereference(diagraph_EReference diagraph_ereference) {
        this.diagraph_ereference = diagraph_ereference;
    }

}