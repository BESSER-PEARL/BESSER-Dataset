





import java.util.List;
import java.util.ArrayList;

public class dtmc_DTMC extends IDBase {

    private String name;





    private List<dtmc_State> dtmc_states;




    private dtmc_State dtmc_state;


    public dtmc_DTMC(
        String name    ) {
        super(
        );
        this.name = name;
        this.dtmc_states = new ArrayList<>();
    }

    public dtmc_DTMC(
        String name        ArrayList<dtmc_State> dtmc_states    ) {
        this.name = name;
        this.dtmc_states = dtmc_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<dtmc_State> getDtmc_states() {
        return dtmc_states;
    }

    public void addDtmc_state(Dtmc_state dtmc_state) {
        this.dtmc_states.add(dtmc_state);
    }
    public dtmc_State getDtmc_state() {
        return dtmc_state;
    }

    public void setDtmc_state(dtmc_State dtmc_state) {
        this.dtmc_state = dtmc_state;
    }

}