





import java.util.List;
import java.util.ArrayList;

public class iot2_ActivityNode extends NamedElement {

    private String running;





    private iot2_Token iot2_token;




    private iot2_Trace iot2_trace;


    public iot2_ActivityNode(
        String running    ) {
        super(
        );
        this.running = running;
    }


    public String getRunning() {
        return running;
    }

    public void setRunning(String running) {
        this.running = running;
    }

    public iot2_Token getIot2_token() {
        return iot2_token;
    }

    public void setIot2_token(iot2_Token iot2_token) {
        this.iot2_token = iot2_token;
    }
    public iot2_Trace getIot2_trace() {
        return iot2_trace;
    }

    public void setIot2_trace(iot2_Trace iot2_trace) {
        this.iot2_trace = iot2_trace;
    }

}