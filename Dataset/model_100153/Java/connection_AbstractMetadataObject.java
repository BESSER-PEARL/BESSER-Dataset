





import java.util.List;
import java.util.ArrayList;

public class connection_AbstractMetadataObject  {

    private String properties;
    private String label;
    private String comment;
    private boolean synchronised;
    private String id;
    private boolean readOnly;
    private boolean divergency;



    public connection_AbstractMetadataObject(
        String properties,        String label,        String comment,        boolean synchronised,        String id,        boolean readOnly,        boolean divergency    ) {
        this.properties = properties;
        this.label = label;
        this.comment = comment;
        this.synchronised = synchronised;
        this.id = id;
        this.readOnly = readOnly;
        this.divergency = divergency;
    }


    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public boolean getSynchronised() {
        return synchronised;
    }

    public void setSynchronised(boolean synchronised) {
        this.synchronised = synchronised;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }
    public boolean getDivergency() {
        return divergency;
    }

    public void setDivergency(boolean divergency) {
        this.divergency = divergency;
    }


}