





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_TransitionNode extends Node {






    private pnmlcoremodel_RefTransition pnmlcoremodel_reftransition;




    private List<pnmlcoremodel_RefTransition> pnmlcoremodel_reftransitions;


    public pnmlcoremodel_TransitionNode(
    ) {
        super(
        );
        this.pnmlcoremodel_reftransitions = new ArrayList<>();
    }

    public pnmlcoremodel_TransitionNode(
        ArrayList<pnmlcoremodel_RefTransition> pnmlcoremodel_reftransitions    ) {
        this.pnmlcoremodel_reftransitions = pnmlcoremodel_reftransitions;
    }


    public pnmlcoremodel_RefTransition getPnmlcoremodel_reftransition() {
        return pnmlcoremodel_reftransition;
    }

    public void setPnmlcoremodel_reftransition(pnmlcoremodel_RefTransition pnmlcoremodel_reftransition) {
        this.pnmlcoremodel_reftransition = pnmlcoremodel_reftransition;
    }
    public List<pnmlcoremodel_RefTransition> getPnmlcoremodel_reftransitions() {
        return pnmlcoremodel_reftransitions;
    }

    public void addPnmlcoremodel_reftransition(Pnmlcoremodel_reftransition pnmlcoremodel_reftransition) {
        this.pnmlcoremodel_reftransitions.add(pnmlcoremodel_reftransition);
    }

}