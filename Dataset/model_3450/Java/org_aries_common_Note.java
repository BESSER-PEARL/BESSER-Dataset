





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_Note  {

    private String text;
    private String id;
    private String creationDate;
    private String lastUpdate;



    public org_aries_common_Note(
        String text,        String id,        String creationDate,        String lastUpdate    ) {
        this.text = text;
        this.id = id;
        this.creationDate = creationDate;
        this.lastUpdate = lastUpdate;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(String creationDate) {
        this.creationDate = creationDate;
    }
    public String getLastupdate() {
        return lastUpdate;
    }

    public void setLastupdate(String lastUpdate) {
        this.lastUpdate = lastUpdate;
    }


}