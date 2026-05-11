





import java.util.List;
import java.util.ArrayList;

public class thingml_Configuration extends AnnotatedElement {

    private boolean fragment;



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


}