





import java.util.List;
import java.util.ArrayList;

public class statemachine_AttributeCondition extends AbstractCondition {






    private List<statemachine_StateAttribute> statemachine_stateattributes;


    public statemachine_AttributeCondition(
    ) {
        super(
        );
        this.statemachine_stateattributes = new ArrayList<>();
    }

    public statemachine_AttributeCondition(
        ArrayList<statemachine_StateAttribute> statemachine_stateattributes    ) {
        this.statemachine_stateattributes = statemachine_stateattributes;
    }


    public List<statemachine_StateAttribute> getStatemachine_stateattributes() {
        return statemachine_stateattributes;
    }

    public void addStatemachine_stateattribute(Statemachine_stateattribute statemachine_stateattribute) {
        this.statemachine_stateattributes.add(statemachine_stateattribute);
    }

}