





import java.util.List;
import java.util.ArrayList;

public class uisut_UIStatemachine extends UISUTElement {






    private List<uisut_AbstractState> uisut_abstractstates;




    private List<uisut_UITransition> uisut_uitransitions;




    private List<uisut_UIDataVariable> uisut_uidatavariables;




    private uisut_UISUT uisut_uisut;


    public uisut_UIStatemachine(
    ) {
        super(
        );
        this.uisut_abstractstates = new ArrayList<>();
        this.uisut_uitransitions = new ArrayList<>();
        this.uisut_uidatavariables = new ArrayList<>();
    }

    public uisut_UIStatemachine(
        ArrayList<uisut_AbstractState> uisut_abstractstates,        ArrayList<uisut_UITransition> uisut_uitransitions,        ArrayList<uisut_UIDataVariable> uisut_uidatavariables    ) {
        this.uisut_abstractstates = uisut_abstractstates;
        this.uisut_uitransitions = uisut_uitransitions;
        this.uisut_uidatavariables = uisut_uidatavariables;
    }


    public List<uisut_AbstractState> getUisut_abstractstates() {
        return uisut_abstractstates;
    }

    public void addUisut_abstractstate(Uisut_abstractstate uisut_abstractstate) {
        this.uisut_abstractstates.add(uisut_abstractstate);
    }
    public List<uisut_UITransition> getUisut_uitransitions() {
        return uisut_uitransitions;
    }

    public void addUisut_uitransition(Uisut_uitransition uisut_uitransition) {
        this.uisut_uitransitions.add(uisut_uitransition);
    }
    public List<uisut_UIDataVariable> getUisut_uidatavariables() {
        return uisut_uidatavariables;
    }

    public void addUisut_uidatavariable(Uisut_uidatavariable uisut_uidatavariable) {
        this.uisut_uidatavariables.add(uisut_uidatavariable);
    }
    public uisut_UISUT getUisut_uisut() {
        return uisut_uisut;
    }

    public void setUisut_uisut(uisut_UISUT uisut_uisut) {
        this.uisut_uisut = uisut_uisut;
    }

}