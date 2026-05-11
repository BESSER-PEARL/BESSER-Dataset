





import java.util.List;
import java.util.ArrayList;

public class qm_FindingMessage  {

    private String message;
    private String location;





    private qm_FindingsMeasurementResult qm_findingsmeasurementresult;


    public qm_FindingMessage(
        String message,        String location    ) {
        this.message = message;
        this.location = location;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public qm_FindingsMeasurementResult getQm_findingsmeasurementresult() {
        return qm_findingsmeasurementresult;
    }

    public void setQm_findingsmeasurementresult(qm_FindingsMeasurementResult qm_findingsmeasurementresult) {
        this.qm_findingsmeasurementresult = qm_findingsmeasurementresult;
    }

}