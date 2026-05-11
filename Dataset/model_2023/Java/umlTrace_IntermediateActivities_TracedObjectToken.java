





import java.util.List;
import java.util.ArrayList;

public class umlTrace_IntermediateActivities_TracedObjectToken extends TracedToken {






    private List<ObjectToken_value_Value> objecttoken_value_values;


    public umlTrace_IntermediateActivities_TracedObjectToken(
    ) {
        super(
        );
        this.objecttoken_value_values = new ArrayList<>();
    }

    public umlTrace_IntermediateActivities_TracedObjectToken(
        ArrayList<ObjectToken_value_Value> objecttoken_value_values    ) {
        this.objecttoken_value_values = objecttoken_value_values;
    }


    public List<ObjectToken_value_Value> getObjecttoken_value_values() {
        return objecttoken_value_values;
    }

    public void addObjecttoken_value_value(Objecttoken_value_value objecttoken_value_value) {
        this.objecttoken_value_values.add(objecttoken_value_value);
    }

}