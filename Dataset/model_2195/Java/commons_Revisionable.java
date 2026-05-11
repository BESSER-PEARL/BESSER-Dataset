





import java.util.List;
import java.util.ArrayList;

public class commons_Revisionable  {

    private String guid;
    private String revision;



    public commons_Revisionable(
        String guid,        String revision    ) {
        this.guid = guid;
        this.revision = revision;
    }


    public String getGuid() {
        return guid;
    }

    public void setGuid(String guid) {
        this.guid = guid;
    }
    public String getRevision() {
        return revision;
    }

    public void setRevision(String revision) {
        this.revision = revision;
    }


}