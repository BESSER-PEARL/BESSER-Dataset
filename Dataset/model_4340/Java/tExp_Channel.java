





import java.util.List;
import java.util.ArrayList;

public class tExp_Channel  {

    private String name;
    private String reliability;





    private tExp_EventType texp_eventtype;




    private tExp_TraceExpression texp_traceexpression;


    public tExp_Channel(
        String name,        String reliability    ) {
        this.name = name;
        this.reliability = reliability;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReliability() {
        return reliability;
    }

    public void setReliability(String reliability) {
        this.reliability = reliability;
    }

    public tExp_EventType getTexp_eventtype() {
        return texp_eventtype;
    }

    public void setTexp_eventtype(tExp_EventType texp_eventtype) {
        this.texp_eventtype = texp_eventtype;
    }
    public tExp_TraceExpression getTexp_traceexpression() {
        return texp_traceexpression;
    }

    public void setTexp_traceexpression(tExp_TraceExpression texp_traceexpression) {
        this.texp_traceexpression = texp_traceexpression;
    }

}