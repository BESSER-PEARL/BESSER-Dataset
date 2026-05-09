





import java.util.List;
import java.util.ArrayList;

public class statesml_Transition extends Node {






    private statesml_ChangeEvent statesml_changeevent;




    private statesml_State statesml_state;




    private statesml_SelectionDivergence statesml_selectiondivergence;




    private statesml_SelectionConvergence statesml_selectionconvergence;




    private statesml_State statesml_state;


    public statesml_Transition(
    ) {
        super(
        );
    }



    public statesml_ChangeEvent getStatesml_changeevent() {
        return statesml_changeevent;
    }

    public void setStatesml_changeevent(statesml_ChangeEvent statesml_changeevent) {
        this.statesml_changeevent = statesml_changeevent;
    }
    public statesml_State getStatesml_state() {
        return statesml_state;
    }

    public void setStatesml_state(statesml_State statesml_state) {
        this.statesml_state = statesml_state;
    }
    public statesml_SelectionDivergence getStatesml_selectiondivergence() {
        return statesml_selectiondivergence;
    }

    public void setStatesml_selectiondivergence(statesml_SelectionDivergence statesml_selectiondivergence) {
        this.statesml_selectiondivergence = statesml_selectiondivergence;
    }
    public statesml_SelectionConvergence getStatesml_selectionconvergence() {
        return statesml_selectionconvergence;
    }

    public void setStatesml_selectionconvergence(statesml_SelectionConvergence statesml_selectionconvergence) {
        this.statesml_selectionconvergence = statesml_selectionconvergence;
    }
    public statesml_State getStatesml_state() {
        return statesml_state;
    }

    public void setStatesml_state(statesml_State statesml_state) {
        this.statesml_state = statesml_state;
    }

}