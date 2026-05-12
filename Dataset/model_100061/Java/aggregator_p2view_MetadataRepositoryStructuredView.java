





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_MetadataRepositoryStructuredView  {

    private String name;
    private String location;
    private boolean loaded;





    private Properties properties;


    public aggregator_p2view_MetadataRepositoryStructuredView(
        String name,        String location,        boolean loaded    ) {
        this.name = name;
        this.location = location;
        this.loaded = loaded;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
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

    public Properties getProperties() {
        return properties;
    }

    public void setProperties(Properties properties) {
        this.properties = properties;
    }

}