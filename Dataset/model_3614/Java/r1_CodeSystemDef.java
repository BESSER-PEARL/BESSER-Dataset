





import java.util.List;
import java.util.ArrayList;

public class r1_CodeSystemDef extends Element {

    private String version;
    private String accessLevel;
    private String name;
    private String id;



    public r1_CodeSystemDef(
        String version,        String accessLevel,        String name,        String id    ) {
        super(
        );
        this.version = version;
        this.accessLevel = accessLevel;
        this.name = name;
        this.id = id;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getAccesslevel() {
        return accessLevel;
    }

    public void setAccesslevel(String accessLevel) {
        this.accessLevel = accessLevel;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}