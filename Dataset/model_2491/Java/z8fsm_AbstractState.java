





import java.util.List;
import java.util.ArrayList;

public class z8fsm_AbstractState  {

    private String id;





    private z8fsm_Region z8fsm_region;




    private List<z8fsm_AbstractState> z8fsm_abstractstates;


    public z8fsm_AbstractState(
        String id    ) {
        this.id = id;
        this.z8fsm_abstractstates = new ArrayList<>();
    }

    public z8fsm_AbstractState(
        String id        ArrayList<z8fsm_AbstractState> z8fsm_abstractstates    ) {
        this.id = id;
        this.z8fsm_abstractstates = z8fsm_abstractstates;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public z8fsm_Region getZ8fsm_region() {
        return z8fsm_region;
    }

    public void setZ8fsm_region(z8fsm_Region z8fsm_region) {
        this.z8fsm_region = z8fsm_region;
    }
    public List<z8fsm_AbstractState> getZ8fsm_abstractstates() {
        return z8fsm_abstractstates;
    }

    public void addZ8fsm_abstractstate(Z8fsm_abstractstate z8fsm_abstractstate) {
        this.z8fsm_abstractstates.add(z8fsm_abstractstate);
    }

}