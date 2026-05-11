





import java.util.List;
import java.util.ArrayList;

public class thingml_Property extends Variable {

    private boolean changeable;





    private thingml_PropertyAssign thingml_propertyassign;




    private thingml_Thing thingml_thing;




    private thingml_State thingml_state;




    private thingml_Expression thingml_expression;




    private thingml_ConfigPropertyAssign thingml_configpropertyassign;


    public thingml_Property(
        boolean changeable    ) {
        super(
        );
        this.changeable = changeable;
    }


    public boolean getChangeable() {
        return changeable;
    }

    public void setChangeable(boolean changeable) {
        this.changeable = changeable;
    }

    public thingml_PropertyAssign getThingml_propertyassign() {
        return thingml_propertyassign;
    }

    public void setThingml_propertyassign(thingml_PropertyAssign thingml_propertyassign) {
        this.thingml_propertyassign = thingml_propertyassign;
    }
    public thingml_Thing getThingml_thing() {
        return thingml_thing;
    }

    public void setThingml_thing(thingml_Thing thingml_thing) {
        this.thingml_thing = thingml_thing;
    }
    public thingml_State getThingml_state() {
        return thingml_state;
    }

    public void setThingml_state(thingml_State thingml_state) {
        this.thingml_state = thingml_state;
    }
    public thingml_Expression getThingml_expression() {
        return thingml_expression;
    }

    public void setThingml_expression(thingml_Expression thingml_expression) {
        this.thingml_expression = thingml_expression;
    }
    public thingml_ConfigPropertyAssign getThingml_configpropertyassign() {
        return thingml_configpropertyassign;
    }

    public void setThingml_configpropertyassign(thingml_ConfigPropertyAssign thingml_configpropertyassign) {
        this.thingml_configpropertyassign = thingml_configpropertyassign;
    }

}