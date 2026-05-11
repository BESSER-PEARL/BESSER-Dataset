





import java.util.List;
import java.util.ArrayList;

public class r1_CodeSystemDef extends Element {

    private String version;
    private String id;
    private String name;
    private String accessLevel;



    public r1_CodeSystemDef(
        String version,        String id,        String name,        String accessLevel    ) {
        super(
        );
        this.version = version;
        this.id = id;
        this.name = name;
        this.accessLevel = accessLevel;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccesslevel() {
        return accessLevel;
    }

    public void setAccesslevel(String accessLevel) {
        this.accessLevel = accessLevel;
    }


}