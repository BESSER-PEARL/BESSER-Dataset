





import java.util.List;
import java.util.ArrayList;

public class aml_Witness  {

    private String idRef;
    private String timestamp;
    private String description;



    public aml_Witness(
        String idRef,        String timestamp,        String description    ) {
        this.idRef = idRef;
        this.timestamp = timestamp;
        this.description = description;
    }


    public String getIdref() {
        return idRef;
    }

    public void setIdref(String idRef) {
        this.idRef = idRef;
    }
    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}