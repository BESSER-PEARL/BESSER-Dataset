





import java.util.List;
import java.util.ArrayList;

public class bpmn_Graph extends ArtifactsContainer, AssociationTarget {






    private List<bpmn_SequenceEdge> bpmn_sequenceedges;




    private bpmn_SequenceEdge bpmn_sequenceedge;


    public bpmn_Graph(
    ) {
        super(
        );
        this.bpmn_sequenceedges = new ArrayList<>();
    }

    public bpmn_Graph(
        ArrayList<bpmn_SequenceEdge> bpmn_sequenceedges    ) {
        this.bpmn_sequenceedges = bpmn_sequenceedges;
    }


    public List<bpmn_SequenceEdge> getBpmn_sequenceedges() {
        return bpmn_sequenceedges;
    }

    public void addBpmn_sequenceedge(Bpmn_sequenceedge bpmn_sequenceedge) {
        this.bpmn_sequenceedges.add(bpmn_sequenceedge);
    }
    public bpmn_SequenceEdge getBpmn_sequenceedge() {
        return bpmn_sequenceedge;
    }

    public void setBpmn_sequenceedge(bpmn_SequenceEdge bpmn_sequenceedge) {
        this.bpmn_sequenceedge = bpmn_sequenceedge;
    }

}