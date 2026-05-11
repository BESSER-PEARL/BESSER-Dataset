





import java.util.List;
import java.util.ArrayList;

public class thingML_EventReference extends Expression {






    private thingML_Parameter thingml_parameter;




    private thingML_Event thingml_event;


    public thingML_EventReference(
    ) {
        super(
        );
    }



    public thingML_Parameter getThingml_parameter() {
        return thingml_parameter;
    }

    public void setThingml_parameter(thingML_Parameter thingml_parameter) {
        this.thingml_parameter = thingml_parameter;
    }
    public thingML_Event getThingml_event() {
        return thingml_event;
    }

    public void setThingml_event(thingML_Event thingml_event) {
        this.thingml_event = thingml_event;
    }

}