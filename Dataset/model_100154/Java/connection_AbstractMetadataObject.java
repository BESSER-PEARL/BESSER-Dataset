





import java.util.List;
import java.util.ArrayList;

public class connection_AbstractMetadataObject extends ModelElement {

    private String id;
    private boolean divergency;
    private boolean synchronised;
    private String label;
    private boolean readOnly;
    private String comment;
    private String properties;



    public connection_AbstractMetadataObject(
        String id,        boolean divergency,        boolean synchronised,        String label,        boolean readOnly,        String comment,        String properties    ) {
        super(
        );
        this.id = id;
        this.divergency = divergency;
        this.synchronised = synchronised;
        this.label = label;
        this.readOnly = readOnly;
        this.comment = comment;
        this.properties = properties;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getDivergency() {
        return divergency;
    }

    public void setDivergency(boolean divergency) {
        this.divergency = divergency;
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
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }


}