





import java.util.List;
import java.util.ArrayList;

public class traces_A extends RootIn {

    private String name;





    private traces_R1_Trace traces_r1_trace;


    public traces_A(
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

    public traces_R1_Trace getTraces_r1_trace() {
        return traces_r1_trace;
    }

    public void setTraces_r1_trace(traces_R1_Trace traces_r1_trace) {
        this.traces_r1_trace = traces_r1_trace;
    }

}