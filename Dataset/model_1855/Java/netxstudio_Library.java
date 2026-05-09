





import java.util.List;
import java.util.ArrayList;

public class netxstudio_Library  {

    private String description;
    private String version;
    private String name;



    public netxstudio_Library(
        String description,        String version,        String name    ) {
        this.description = description;
        this.version = version;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}