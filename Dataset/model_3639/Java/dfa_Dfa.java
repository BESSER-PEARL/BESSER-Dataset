





import java.util.List;
import java.util.ArrayList;

public class dfa_Dfa extends NamedElement {






    private List<dfa_RegularState> dfa_regularstates;




    private List<dfa_FinalState> dfa_finalstates;




    private dfa_InitialState dfa_initialstate;


    public dfa_Dfa(
    ) {
        super(
        );
        this.dfa_regularstates = new ArrayList<>();
        this.dfa_finalstates = new ArrayList<>();
    }

    public dfa_Dfa(
        ArrayList<dfa_RegularState> dfa_regularstates,        ArrayList<dfa_FinalState> dfa_finalstates    ) {
        this.dfa_regularstates = dfa_regularstates;
        this.dfa_finalstates = dfa_finalstates;
    }


    public List<dfa_RegularState> getDfa_regularstates() {
        return dfa_regularstates;
    }

    public void addDfa_regularstate(Dfa_regularstate dfa_regularstate) {
        this.dfa_regularstates.add(dfa_regularstate);
    }
    public List<dfa_FinalState> getDfa_finalstates() {
        return dfa_finalstates;
    }

    public void addDfa_finalstate(Dfa_finalstate dfa_finalstate) {
        this.dfa_finalstates.add(dfa_finalstate);
    }
    public dfa_InitialState getDfa_initialstate() {
        return dfa_initialstate;
    }

    public void setDfa_initialstate(dfa_InitialState dfa_initialstate) {
        this.dfa_initialstate = dfa_initialstate;
    }

}