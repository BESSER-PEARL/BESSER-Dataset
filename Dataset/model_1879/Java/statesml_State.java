





import java.util.List;
import java.util.ArrayList;

public class statesml_State extends Node {

    private boolean isInitial;
    private boolean isTerminal;





    private statesml_SelectionDivergence statesml_selectiondivergence;


    public statesml_State(
        boolean isInitial,        boolean isTerminal    ) {
        super(
        );
        this.isInitial = isInitial;
        this.isTerminal = isTerminal;
    }


    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }
    public boolean getIsterminal() {
        return isTerminal;
    }

    public void setIsterminal(boolean isTerminal) {
        this.isTerminal = isTerminal;
    }

    public statesml_SelectionDivergence getStatesml_selectiondivergence() {
        return statesml_selectiondivergence;
    }

    public void setStatesml_selectiondivergence(statesml_SelectionDivergence statesml_selectiondivergence) {
        this.statesml_selectiondivergence = statesml_selectiondivergence;
    }

}