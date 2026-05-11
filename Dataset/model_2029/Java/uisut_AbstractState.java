





import java.util.List;
import java.util.ArrayList;

public class uisut_AbstractState extends UISUTElement {






    private uisut_UIStatemachine uisut_uistatemachine;




    private uisut_UITransition uisut_uitransition;




    private List<uisut_UITransition> uisut_uitransitions;




    private List<uisut_UITransition> uisut_uitransitions;




    private uisut_UITransition uisut_uitransition;


    public uisut_AbstractState(
    ) {
        super(
        );
        this.uisut_uitransitions = new ArrayList<>();
        this.uisut_uitransitions = new ArrayList<>();
    }

    public uisut_AbstractState(
        ArrayList<uisut_UITransition> uisut_uitransitions,        ArrayList<uisut_UITransition> uisut_uitransitions    ) {
        this.uisut_uitransitions = uisut_uitransitions;
        this.uisut_uitransitions = uisut_uitransitions;
    }


    public uisut_UIStatemachine getUisut_uistatemachine() {
        return uisut_uistatemachine;
    }

    public void setUisut_uistatemachine(uisut_UIStatemachine uisut_uistatemachine) {
        this.uisut_uistatemachine = uisut_uistatemachine;
    }
    public uisut_UITransition getUisut_uitransition() {
        return uisut_uitransition;
    }

    public void setUisut_uitransition(uisut_UITransition uisut_uitransition) {
        this.uisut_uitransition = uisut_uitransition;
    }
    public List<uisut_UITransition> getUisut_uitransitions() {
        return uisut_uitransitions;
    }

    public void addUisut_uitransition(Uisut_uitransition uisut_uitransition) {
        this.uisut_uitransitions.add(uisut_uitransition);
    }
    public List<uisut_UITransition> getUisut_uitransitions() {
        return uisut_uitransitions;
    }

    public void addUisut_uitransition(Uisut_uitransition uisut_uitransition) {
        this.uisut_uitransitions.add(uisut_uitransition);
    }
    public uisut_UITransition getUisut_uitransition() {
        return uisut_uitransition;
    }

    public void setUisut_uitransition(uisut_UITransition uisut_uitransition) {
        this.uisut_uitransition = uisut_uitransition;
    }

}