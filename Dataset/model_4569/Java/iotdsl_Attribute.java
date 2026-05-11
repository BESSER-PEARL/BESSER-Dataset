





import java.util.List;
import java.util.ArrayList;

public class iotdsl_Attribute  {

    private String name;





    private iotdsl_EventOccurrence iotdsl_eventoccurrence;


    public iotdsl_Attribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iotdsl_EventOccurrence getIotdsl_eventoccurrence() {
        return iotdsl_eventoccurrence;
    }

    public void setIotdsl_eventoccurrence(iotdsl_EventOccurrence iotdsl_eventoccurrence) {
        this.iotdsl_eventoccurrence = iotdsl_eventoccurrence;
    }

}