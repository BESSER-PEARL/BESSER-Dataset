





import java.util.List;
import java.util.ArrayList;

public class thingML_CompositeState extends StateContainer, State {






    private thingML_Thing thingml_thing;


    public thingML_CompositeState(
    ) {
        super(
        );
    }



    public thingML_Thing getThingml_thing() {
        return thingml_thing;
    }

    public void setThingml_thing(thingML_Thing thingml_thing) {
        this.thingml_thing = thingml_thing;
    }

}