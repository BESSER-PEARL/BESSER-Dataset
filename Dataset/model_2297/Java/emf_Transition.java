





import java.util.List;
import java.util.ArrayList;

public class emf_Transition  {

    private String action;





    private emf_State emf_state;




    private emf_TransitionToStateMapEntry emf_transitiontostatemapentry;


    public emf_Transition(
        String action    ) {
        this.action = action;
    }


    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public emf_State getEmf_state() {
        return emf_state;
    }

    public void setEmf_state(emf_State emf_state) {
        this.emf_state = emf_state;
    }
    public emf_TransitionToStateMapEntry getEmf_transitiontostatemapentry() {
        return emf_transitiontostatemapentry;
    }

    public void setEmf_transitiontostatemapentry(emf_TransitionToStateMapEntry emf_transitiontostatemapentry) {
        this.emf_transitiontostatemapentry = emf_transitiontostatemapentry;
    }

}