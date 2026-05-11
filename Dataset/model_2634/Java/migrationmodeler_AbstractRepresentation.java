





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_AbstractRepresentation  {

    private boolean hidden;
    private String mappingId;
    private boolean pinned;
    private boolean displayed;



    public migrationmodeler_AbstractRepresentation(
        boolean hidden,        String mappingId,        boolean pinned,        boolean displayed    ) {
        this.hidden = hidden;
        this.mappingId = mappingId;
        this.pinned = pinned;
        this.displayed = displayed;
    }


    public boolean getHidden() {
        return hidden;
    }

    public void setHidden(boolean hidden) {
        this.hidden = hidden;
    }
    public String getMappingid() {
        return mappingId;
    }

    public void setMappingid(String mappingId) {
        this.mappingId = mappingId;
    }
    public boolean getPinned() {
        return pinned;
    }

    public void setPinned(boolean pinned) {
        this.pinned = pinned;
    }
    public boolean getDisplayed() {
        return displayed;
    }

    public void setDisplayed(boolean displayed) {
        this.displayed = displayed;
    }


}