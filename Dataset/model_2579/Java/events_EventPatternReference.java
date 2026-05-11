





import java.util.List;
import java.util.ArrayList;

public class events_EventPatternReference  {

    private String parameterSymbolicNames;





    private events_EventPattern events_eventpattern;


    public events_EventPatternReference(
        String parameterSymbolicNames    ) {
        this.parameterSymbolicNames = parameterSymbolicNames;
    }


    public String getParametersymbolicnames() {
        return parameterSymbolicNames;
    }

    public void setParametersymbolicnames(String parameterSymbolicNames) {
        this.parameterSymbolicNames = parameterSymbolicNames;
    }

    public events_EventPattern getEvents_eventpattern() {
        return events_eventpattern;
    }

    public void setEvents_eventpattern(events_EventPattern events_eventpattern) {
        this.events_eventpattern = events_eventpattern;
    }

}