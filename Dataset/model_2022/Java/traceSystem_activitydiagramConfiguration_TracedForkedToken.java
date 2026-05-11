





import java.util.List;
import java.util.ArrayList;

public class traceSystem_activitydiagramConfiguration_TracedForkedToken extends TracedToken {






    private List<ForkedToken_remainingOffersCount_State> forkedtoken_remainingofferscount_states;




    private List<ForkedToken_baseToken_State> forkedtoken_basetoken_states;




    private List<ForkedToken_baseTokenIsWithdrawn_State> forkedtoken_basetokeniswithdrawn_states;


    public traceSystem_activitydiagramConfiguration_TracedForkedToken(
    ) {
        super(
        );
        this.forkedtoken_remainingofferscount_states = new ArrayList<>();
        this.forkedtoken_basetoken_states = new ArrayList<>();
        this.forkedtoken_basetokeniswithdrawn_states = new ArrayList<>();
    }

    public traceSystem_activitydiagramConfiguration_TracedForkedToken(
        ArrayList<ForkedToken_remainingOffersCount_State> forkedtoken_remainingofferscount_states,        ArrayList<ForkedToken_baseToken_State> forkedtoken_basetoken_states,        ArrayList<ForkedToken_baseTokenIsWithdrawn_State> forkedtoken_basetokeniswithdrawn_states    ) {
        this.forkedtoken_remainingofferscount_states = forkedtoken_remainingofferscount_states;
        this.forkedtoken_basetoken_states = forkedtoken_basetoken_states;
        this.forkedtoken_basetokeniswithdrawn_states = forkedtoken_basetokeniswithdrawn_states;
    }


    public List<ForkedToken_remainingOffersCount_State> getForkedtoken_remainingofferscount_states() {
        return forkedtoken_remainingofferscount_states;
    }

    public void addForkedtoken_remainingofferscount_state(Forkedtoken_remainingofferscount_state forkedtoken_remainingofferscount_state) {
        this.forkedtoken_remainingofferscount_states.add(forkedtoken_remainingofferscount_state);
    }
    public List<ForkedToken_baseToken_State> getForkedtoken_basetoken_states() {
        return forkedtoken_basetoken_states;
    }

    public void addForkedtoken_basetoken_state(Forkedtoken_basetoken_state forkedtoken_basetoken_state) {
        this.forkedtoken_basetoken_states.add(forkedtoken_basetoken_state);
    }
    public List<ForkedToken_baseTokenIsWithdrawn_State> getForkedtoken_basetokeniswithdrawn_states() {
        return forkedtoken_basetokeniswithdrawn_states;
    }

    public void addForkedtoken_basetokeniswithdrawn_state(Forkedtoken_basetokeniswithdrawn_state forkedtoken_basetokeniswithdrawn_state) {
        this.forkedtoken_basetokeniswithdrawn_states.add(forkedtoken_basetokeniswithdrawn_state);
    }

}