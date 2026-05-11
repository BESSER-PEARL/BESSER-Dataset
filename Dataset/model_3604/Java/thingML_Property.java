





import java.util.List;
import java.util.ArrayList;

public class thingML_Property extends Variable {

    private boolean readonly;





    private thingML_Expression thingml_expression;




    private thingML_State thingml_state;




    private thingML_Thing thingml_thing;




    private thingML_PropertyAssign thingml_propertyassign;


    public thingML_Property(
        boolean readonly    ) {
        super(
        );
        this.readonly = readonly;
    }


    public boolean getReadonly() {
        return readonly;
    }

    public void setReadonly(boolean readonly) {
        this.readonly = readonly;
    }

    public thingML_Expression getThingml_expression() {
        return thingml_expression;
    }

    public void setThingml_expression(thingML_Expression thingml_expression) {
        this.thingml_expression = thingml_expression;
    }
    public thingML_State getThingml_state() {
        return thingml_state;
    }

    public void setThingml_state(thingML_State thingml_state) {
        this.thingml_state = thingml_state;
    }
    public thingML_Thing getThingml_thing() {
        return thingml_thing;
    }

    public void setThingml_thing(thingML_Thing thingml_thing) {
        this.thingml_thing = thingml_thing;
    }
    public thingML_PropertyAssign getThingml_propertyassign() {
        return thingml_propertyassign;
    }

    public void setThingml_propertyassign(thingML_PropertyAssign thingml_propertyassign) {
        this.thingml_propertyassign = thingml_propertyassign;
    }

}