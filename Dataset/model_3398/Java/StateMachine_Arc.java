





import java.util.List;
import java.util.ArrayList;

public class StateMachine_Arc  {

    private int weight;
    private boolean toPlace;





    private StateMachine_Place statemachine_place;




    private StateMachine_PNTransition statemachine_pntransition;


    public StateMachine_Arc(
        int weight,        boolean toPlace    ) {
        this.weight = weight;
        this.toPlace = toPlace;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }
    public boolean getToplace() {
        return toPlace;
    }

    public void setToplace(boolean toPlace) {
        this.toPlace = toPlace;
    }

    public StateMachine_Place getStatemachine_place() {
        return statemachine_place;
    }

    public void setStatemachine_place(StateMachine_Place statemachine_place) {
        this.statemachine_place = statemachine_place;
    }
    public StateMachine_PNTransition getStatemachine_pntransition() {
        return statemachine_pntransition;
    }

    public void setStatemachine_pntransition(StateMachine_PNTransition statemachine_pntransition) {
        this.statemachine_pntransition = statemachine_pntransition;
    }

}