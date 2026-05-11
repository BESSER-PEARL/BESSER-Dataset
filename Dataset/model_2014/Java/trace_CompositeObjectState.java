





import java.util.List;
import java.util.ArrayList;

public class trace_CompositeObjectState extends ObjectState {

    private int objectstatesOrder;





    private List<trace_ObjectState> trace_objectstates;


    public trace_CompositeObjectState(
        int objectstatesOrder    ) {
        super(
        );
        this.objectstatesOrder = objectstatesOrder;
        this.trace_objectstates = new ArrayList<>();
    }

    public trace_CompositeObjectState(
        int objectstatesOrder        ArrayList<trace_ObjectState> trace_objectstates    ) {
        this.objectstatesOrder = objectstatesOrder;
        this.trace_objectstates = trace_objectstates;
    }

    public int getObjectstatesorder() {
        return objectstatesOrder;
    }

    public void setObjectstatesorder(int objectstatesOrder) {
        this.objectstatesOrder = objectstatesOrder;
    }

    public List<trace_ObjectState> getTrace_objectstates() {
        return trace_objectstates;
    }

    public void addTrace_objectstate(Trace_objectstate trace_objectstate) {
        this.trace_objectstates.add(trace_objectstate);
    }

}