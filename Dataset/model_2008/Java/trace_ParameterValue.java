





import java.util.List;
import java.util.ArrayList;

public class trace_ParameterValue  {

    private String DirectionKind;





    private trace_Step trace_step;




    private List<trace_Value> trace_values;


    public trace_ParameterValue(
        String DirectionKind    ) {
        this.DirectionKind = DirectionKind;
        this.trace_values = new ArrayList<>();
    }

    public trace_ParameterValue(
        String DirectionKind        ArrayList<trace_Value> trace_values    ) {
        this.DirectionKind = DirectionKind;
        this.trace_values = trace_values;
    }

    public String getDirectionkind() {
        return DirectionKind;
    }

    public void setDirectionkind(String DirectionKind) {
        this.DirectionKind = DirectionKind;
    }

    public trace_Step getTrace_step() {
        return trace_step;
    }

    public void setTrace_step(trace_Step trace_step) {
        this.trace_step = trace_step;
    }
    public List<trace_Value> getTrace_values() {
        return trace_values;
    }

    public void addTrace_value(Trace_value trace_value) {
        this.trace_values.add(trace_value);
    }

}