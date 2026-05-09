





import java.util.List;
import java.util.ArrayList;

public class library_Component extends Base {

    private String duration;
    private String name;
    private String description;





    private library_NetXResource library_netxresource;




    private List<library_Parameter> library_parameters;




    private List<library_NetXResource> library_netxresources;




    private List<library_NetXResource> library_netxresources;




    private List<library_Tolerance> library_tolerances;




    private List<library_ConfigAttribute> library_configattributes;


    public library_Component(
        String duration,        String name,        String description    ) {
        super(
        );
        this.duration = duration;
        this.name = name;
        this.description = description;
        this.library_parameters = new ArrayList<>();
        this.library_netxresources = new ArrayList<>();
        this.library_netxresources = new ArrayList<>();
        this.library_tolerances = new ArrayList<>();
        this.library_configattributes = new ArrayList<>();
    }

    public library_Component(
        String duration,        String name,        String description        ArrayList<library_Parameter> library_parameters,        ArrayList<library_NetXResource> library_netxresources,        ArrayList<library_NetXResource> library_netxresources,        ArrayList<library_Tolerance> library_tolerances,        ArrayList<library_ConfigAttribute> library_configattributes    ) {
        this.duration = duration;
        this.name = name;
        this.description = description;
        this.library_parameters = library_parameters;
        this.library_netxresources = library_netxresources;
        this.library_netxresources = library_netxresources;
        this.library_tolerances = library_tolerances;
        this.library_configattributes = library_configattributes;
    }

    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public library_NetXResource getLibrary_netxresource() {
        return library_netxresource;
    }

    public void setLibrary_netxresource(library_NetXResource library_netxresource) {
        this.library_netxresource = library_netxresource;
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
    public List<library_NetXResource> getLibrary_netxresources() {
        return library_netxresources;
    }

    public void addLibrary_netxresource(Library_netxresource library_netxresource) {
        this.library_netxresources.add(library_netxresource);
    }
    public List<library_Tolerance> getLibrary_tolerances() {
        return library_tolerances;
    }

    public void addLibrary_tolerance(Library_tolerance library_tolerance) {
        this.library_tolerances.add(library_tolerance);
    }
    public List<library_ConfigAttribute> getLibrary_configattributes() {
        return library_configattributes;
    }

    public void addLibrary_configattribute(Library_configattribute library_configattribute) {
        this.library_configattributes.add(library_configattribute);
    }

}