





import java.util.List;
import java.util.ArrayList;

public class scxml_AbstractSimpleState  {






    private scxml_InitialState scxml_initialstate;




    private List<scxml_FinalState> scxml_finalstates;




    private scxml_TransitionTarget scxml_transitiontarget;


    public scxml_AbstractSimpleState(
    ) {
        this.scxml_finalstates = new ArrayList<>();
    }

    public scxml_AbstractSimpleState(
        ArrayList<scxml_FinalState> scxml_finalstates    ) {
        this.scxml_finalstates = scxml_finalstates;
    }


    public scxml_InitialState getScxml_initialstate() {
        return scxml_initialstate;
    }

    public void setScxml_initialstate(scxml_InitialState scxml_initialstate) {
        this.scxml_initialstate = scxml_initialstate;
    }
    public List<scxml_FinalState> getScxml_finalstates() {
        return scxml_finalstates;
    }

    public void addScxml_finalstate(Scxml_finalstate scxml_finalstate) {
        this.scxml_finalstates.add(scxml_finalstate);
    }
    public scxml_TransitionTarget getScxml_transitiontarget() {
        return scxml_transitiontarget;
    }

    public void setScxml_transitiontarget(scxml_TransitionTarget scxml_transitiontarget) {
        this.scxml_transitiontarget = scxml_transitiontarget;
    }

}