





import java.util.List;
import java.util.ArrayList;

public class connection_AbstractMetadataObject extends ModelElement {

    private boolean readOnly;
    private String id;
    private boolean synchronised;
    private String properties;
    private String comment;
    private String label;
    private boolean divergency;



    public connection_AbstractMetadataObject(
        boolean readOnly,        String id,        boolean synchronised,        String properties,        String comment,        String label,        boolean divergency    ) {
        super(
        );
        this.readOnly = readOnly;
        this.id = id;
        this.synchronised = synchronised;
        this.properties = properties;
        this.comment = comment;
        this.label = label;
        this.divergency = divergency;
    }


    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
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
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public boolean getDivergency() {
        return divergency;
    }

    public void setDivergency(boolean divergency) {
        this.divergency = divergency;
    }


}