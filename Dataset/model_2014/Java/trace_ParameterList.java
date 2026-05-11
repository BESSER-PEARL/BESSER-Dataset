





import java.util.List;
import java.util.ArrayList;

public class trace_ParameterList  {






    private List<trace_ParameterValue> trace_parametervalues;




    private trace_Step trace_step;


    public trace_ParameterList(
    ) {
        this.trace_parametervalues = new ArrayList<>();
    }

    public trace_ParameterList(
        ArrayList<trace_ParameterValue> trace_parametervalues    ) {
        this.trace_parametervalues = trace_parametervalues;
    }


    public List<trace_ParameterValue> getTrace_parametervalues() {
        return trace_parametervalues;
    }

    public void addTrace_parametervalue(Trace_parametervalue trace_parametervalue) {
        this.trace_parametervalues.add(trace_parametervalue);
    }
    public trace_Step getTrace_step() {
        return trace_step;
    }

    public void setTrace_step(trace_Step trace_step) {
        this.trace_step = trace_step;
    }

}