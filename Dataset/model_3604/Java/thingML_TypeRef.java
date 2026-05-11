





import java.util.List;
import java.util.ArrayList;

public class thingML_TypeRef  {

    private boolean isArray;





    private thingML_Variable thingml_variable;




    private thingML_Type thingml_type;




    private thingML_Function thingml_function;


    public thingML_TypeRef(
        boolean isArray    ) {
        this.isArray = isArray;
    }


    public boolean getIsarray() {
        return isArray;
    }

    public void setIsarray(boolean isArray) {
        this.isArray = isArray;
    }

    public thingML_Variable getThingml_variable() {
        return thingml_variable;
    }

    public void setThingml_variable(thingML_Variable thingml_variable) {
        this.thingml_variable = thingml_variable;
    }
    public thingML_Type getThingml_type() {
        return thingml_type;
    }

    public void setThingml_type(thingML_Type thingml_type) {
        this.thingml_type = thingml_type;
    }
    public thingML_Function getThingml_function() {
        return thingml_function;
    }

    public void setThingml_function(thingML_Function thingml_function) {
        this.thingml_function = thingml_function;
    }

}