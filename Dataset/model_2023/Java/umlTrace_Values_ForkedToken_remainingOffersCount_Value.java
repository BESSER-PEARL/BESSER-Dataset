





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_ForkedToken_remainingOffersCount_Value  {

    private int remainingOffersCount;





    private List<Values_umlTrace_State> values_umltrace_states;


    public umlTrace_Values_ForkedToken_remainingOffersCount_Value(
        int remainingOffersCount    ) {
        this.remainingOffersCount = remainingOffersCount;
        this.values_umltrace_states = new ArrayList<>();
    }

    public umlTrace_Values_ForkedToken_remainingOffersCount_Value(
        int remainingOffersCount        ArrayList<Values_umlTrace_State> values_umltrace_states    ) {
        this.remainingOffersCount = remainingOffersCount;
        this.values_umltrace_states = values_umltrace_states;
    }

    public int getRemainingofferscount() {
        return remainingOffersCount;
    }

    public void setRemainingofferscount(int remainingOffersCount) {
        this.remainingOffersCount = remainingOffersCount;
    }

    public List<Values_umlTrace_State> getValues_umltrace_states() {
        return values_umltrace_states;
    }

    public void addValues_umltrace_state(Values_umltrace_state values_umltrace_state) {
        this.values_umltrace_states.add(values_umltrace_state);
    }

}