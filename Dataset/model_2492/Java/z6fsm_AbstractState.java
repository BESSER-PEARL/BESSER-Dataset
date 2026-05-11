





import java.util.List;
import java.util.ArrayList;

public class z6fsm_AbstractState  {

    private String id;





    private List<z6fsm_AbstractState> z6fsm_abstractstates;




    private z6fsm_Region z6fsm_region;


    public z6fsm_AbstractState(
        String id    ) {
        this.id = id;
        this.z6fsm_abstractstates = new ArrayList<>();
    }

    public z6fsm_AbstractState(
        String id        ArrayList<z6fsm_AbstractState> z6fsm_abstractstates    ) {
        this.id = id;
        this.z6fsm_abstractstates = z6fsm_abstractstates;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<z6fsm_AbstractState> getZ6fsm_abstractstates() {
        return z6fsm_abstractstates;
    }

    public void addZ6fsm_abstractstate(Z6fsm_abstractstate z6fsm_abstractstate) {
        this.z6fsm_abstractstates.add(z6fsm_abstractstate);
    }
    public z6fsm_Region getZ6fsm_region() {
        return z6fsm_region;
    }

    public void setZ6fsm_region(z6fsm_Region z6fsm_region) {
        this.z6fsm_region = z6fsm_region;
    }

}