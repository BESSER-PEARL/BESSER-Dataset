





import java.util.List;
import java.util.ArrayList;

public class traces_Model  {

    private String uriModel;





    private traces_TraceRecord traces_tracerecord;


    public traces_Model(
        String uriModel    ) {
        this.uriModel = uriModel;
    }


    public String getUrimodel() {
        return uriModel;
    }

    public void setUrimodel(String uriModel) {
        this.uriModel = uriModel;
    }

    public traces_TraceRecord getTraces_tracerecord() {
        return traces_tracerecord;
    }

    public void setTraces_tracerecord(traces_TraceRecord traces_tracerecord) {
        this.traces_tracerecord = traces_tracerecord;
    }

}