





import java.util.List;
import java.util.ArrayList;

public class build_InstallationUnit  {

    private String id;
    private String version;





    private build_Repository build_repository;


    public build_InstallationUnit(
        String id,        String version    ) {
        this.id = id;
        this.version = version;
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

    public build_Repository getBuild_repository() {
        return build_repository;
    }

    public void setBuild_repository(build_Repository build_repository) {
        this.build_repository = build_repository;
    }

}