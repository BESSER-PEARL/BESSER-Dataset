





import java.util.List;
import java.util.ArrayList;

public class cstat1_StateChart  {






    private List<cstat1_State> cstat1_states;


    public cstat1_StateChart(
    ) {
        this.cstat1_states = new ArrayList<>();
    }

    public cstat1_StateChart(
        ArrayList<cstat1_State> cstat1_states    ) {
        this.cstat1_states = cstat1_states;
    }


    public List<cstat1_State> getCstat1_states() {
        return cstat1_states;
    }

    public void addCstat1_state(Cstat1_state cstat1_state) {
        this.cstat1_states.add(cstat1_state);
    }

}