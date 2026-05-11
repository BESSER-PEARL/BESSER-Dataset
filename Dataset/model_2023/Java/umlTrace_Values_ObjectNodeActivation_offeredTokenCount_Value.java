





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value  {

    private int offeredTokenCount;





    private List<Values_umlTrace_State> values_umltrace_states;


    public umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value(
        int offeredTokenCount    ) {
        this.offeredTokenCount = offeredTokenCount;
        this.values_umltrace_states = new ArrayList<>();
    }

    public umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value(
        int offeredTokenCount        ArrayList<Values_umlTrace_State> values_umltrace_states    ) {
        this.offeredTokenCount = offeredTokenCount;
        this.values_umltrace_states = values_umltrace_states;
    }

    public int getOfferedtokencount() {
        return offeredTokenCount;
    }

    public void setOfferedtokencount(int offeredTokenCount) {
        this.offeredTokenCount = offeredTokenCount;
    }

    public List<Values_umlTrace_State> getValues_umltrace_states() {
        return values_umltrace_states;
    }

    public void addValues_umltrace_state(Values_umltrace_state values_umltrace_state) {
        this.values_umltrace_states.add(values_umltrace_state);
    }

}