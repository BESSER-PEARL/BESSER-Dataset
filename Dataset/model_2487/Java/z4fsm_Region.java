





import java.util.List;
import java.util.ArrayList;

public class z4fsm_Region  {

    private String name;





    private List<z4fsm_AbstractState> z4fsm_abstractstates;


    public z4fsm_Region(
        String name    ) {
        this.name = name;
        this.z4fsm_abstractstates = new ArrayList<>();
    }

    public z4fsm_Region(
        String name        ArrayList<z4fsm_AbstractState> z4fsm_abstractstates    ) {
        this.name = name;
        this.z4fsm_abstractstates = z4fsm_abstractstates;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<z4fsm_AbstractState> getZ4fsm_abstractstates() {
        return z4fsm_abstractstates;
    }

    public void addZ4fsm_abstractstate(Z4fsm_abstractstate z4fsm_abstractstate) {
        this.z4fsm_abstractstates.add(z4fsm_abstractstate);
    }

}