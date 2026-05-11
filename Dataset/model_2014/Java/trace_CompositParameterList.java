





import java.util.List;
import java.util.ArrayList;

public class trace_CompositParameterList extends ParameterList {

    private int paramtervaluesOrder;





    private List<trace_ParameterList> trace_parameterlists;


    public trace_CompositParameterList(
        int paramtervaluesOrder    ) {
        super(
        );
        this.paramtervaluesOrder = paramtervaluesOrder;
        this.trace_parameterlists = new ArrayList<>();
    }

    public trace_CompositParameterList(
        int paramtervaluesOrder        ArrayList<trace_ParameterList> trace_parameterlists    ) {
        this.paramtervaluesOrder = paramtervaluesOrder;
        this.trace_parameterlists = trace_parameterlists;
    }

    public int getParamtervaluesorder() {
        return paramtervaluesOrder;
    }

    public void setParamtervaluesorder(int paramtervaluesOrder) {
        this.paramtervaluesOrder = paramtervaluesOrder;
    }

    public List<trace_ParameterList> getTrace_parameterlists() {
        return trace_parameterlists;
    }

    public void addTrace_parameterlist(Trace_parameterlist trace_parameterlist) {
        this.trace_parameterlists.add(trace_parameterlist);
    }

}