





import java.util.List;
import java.util.ArrayList;

public class thingml_Configuration extends AnnotatedElement {

    private boolean fragment;





    private thingml_ThingMLModel thingml_thingmlmodel;


    public thingml_Configuration(
        boolean fragment    ) {
        super(
        );
        this.fragment = fragment;
    }


    public boolean getFragment() {
        return fragment;
    }

    public void setFragment(boolean fragment) {
        this.fragment = fragment;
    }

    public thingml_ThingMLModel getThingml_thingmlmodel() {
        return thingml_thingmlmodel;
    }

    public void setThingml_thingmlmodel(thingml_ThingMLModel thingml_thingmlmodel) {
        this.thingml_thingmlmodel = thingml_thingmlmodel;
    }

}