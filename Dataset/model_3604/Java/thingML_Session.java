





import java.util.List;
import java.util.ArrayList;

public class thingML_Session extends StateContainer {






    private thingML_CompositeState thingml_compositestate;




    private thingML_Expression thingml_expression;




    private thingML_StartSession thingml_startsession;


    public thingML_Session(
    ) {
        super(
        );
    }



    public thingML_CompositeState getThingml_compositestate() {
        return thingml_compositestate;
    }

    public void setThingml_compositestate(thingML_CompositeState thingml_compositestate) {
        this.thingml_compositestate = thingml_compositestate;
    }
    public thingML_Expression getThingml_expression() {
        return thingml_expression;
    }

    public void setThingml_expression(thingML_Expression thingml_expression) {
        this.thingml_expression = thingml_expression;
    }
    public thingML_StartSession getThingml_startsession() {
        return thingml_startsession;
    }

    public void setThingml_startsession(thingML_StartSession thingml_startsession) {
        this.thingml_startsession = thingml_startsession;
    }

}