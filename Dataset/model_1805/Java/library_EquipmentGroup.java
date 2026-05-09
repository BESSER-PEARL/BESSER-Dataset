





import java.util.List;
import java.util.ArrayList;

public class library_EquipmentGroup extends Base {

    private String description;
    private String count;
    private String name;





    private List<library_NetXResource> library_netxresources;




    private List<library_Parameter> library_parameters;




    private List<library_NetXResource> library_netxresources;


    public library_EquipmentGroup(
        String description,        String count,        String name    ) {
        super(
        );
        this.description = description;
        this.count = count;
        this.name = name;
        this.library_netxresources = new ArrayList<>();
        this.library_parameters = new ArrayList<>();
        this.library_netxresources = new ArrayList<>();
    }

    public library_EquipmentGroup(
        String description,        String count,        String name        ArrayList<library_NetXResource> library_netxresources,        ArrayList<library_Parameter> library_parameters,        ArrayList<library_NetXResource> library_netxresources    ) {
        this.description = description;
        this.count = count;
        this.name = name;
        this.library_netxresources = library_netxresources;
        this.library_parameters = library_parameters;
        this.library_netxresources = library_netxresources;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getCount() {
        return count;
    }

    public void setCount(String count) {
        this.count = count;
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
    public List<library_Parameter> getLibrary_parameters() {
        return library_parameters;
    }

    public void addLibrary_parameter(Library_parameter library_parameter) {
        this.library_parameters.add(library_parameter);
    }
    public List<library_NetXResource> getLibrary_netxresources() {
        return library_netxresources;
    }

    public void addLibrary_netxresource(Library_netxresource library_netxresource) {
        this.library_netxresources.add(library_netxresource);
    }

}