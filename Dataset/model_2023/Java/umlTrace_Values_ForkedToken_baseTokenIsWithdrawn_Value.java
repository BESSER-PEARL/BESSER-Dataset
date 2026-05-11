





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value  {

    private boolean baseTokenIsWithdrawn;





    private List<Values_umlTrace_State> values_umltrace_states;


    public umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value(
        boolean baseTokenIsWithdrawn    ) {
        this.baseTokenIsWithdrawn = baseTokenIsWithdrawn;
        this.values_umltrace_states = new ArrayList<>();
    }

    public umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value(
        boolean baseTokenIsWithdrawn        ArrayList<Values_umlTrace_State> values_umltrace_states    ) {
        this.baseTokenIsWithdrawn = baseTokenIsWithdrawn;
        this.values_umltrace_states = values_umltrace_states;
    }

    public boolean getBasetokeniswithdrawn() {
        return baseTokenIsWithdrawn;
    }

    public void setBasetokeniswithdrawn(boolean baseTokenIsWithdrawn) {
        this.baseTokenIsWithdrawn = baseTokenIsWithdrawn;
    }

    public List<Values_umlTrace_State> getValues_umltrace_states() {
        return values_umltrace_states;
    }

    public void addValues_umltrace_state(Values_umltrace_state values_umltrace_state) {
        this.values_umltrace_states.add(values_umltrace_state);
    }

}