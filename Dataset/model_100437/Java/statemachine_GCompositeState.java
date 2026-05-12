





import java.util.List;
import java.util.ArrayList;

public class statemachine_GCompositeState extends GState {






    private List<statemachine_GAbstractState> statemachine_gabstractstates;


    public statemachine_GCompositeState(
    ) {
        super(
        );
        this.statemachine_gabstractstates = new ArrayList<>();
    }

    public statemachine_GCompositeState(
        ArrayList<statemachine_GAbstractState> statemachine_gabstractstates    ) {
        this.statemachine_gabstractstates = statemachine_gabstractstates;
    }


    public List<statemachine_GAbstractState> getStatemachine_gabstractstates() {
        return statemachine_gabstractstates;
    }

    public void addStatemachine_gabstractstate(Statemachine_gabstractstate statemachine_gabstractstate) {
        this.statemachine_gabstractstates.add(statemachine_gabstractstate);
    }

}