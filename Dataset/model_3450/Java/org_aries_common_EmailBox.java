





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_EmailBox  {

    private String type;
    private String id;
    private String lastUpdate;
    private String creationDate;
    private String name;



    public org_aries_common_EmailBox(
        String type,        String id,        String lastUpdate,        String creationDate,        String name    ) {
        this.type = type;
        this.id = id;
        this.lastUpdate = lastUpdate;
        this.creationDate = creationDate;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLastupdate() {
        return lastUpdate;
    }

    public void setLastupdate(String lastUpdate) {
        this.lastUpdate = lastUpdate;
    }
    public String getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(String creationDate) {
        this.creationDate = creationDate;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}