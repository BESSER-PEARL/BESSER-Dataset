





import java.util.List;
import java.util.ArrayList;

public class metadata_Versions  {

    private String version;





    private metadata_Versioning metadata_versioning;


    public metadata_Versions(
        String version    ) {
        this.version = version;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public metadata_Versioning getMetadata_versioning() {
        return metadata_versioning;
    }

    public void setMetadata_versioning(metadata_Versioning metadata_versioning) {
        this.metadata_versioning = metadata_versioning;
    }

}