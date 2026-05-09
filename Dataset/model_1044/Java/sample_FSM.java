





import java.util.List;
import java.util.ArrayList;

public class sample_FSM  {

    private String name;





    private List<sample_State> sample_states;


    public sample_FSM(
        String name    ) {
        this.name = name;
        this.sample_states = new ArrayList<>();
    }

    public sample_FSM(
        String name        ArrayList<sample_State> sample_states    ) {
        this.name = name;
        this.sample_states = sample_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<sample_State> getSample_states() {
        return sample_states;
    }

    public void addSample_state(Sample_state sample_state) {
        this.sample_states.add(sample_state);
    }

}