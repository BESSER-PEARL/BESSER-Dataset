





import java.util.List;
import java.util.ArrayList;

public class smDsl_Model  {

    private String name;





    private List<smDsl_State> smdsl_states;


    public smDsl_Model(
        String name    ) {
        this.name = name;
        this.smdsl_states = new ArrayList<>();
    }

    public smDsl_Model(
        String name        ArrayList<smDsl_State> smdsl_states    ) {
        this.name = name;
        this.smdsl_states = smdsl_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<smDsl_State> getSmdsl_states() {
        return smdsl_states;
    }

    public void addSmdsl_state(Smdsl_state smdsl_state) {
        this.smdsl_states.add(smdsl_state);
    }

}