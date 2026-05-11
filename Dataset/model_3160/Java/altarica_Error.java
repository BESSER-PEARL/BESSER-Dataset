





import java.util.List;
import java.util.ArrayList;

public class altarica_Error  {

    private String message;
    private String severity;





    private altarica_Model altarica_model;


    public altarica_Error(
        String message,        String severity    ) {
        this.message = message;
        this.severity = severity;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }

    public altarica_Model getAltarica_model() {
        return altarica_model;
    }

    public void setAltarica_model(altarica_Model altarica_model) {
        this.altarica_model = altarica_model;
    }

}