





import java.util.List;
import java.util.ArrayList;

public class trace_petrinet_TracedPlace  {

    private int initialTokens;
    private String name;





    private List<Place_tokens_State> place_tokens_states;


    public trace_petrinet_TracedPlace(
        int initialTokens,        String name    ) {
        this.initialTokens = initialTokens;
        this.name = name;
        this.place_tokens_states = new ArrayList<>();
    }

    public trace_petrinet_TracedPlace(
        int initialTokens,        String name        ArrayList<Place_tokens_State> place_tokens_states    ) {
        this.initialTokens = initialTokens;
        this.name = name;
        this.place_tokens_states = place_tokens_states;
    }

    public int getInitialtokens() {
        return initialTokens;
    }

    public void setInitialtokens(int initialTokens) {
        this.initialTokens = initialTokens;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Place_tokens_State> getPlace_tokens_states() {
        return place_tokens_states;
    }

    public void addPlace_tokens_state(Place_tokens_state place_tokens_state) {
        this.place_tokens_states.add(place_tokens_state);
    }

}