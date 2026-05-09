





import java.util.List;
import java.util.ArrayList;

public class trace_ETuplePartValue extends EValue {

    private String name;





    private trace_EValue trace_evalue;


    public trace_ETuplePartValue(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public trace_EValue getTrace_evalue() {
        return trace_evalue;
    }

    public void setTrace_evalue(trace_EValue trace_evalue) {
        this.trace_evalue = trace_evalue;
    }

}