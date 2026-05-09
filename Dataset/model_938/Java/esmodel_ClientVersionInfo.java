





import java.util.List;
import java.util.ArrayList;

public class esmodel_ClientVersionInfo  {

    private String version;
    private String name;



    public esmodel_ClientVersionInfo(
        String version,        String name    ) {
        this.version = version;
        this.name = name;
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