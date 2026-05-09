





import java.util.List;
import java.util.ArrayList;

public class eTJ_Project  {

    private String name;
    private String id;
    private String version;





    private eTJ_Global etj_global;


    public eTJ_Project(
        String name,        String id,        String version    ) {
        this.name = name;
        this.id = id;
        this.version = version;
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
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public eTJ_Global getEtj_global() {
        return etj_global;
    }

    public void setEtj_global(eTJ_Global etj_global) {
        this.etj_global = etj_global;
    }

}