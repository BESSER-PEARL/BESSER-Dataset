





import java.util.List;
import java.util.ArrayList;

public class ptnet_TransitionNode extends Node {






    private List<ptnet_RefTransition> ptnet_reftransitions;




    private ptnet_RefTransition ptnet_reftransition;


    public ptnet_TransitionNode(
    ) {
        super(
        );
        this.ptnet_reftransitions = new ArrayList<>();
    }

    public ptnet_TransitionNode(
        ArrayList<ptnet_RefTransition> ptnet_reftransitions    ) {
        this.ptnet_reftransitions = ptnet_reftransitions;
    }


    public List<ptnet_RefTransition> getPtnet_reftransitions() {
        return ptnet_reftransitions;
    }

    public void addPtnet_reftransition(Ptnet_reftransition ptnet_reftransition) {
        this.ptnet_reftransitions.add(ptnet_reftransition);
    }
    public ptnet_RefTransition getPtnet_reftransition() {
        return ptnet_reftransition;
    }

    public void setPtnet_reftransition(ptnet_RefTransition ptnet_reftransition) {
        this.ptnet_reftransition = ptnet_reftransition;
    }

}