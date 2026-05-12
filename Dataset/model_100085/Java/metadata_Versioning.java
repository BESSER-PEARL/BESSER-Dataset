





import java.util.List;
import java.util.ArrayList;

public class metadata_Versioning  {

    private String lastUpdated;
    private String release;
    private String latest;





    private metadata_MetaData metadata_metadata;


    public metadata_Versioning(
        String lastUpdated,        String release,        String latest    ) {
        this.lastUpdated = lastUpdated;
        this.release = release;
        this.latest = latest;
    }


    public String getLastupdated() {
        return lastUpdated;
    }

    public void setLastupdated(String lastUpdated) {
        this.lastUpdated = lastUpdated;
    }
    public String getRelease() {
        return release;
    }

    public void setRelease(String release) {
        this.release = release;
    }
    public String getLatest() {
        return latest;
    }

    public void setLatest(String latest) {
        this.latest = latest;
    }

    public metadata_MetaData getMetadata_metadata() {
        return metadata_metadata;
    }

    public void setMetadata_metadata(metadata_MetaData metadata_metadata) {
        this.metadata_metadata = metadata_metadata;
    }

}