





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Note  {

    private String severity;
    private String version;
    private String value;



    public eaglemodel_Note(
        String severity,        String version,        String value    ) {
        this.severity = severity;
        this.version = version;
        this.value = value;
    }


    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}