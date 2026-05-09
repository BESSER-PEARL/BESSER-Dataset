





import java.util.List;
import java.util.ArrayList;

public class library_Component extends Base {

    private String duration;
    private String description;
    private String name;





    private List<library_NetXResource> library_netxresources;




    private library_NetXResource library_netxresource;




    private List<library_NetXResource> library_netxresources;


    public library_Component(
        String duration,        String description,        String name    ) {
        super(
        );
        this.duration = duration;
        this.description = description;
        this.name = name;
        this.library_netxresources = new ArrayList<>();
        this.library_netxresources = new ArrayList<>();
    }

    public library_Component(
        String duration,        String description,        String name        ArrayList<library_NetXResource> library_netxresources,        ArrayList<library_NetXResource> library_netxresources    ) {
        this.duration = duration;
        this.description = description;
        this.name = name;
        this.library_netxresources = library_netxresources;
        this.library_netxresources = library_netxresources;
    }

    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<library_NetXResource> getLibrary_netxresources() {
        return library_netxresources;
    }

    public void addLibrary_netxresource(Library_netxresource library_netxresource) {
        this.library_netxresources.add(library_netxresource);
    }
    public library_NetXResource getLibrary_netxresource() {
        return library_netxresource;
    }

    public void setLibrary_netxresource(library_NetXResource library_netxresource) {
        this.library_netxresource = library_netxresource;
    }
    public List<library_NetXResource> getLibrary_netxresources() {
        return library_netxresources;
    }

    public void addLibrary_netxresource(Library_netxresource library_netxresource) {
        this.library_netxresources.add(library_netxresource);
    }

}