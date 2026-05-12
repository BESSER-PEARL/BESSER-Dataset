





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_MetadataRepositoryStructuredView  {

    private boolean loaded;
    private String name;





    private MetadataRepository metadatarepository;


    public aggregator_p2view_MetadataRepositoryStructuredView(
        boolean loaded,        String name    ) {
        this.loaded = loaded;
        this.name = name;
    }


    public boolean getLoaded() {
        return loaded;
    }

    public void setLoaded(boolean loaded) {
        this.loaded = loaded;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MetadataRepository getMetadatarepository() {
        return metadatarepository;
    }

    public void setMetadatarepository(MetadataRepository metadatarepository) {
        this.metadatarepository = metadatarepository;
    }

}