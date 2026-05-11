





import java.util.List;
import java.util.ArrayList;

public class sooml_StateMachine  {






    private sooml_State sooml_state;




    private List<sooml_State> sooml_states;




    private sooml_Class sooml_class;




    private sooml_Class sooml_class;


    public sooml_StateMachine(
    ) {
        this.sooml_states = new ArrayList<>();
    }

    public sooml_StateMachine(
        ArrayList<sooml_State> sooml_states    ) {
        this.sooml_states = sooml_states;
    }


    public sooml_State getSooml_state() {
        return sooml_state;
    }

    public void setSooml_state(sooml_State sooml_state) {
        this.sooml_state = sooml_state;
    }
    public List<sooml_State> getSooml_states() {
        return sooml_states;
    }

    public void addSooml_state(Sooml_state sooml_state) {
        this.sooml_states.add(sooml_state);
    }
    public sooml_Class getSooml_class() {
        return sooml_class;
    }

    public void setSooml_class(sooml_Class sooml_class) {
        this.sooml_class = sooml_class;
    }
    public sooml_Class getSooml_class() {
        return sooml_class;
    }

    public void setSooml_class(sooml_Class sooml_class) {
        this.sooml_class = sooml_class;
    }

}