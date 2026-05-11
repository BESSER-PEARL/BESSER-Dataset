





import java.util.List;
import java.util.ArrayList;

public class turingmodel_State  {

    private String name;
    private boolean isEndState;





    private turingmodel_State turingmodel_state;




    private List<turingmodel_State> turingmodel_states;




    private turingmodel_TuringMachine turingmodel_turingmachine;




    private turingmodel_TuringMachine turingmodel_turingmachine;


    public turingmodel_State(
        String name,        boolean isEndState    ) {
        this.name = name;
        this.isEndState = isEndState;
        this.turingmodel_states = new ArrayList<>();
    }

    public turingmodel_State(
        String name,        boolean isEndState        ArrayList<turingmodel_State> turingmodel_states    ) {
        this.name = name;
        this.isEndState = isEndState;
        this.turingmodel_states = turingmodel_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsendstate() {
        return isEndState;
    }

    public void setIsendstate(boolean isEndState) {
        this.isEndState = isEndState;
    }

    public turingmodel_State getTuringmodel_state() {
        return turingmodel_state;
    }

    public void setTuringmodel_state(turingmodel_State turingmodel_state) {
        this.turingmodel_state = turingmodel_state;
    }
    public List<turingmodel_State> getTuringmodel_states() {
        return turingmodel_states;
    }

    public void addTuringmodel_state(Turingmodel_state turingmodel_state) {
        this.turingmodel_states.add(turingmodel_state);
    }
    public turingmodel_TuringMachine getTuringmodel_turingmachine() {
        return turingmodel_turingmachine;
    }

    public void setTuringmodel_turingmachine(turingmodel_TuringMachine turingmodel_turingmachine) {
        this.turingmodel_turingmachine = turingmodel_turingmachine;
    }
    public turingmodel_TuringMachine getTuringmodel_turingmachine() {
        return turingmodel_turingmachine;
    }

    public void setTuringmodel_turingmachine(turingmodel_TuringMachine turingmodel_turingmachine) {
        this.turingmodel_turingmachine = turingmodel_turingmachine;
    }

}