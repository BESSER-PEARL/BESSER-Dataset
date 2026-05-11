





import java.util.List;
import java.util.ArrayList;

public class trace_NameToValueMap  {

    private String key;





    private trace_StructValue trace_structvalue;




    private trace_Value trace_value;


    public trace_NameToValueMap(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public trace_StructValue getTrace_structvalue() {
        return trace_structvalue;
    }

    public void setTrace_structvalue(trace_StructValue trace_structvalue) {
        this.trace_structvalue = trace_structvalue;
    }
    public trace_Value getTrace_value() {
        return trace_value;
    }

    public void setTrace_value(trace_Value trace_value) {
        this.trace_value = trace_value;
    }

}