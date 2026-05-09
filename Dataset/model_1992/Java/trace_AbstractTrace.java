





import java.util.List;
import java.util.ArrayList;

public class trace_AbstractTrace  {

    private int visualID;
    private boolean processed;



    public trace_AbstractTrace(
        int visualID,        boolean processed    ) {
        this.visualID = visualID;
        this.processed = processed;
    }


    public int getVisualid() {
        return visualID;
    }

    public void setVisualid(int visualID) {
        this.visualID = visualID;
    }
    public boolean getProcessed() {
        return processed;
    }

    public void setProcessed(boolean processed) {
        this.processed = processed;
    }


}