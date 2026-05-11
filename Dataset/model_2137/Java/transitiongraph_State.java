





import java.util.List;
import java.util.ArrayList;

public class transitiongraph_State  {

    private int id;
    private boolean isInitial;
    private boolean isFinal;





    private transitiongraph_TransitionGraph transitiongraph_transitiongraph;


    public transitiongraph_State(
        int id,        boolean isInitial,        boolean isFinal    ) {
        this.id = id;
        this.isInitial = isInitial;
        this.isFinal = isFinal;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }
    public boolean getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(boolean isFinal) {
        this.isFinal = isFinal;
    }

    public transitiongraph_TransitionGraph getTransitiongraph_transitiongraph() {
        return transitiongraph_transitiongraph;
    }

    public void setTransitiongraph_transitiongraph(transitiongraph_TransitionGraph transitiongraph_transitiongraph) {
        this.transitiongraph_transitiongraph = transitiongraph_transitiongraph;
    }

}