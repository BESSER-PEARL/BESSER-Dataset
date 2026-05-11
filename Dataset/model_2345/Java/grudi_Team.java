





import java.util.List;
import java.util.ArrayList;

public class grudi_Team  {

    private String name;
    private String versionNumber;
    private String id;



    public grudi_Team(
        String name,        String versionNumber,        String id    ) {
        this.name = name;
        this.versionNumber = versionNumber;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersionnumber() {
        return versionNumber;
    }

    public void setVersionnumber(String versionNumber) {
        this.versionNumber = versionNumber;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}