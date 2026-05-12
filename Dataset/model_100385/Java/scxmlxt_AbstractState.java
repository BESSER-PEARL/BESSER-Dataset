





import java.util.List;
import java.util.ArrayList;

public class scxmlxt_AbstractState  {






    private List<scxmlxt_State> scxmlxt_states;


    public scxmlxt_AbstractState(
    ) {
        this.scxmlxt_states = new ArrayList<>();
    }

    public scxmlxt_AbstractState(
        ArrayList<scxmlxt_State> scxmlxt_states    ) {
        this.scxmlxt_states = scxmlxt_states;
    }


    public List<scxmlxt_State> getScxmlxt_states() {
        return scxmlxt_states;
    }

    public void addScxmlxt_state(Scxmlxt_state scxmlxt_state) {
        this.scxmlxt_states.add(scxmlxt_state);
    }

}