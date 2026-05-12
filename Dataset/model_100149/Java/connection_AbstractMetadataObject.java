





import java.util.List;
import java.util.ArrayList;

public class connection_AbstractMetadataObject extends ModelElement {

    private boolean readOnly;
    private boolean synchronised;
    private String label;
    private String properties;
    private boolean divergency;
    private String id;
    private String comment;



    public connection_AbstractMetadataObject(
        boolean readOnly,        boolean synchronised,        String label,        String properties,        boolean divergency,        String id,        String comment    ) {
        super(
        );
        this.readOnly = readOnly;
        this.synchronised = synchronised;
        this.label = label;
        this.properties = properties;
        this.divergency = divergency;
        this.id = id;
        this.comment = comment;
    }


    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }
    public boolean getSynchronised() {
        return synchronised;
    }

    public void setSynchronised(boolean synchronised) {
        this.synchronised = synchronised;
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
    public boolean getDivergency() {
        return divergency;
    }

    public void setDivergency(boolean divergency) {
        this.divergency = divergency;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}