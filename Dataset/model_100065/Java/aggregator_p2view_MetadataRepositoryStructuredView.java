





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_MetadataRepositoryStructuredView  {

    private String location;
    private boolean loaded;
    private String name;





    private p2view_aggregator_MetadataRepository p2view_aggregator_metadatarepository;




    private Properties properties;




    private RepositoryReferences repositoryreferences;


    public aggregator_p2view_MetadataRepositoryStructuredView(
        String location,        boolean loaded,        String name    ) {
        this.location = location;
        this.loaded = loaded;
        this.name = name;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
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

    public p2view_aggregator_MetadataRepository getP2view_aggregator_metadatarepository() {
        return p2view_aggregator_metadatarepository;
    }

    public void setP2view_aggregator_metadatarepository(p2view_aggregator_MetadataRepository p2view_aggregator_metadatarepository) {
        this.p2view_aggregator_metadatarepository = p2view_aggregator_metadatarepository;
    }
    public Properties getProperties() {
        return properties;
    }

    public void setProperties(Properties properties) {
        this.properties = properties;
    }
    public RepositoryReferences getRepositoryreferences() {
        return repositoryreferences;
    }

    public void setRepositoryreferences(RepositoryReferences repositoryreferences) {
        this.repositoryreferences = repositoryreferences;
    }

}