





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_MetadataRepositoryStructuredView  {

    private String name;
    private boolean loaded;





    private Properties properties;




    private InstallableUnits installableunits;




    private MetadataRepository metadatarepository;


    public aggregator_p2view_MetadataRepositoryStructuredView(
        String name,        boolean loaded    ) {
        this.name = name;
        this.loaded = loaded;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getLoaded() {
        return loaded;
    }

    public void setLoaded(boolean loaded) {
        this.loaded = loaded;
    }

    public Properties getProperties() {
        return properties;
    }

    public void setProperties(Properties properties) {
        this.properties = properties;
    }
    public InstallableUnits getInstallableunits() {
        return installableunits;
    }

    public void setInstallableunits(InstallableUnits installableunits) {
        this.installableunits = installableunits;
    }
    public MetadataRepository getMetadatarepository() {
        return metadatarepository;
    }

    public void setMetadatarepository(MetadataRepository metadatarepository) {
        this.metadatarepository = metadatarepository;
    }

}