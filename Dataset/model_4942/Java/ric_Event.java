





import java.util.List;
import java.util.ArrayList;

public class ric_Event  {

    private String type;





    private ric_EventComponent ric_eventcomponent;


    public ric_Event(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ric_EventComponent getRic_eventcomponent() {
        return ric_eventcomponent;
    }

    public void setRic_eventcomponent(ric_EventComponent ric_eventcomponent) {
        this.ric_eventcomponent = ric_eventcomponent;
    }

}