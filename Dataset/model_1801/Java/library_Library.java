





import java.util.List;
import java.util.ArrayList;

public class library_Library  {

    private String protocols;
    private String name;





    private List<library_Tolerance> library_tolerances;




    private List<library_MetricSource> library_metricsources;




    private List<library_Equipment> library_equipments;




    private List<library_NodeType> library_nodetypes;




    private List<library_Function> library_functions;




    private List<library_Parameter> library_parameters;


    public library_Library(
        String protocols,        String name    ) {
        this.protocols = protocols;
        this.name = name;
        this.library_tolerances = new ArrayList<>();
        this.library_metricsources = new ArrayList<>();
        this.library_equipments = new ArrayList<>();
        this.library_nodetypes = new ArrayList<>();
        this.library_functions = new ArrayList<>();
        this.library_parameters = new ArrayList<>();
    }

    public library_Library(
        String protocols,        String name        ArrayList<library_Tolerance> library_tolerances,        ArrayList<library_MetricSource> library_metricsources,        ArrayList<library_Equipment> library_equipments,        ArrayList<library_NodeType> library_nodetypes,        ArrayList<library_Function> library_functions,        ArrayList<library_Parameter> library_parameters    ) {
        this.protocols = protocols;
        this.name = name;
        this.library_tolerances = library_tolerances;
        this.library_metricsources = library_metricsources;
        this.library_equipments = library_equipments;
        this.library_nodetypes = library_nodetypes;
        this.library_functions = library_functions;
        this.library_parameters = library_parameters;
    }

    public String getProtocols() {
        return protocols;
    }

    public void setProtocols(String protocols) {
        this.protocols = protocols;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<library_Tolerance> getLibrary_tolerances() {
        return library_tolerances;
    }

    public void addLibrary_tolerance(Library_tolerance library_tolerance) {
        this.library_tolerances.add(library_tolerance);
    }
    public List<library_MetricSource> getLibrary_metricsources() {
        return library_metricsources;
    }

    public void addLibrary_metricsource(Library_metricsource library_metricsource) {
        this.library_metricsources.add(library_metricsource);
    }
    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
    }
    public List<library_NodeType> getLibrary_nodetypes() {
        return library_nodetypes;
    }

    public void addLibrary_nodetype(Library_nodetype library_nodetype) {
        this.library_nodetypes.add(library_nodetype);
    }
    public List<library_Function> getLibrary_functions() {
        return library_functions;
    }

    public void addLibrary_function(Library_function library_function) {
        this.library_functions.add(library_function);
    }
    public List<library_Parameter> getLibrary_parameters() {
        return library_parameters;
    }

    public void addLibrary_parameter(Library_parameter library_parameter) {
        this.library_parameters.add(library_parameter);
    }

}