





import java.util.List;
import java.util.ArrayList;

public class thingML_PropertyReference extends Expression {






    private thingML_Variable thingml_variable;




    private thingML_ForAction thingml_foraction;


    public thingML_PropertyReference(
    ) {
        super(
        );
    }



    public thingML_Variable getThingml_variable() {
        return thingml_variable;
    }

    public void setThingml_variable(thingML_Variable thingml_variable) {
        this.thingml_variable = thingml_variable;
    }
    public thingML_ForAction getThingml_foraction() {
        return thingml_foraction;
    }

    public void setThingml_foraction(thingML_ForAction thingml_foraction) {
        this.thingml_foraction = thingml_foraction;
    }

}