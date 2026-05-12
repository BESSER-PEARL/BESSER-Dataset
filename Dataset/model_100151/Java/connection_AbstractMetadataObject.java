





import java.util.List;
import java.util.ArrayList;

public class connection_AbstractMetadataObject  {

    private String id;
    private boolean synchronised;
    private boolean divergency;
    private boolean readOnly;
    private String label;
    private String properties;
    private String comment;



    public connection_AbstractMetadataObject(
        String id,        boolean synchronised,        boolean divergency,        boolean readOnly,        String label,        String properties,        String comment    ) {
        this.id = id;
        this.synchronised = synchronised;
        this.divergency = divergency;
        this.readOnly = readOnly;
        this.label = label;
        this.properties = properties;
        this.comment = comment;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}