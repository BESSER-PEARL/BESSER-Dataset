





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_MetadataRepositoryStructuredView  {

    private boolean loaded;
    private String location;
    private String name;



    public aggregator_p2view_MetadataRepositoryStructuredView(
        boolean loaded,        String location,        String name    ) {
        this.loaded = loaded;
        this.location = location;
        this.name = name;
    }


    public boolean getLoaded() {
        return loaded;
    }

    public void setLoaded(boolean loaded) {
        this.loaded = loaded;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}