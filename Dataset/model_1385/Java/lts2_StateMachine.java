





import java.util.List;
import java.util.ArrayList;

public class lts2_StateMachine  {






    private lts2_AbortState lts2_abortstate;




    private List<lts2_TransitionalState> lts2_transitionalstates;




    private lts2_FinalState lts2_finalstate;




    private lts2_InitialState lts2_initialstate;


    public lts2_StateMachine(
    ) {
        this.lts2_transitionalstates = new ArrayList<>();
    }

    public lts2_StateMachine(
        ArrayList<lts2_TransitionalState> lts2_transitionalstates    ) {
        this.lts2_transitionalstates = lts2_transitionalstates;
    }


    public lts2_AbortState getLts2_abortstate() {
        return lts2_abortstate;
    }

    public void setLts2_abortstate(lts2_AbortState lts2_abortstate) {
        this.lts2_abortstate = lts2_abortstate;
    }
    public List<lts2_TransitionalState> getLts2_transitionalstates() {
        return lts2_transitionalstates;
    }

    public void addLts2_transitionalstate(Lts2_transitionalstate lts2_transitionalstate) {
        this.lts2_transitionalstates.add(lts2_transitionalstate);
    }
    public lts2_FinalState getLts2_finalstate() {
        return lts2_finalstate;
    }

    public void setLts2_finalstate(lts2_FinalState lts2_finalstate) {
        this.lts2_finalstate = lts2_finalstate;
    }
    public lts2_InitialState getLts2_initialstate() {
        return lts2_initialstate;
    }

    public void setLts2_initialstate(lts2_InitialState lts2_initialstate) {
        this.lts2_initialstate = lts2_initialstate;
    }

}