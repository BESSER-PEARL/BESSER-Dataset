





import java.util.List;
import java.util.ArrayList;

public class fiacre_Transition extends EModelElement {






    private fiacre_Process fiacre_process;




    private fiacre_State fiacre_state;




    private List<fiacre_State> fiacre_states;


    public fiacre_Transition(
    ) {
        super(
        );
        this.fiacre_states = new ArrayList<>();
    }

    public fiacre_Transition(
        ArrayList<fiacre_State> fiacre_states    ) {
        this.fiacre_states = fiacre_states;
    }


    public fiacre_Process getFiacre_process() {
        return fiacre_process;
    }

    public void setFiacre_process(fiacre_Process fiacre_process) {
        this.fiacre_process = fiacre_process;
    }
    public fiacre_State getFiacre_state() {
        return fiacre_state;
    }

    public void setFiacre_state(fiacre_State fiacre_state) {
        this.fiacre_state = fiacre_state;
    }
    public List<fiacre_State> getFiacre_states() {
        return fiacre_states;
    }

    public void addFiacre_state(Fiacre_state fiacre_state) {
        this.fiacre_states.add(fiacre_state);
    }

}