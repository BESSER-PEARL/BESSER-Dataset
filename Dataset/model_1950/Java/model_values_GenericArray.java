





import java.util.List;
import java.util.ArrayList;

public class model_values_GenericArray extends AArrayValue {






    private List<Value> values;


    public model_values_GenericArray(
    ) {
        super(
        );
        this.values = new ArrayList<>();
    }

    public model_values_GenericArray(
        ArrayList<Value> values    ) {
        this.values = values;
    }


    public List<Value> getValues() {
        return values;
    }

    public void addValue(Value value) {
        this.values.add(value);
    }

}