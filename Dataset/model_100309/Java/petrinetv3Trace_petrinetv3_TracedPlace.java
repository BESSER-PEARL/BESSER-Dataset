





import java.util.List;
import java.util.ArrayList;

public class petrinetv3Trace_petrinetv3_TracedPlace  {






    private List<Place_tokens_Value> place_tokens_values;


    public petrinetv3Trace_petrinetv3_TracedPlace(
    ) {
        this.place_tokens_values = new ArrayList<>();
    }

    public petrinetv3Trace_petrinetv3_TracedPlace(
        ArrayList<Place_tokens_Value> place_tokens_values    ) {
        this.place_tokens_values = place_tokens_values;
    }


    public List<Place_tokens_Value> getPlace_tokens_values() {
        return place_tokens_values;
    }

    public void addPlace_tokens_value(Place_tokens_value place_tokens_value) {
        this.place_tokens_values.add(place_tokens_value);
    }

}