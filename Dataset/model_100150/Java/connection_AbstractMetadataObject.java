





import java.util.List;
import java.util.ArrayList;

public class connection_AbstractMetadataObject  {

    private boolean synchronised;
    private boolean divergency;
    private String label;
    private String id;
    private String properties;
    private boolean readOnly;
    private String comment;



    public connection_AbstractMetadataObject(
        boolean synchronised,        boolean divergency,        String label,        String id,        String properties,        boolean readOnly,        String comment    ) {
        this.synchronised = synchronised;
        this.divergency = divergency;
        this.label = label;
        this.id = id;
        this.properties = properties;
        this.readOnly = readOnly;
        this.comment = comment;
    }


    public boolean getSynchronised() {
        return synchronised;
    }

    public void setSynchronised(boolean synchronised) {
        this.synchronised = synchronised;
    }
    public boolean getDivergency() {
        return divergency;
    }

    public void setDivergency(boolean divergency) {
        this.divergency = divergency;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }
    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}