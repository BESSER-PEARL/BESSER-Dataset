





import java.util.List;
import java.util.ArrayList;

public class thingML_RequiredPort extends Port {

    private boolean optional;



    public thingML_RequiredPort(
        boolean optional    ) {
        super(
        );
        this.optional = optional;
    }


    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }


}