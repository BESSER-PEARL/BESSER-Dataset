





import java.util.List;
import java.util.ArrayList;

public class traces_E extends RootOut {

    private String name;





    private traces_D traces_d;




    private traces_R2_Trace traces_r2_trace;




    private traces_D traces_d;


    public traces_E(
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

    public traces_D getTraces_d() {
        return traces_d;
    }

    public void setTraces_d(traces_D traces_d) {
        this.traces_d = traces_d;
    }
    public traces_R2_Trace getTraces_r2_trace() {
        return traces_r2_trace;
    }

    public void setTraces_r2_trace(traces_R2_Trace traces_r2_trace) {
        this.traces_r2_trace = traces_r2_trace;
    }
    public traces_D getTraces_d() {
        return traces_d;
    }

    public void setTraces_d(traces_D traces_d) {
        this.traces_d = traces_d;
    }

}