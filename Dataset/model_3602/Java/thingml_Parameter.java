





import java.util.List;
import java.util.ArrayList;

public class thingml_Parameter extends Variable {






    private thingml_Function thingml_function;




    private thingml_Message thingml_message;


    public thingml_Parameter(
    ) {
        super(
        );
    }



    public thingml_Function getThingml_function() {
        return thingml_function;
    }

    public void setThingml_function(thingml_Function thingml_function) {
        this.thingml_function = thingml_function;
    }
    public thingml_Message getThingml_message() {
        return thingml_message;
    }

    public void setThingml_message(thingml_Message thingml_message) {
        this.thingml_message = thingml_message;
    }

}