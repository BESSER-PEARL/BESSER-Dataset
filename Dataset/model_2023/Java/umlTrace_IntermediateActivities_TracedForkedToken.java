





import java.util.List;
import java.util.ArrayList;

public class umlTrace_IntermediateActivities_TracedForkedToken extends TracedToken {






    private List<ForkedToken_baseToken_Value> forkedtoken_basetoken_values;




    private List<ForkedToken_baseTokenIsWithdrawn_Value> forkedtoken_basetokeniswithdrawn_values;




    private List<ForkedToken_remainingOffersCount_Value> forkedtoken_remainingofferscount_values;


    public umlTrace_IntermediateActivities_TracedForkedToken(
    ) {
        super(
        );
        this.forkedtoken_basetoken_values = new ArrayList<>();
        this.forkedtoken_basetokeniswithdrawn_values = new ArrayList<>();
        this.forkedtoken_remainingofferscount_values = new ArrayList<>();
    }

    public umlTrace_IntermediateActivities_TracedForkedToken(
        ArrayList<ForkedToken_baseToken_Value> forkedtoken_basetoken_values,        ArrayList<ForkedToken_baseTokenIsWithdrawn_Value> forkedtoken_basetokeniswithdrawn_values,        ArrayList<ForkedToken_remainingOffersCount_Value> forkedtoken_remainingofferscount_values    ) {
        this.forkedtoken_basetoken_values = forkedtoken_basetoken_values;
        this.forkedtoken_basetokeniswithdrawn_values = forkedtoken_basetokeniswithdrawn_values;
        this.forkedtoken_remainingofferscount_values = forkedtoken_remainingofferscount_values;
    }


    public List<ForkedToken_baseToken_Value> getForkedtoken_basetoken_values() {
        return forkedtoken_basetoken_values;
    }

    public void addForkedtoken_basetoken_value(Forkedtoken_basetoken_value forkedtoken_basetoken_value) {
        this.forkedtoken_basetoken_values.add(forkedtoken_basetoken_value);
    }
    public List<ForkedToken_baseTokenIsWithdrawn_Value> getForkedtoken_basetokeniswithdrawn_values() {
        return forkedtoken_basetokeniswithdrawn_values;
    }

    public void addForkedtoken_basetokeniswithdrawn_value(Forkedtoken_basetokeniswithdrawn_value forkedtoken_basetokeniswithdrawn_value) {
        this.forkedtoken_basetokeniswithdrawn_values.add(forkedtoken_basetokeniswithdrawn_value);
    }
    public List<ForkedToken_remainingOffersCount_Value> getForkedtoken_remainingofferscount_values() {
        return forkedtoken_remainingofferscount_values;
    }

    public void addForkedtoken_remainingofferscount_value(Forkedtoken_remainingofferscount_value forkedtoken_remainingofferscount_value) {
        this.forkedtoken_remainingofferscount_values.add(forkedtoken_remainingofferscount_value);
    }

}