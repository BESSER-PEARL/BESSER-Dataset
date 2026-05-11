





import java.util.List;
import java.util.ArrayList;

public class z7fsm_AbstractState  {

    private String id;





    private z7fsm_Region z7fsm_region;




    private List<z7fsm_AbstractState> z7fsm_abstractstates;


    public z7fsm_AbstractState(
        String id    ) {
        this.id = id;
        this.z7fsm_abstractstates = new ArrayList<>();
    }

    public z7fsm_AbstractState(
        String id        ArrayList<z7fsm_AbstractState> z7fsm_abstractstates    ) {
        this.id = id;
        this.z7fsm_abstractstates = z7fsm_abstractstates;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public z7fsm_Region getZ7fsm_region() {
        return z7fsm_region;
    }

    public void setZ7fsm_region(z7fsm_Region z7fsm_region) {
        this.z7fsm_region = z7fsm_region;
    }
    public List<z7fsm_AbstractState> getZ7fsm_abstractstates() {
        return z7fsm_abstractstates;
    }

    public void addZ7fsm_abstractstate(Z7fsm_abstractstate z7fsm_abstractstate) {
        this.z7fsm_abstractstates.add(z7fsm_abstractstate);
    }

}