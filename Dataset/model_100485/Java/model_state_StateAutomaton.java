





import java.util.List;
import java.util.ArrayList;

public class model_state_StateAutomaton  {






    private List<TransitionSegment> transitionsegments;


    public model_state_StateAutomaton(
    ) {
        this.transitionsegments = new ArrayList<>();
    }

    public model_state_StateAutomaton(
        ArrayList<TransitionSegment> transitionsegments    ) {
        this.transitionsegments = transitionsegments;
    }


    public List<TransitionSegment> getTransitionsegments() {
        return transitionsegments;
    }

    public void addTransitionsegment(Transitionsegment transitionsegment) {
        this.transitionsegments.add(transitionsegment);
    }

}