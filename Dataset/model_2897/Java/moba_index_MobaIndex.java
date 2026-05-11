





import java.util.List;
import java.util.ArrayList;

public class moba_index_MobaIndex  {

    private String id;
    private String version;
    private String description;
    private String name;



    public moba_index_MobaIndex(
        String id,        String version,        String description,        String name    ) {
        this.id = id;
        this.version = version;
        this.description = description;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}