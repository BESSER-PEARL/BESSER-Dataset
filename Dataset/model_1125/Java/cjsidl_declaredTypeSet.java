





import java.util.List;
import java.util.ArrayList;

public class cjsidl_declaredTypeSet  {

    private String typeName;
    private String version;
    private String name;



    public cjsidl_declaredTypeSet(
        String typeName,        String version,        String name    ) {
        this.typeName = typeName;
        this.version = version;
        this.name = name;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
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