





import java.util.List;
import java.util.ArrayList;

public class trace_Value  {

    private String type;





    private trace_ArrayValue trace_arrayvalue;


    public trace_Value(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public trace_ArrayValue getTrace_arrayvalue() {
        return trace_arrayvalue;
    }

    public void setTrace_arrayvalue(trace_ArrayValue trace_arrayvalue) {
        this.trace_arrayvalue = trace_arrayvalue;
    }

}