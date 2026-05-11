





import java.util.List;
import java.util.ArrayList;

public class qm_FindingMessage  {

    private String location;
    private String message;





    private qm_FindingsMeasurementResult qm_findingsmeasurementresult;


    public qm_FindingMessage(
        String location,        String message    ) {
        this.location = location;
        this.message = message;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public qm_FindingsMeasurementResult getQm_findingsmeasurementresult() {
        return qm_findingsmeasurementresult;
    }

    public void setQm_findingsmeasurementresult(qm_FindingsMeasurementResult qm_findingsmeasurementresult) {
        this.qm_findingsmeasurementresult = qm_findingsmeasurementresult;
    }

}