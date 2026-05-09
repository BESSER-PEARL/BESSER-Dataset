





import java.util.List;
import java.util.ArrayList;

public class pnml_ArcTransition2Place extends Element {






    private pnml_TransitionElement pnml_transitionelement;




    private pnml_PlaceElement pnml_placeelement;


    public pnml_ArcTransition2Place(
    ) {
        super(
        );
    }



    public pnml_TransitionElement getPnml_transitionelement() {
        return pnml_transitionelement;
    }

    public void setPnml_transitionelement(pnml_TransitionElement pnml_transitionelement) {
        this.pnml_transitionelement = pnml_transitionelement;
    }
    public pnml_PlaceElement getPnml_placeelement() {
        return pnml_placeelement;
    }

    public void setPnml_placeelement(pnml_PlaceElement pnml_placeelement) {
        this.pnml_placeelement = pnml_placeelement;
    }

}