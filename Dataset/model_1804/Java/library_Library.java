





import java.util.List;
import java.util.ArrayList;

public class library_Library  {

    private String name;
    private String protocols;





    private List<library_NodeType> library_nodetypes;




    private List<library_Unit> library_units;




    private List<library_Tolerance> library_tolerances;




    private List<library_Parameter> library_parameters;




    private List<library_Function> library_functions;




    private List<library_Metric> library_metrics;




    private List<library_Expression> library_expressions;




    private List<library_Equipment> library_equipments;


    public library_Library(
        String name,        String protocols    ) {
        this.name = name;
        this.protocols = protocols;
        this.library_nodetypes = new ArrayList<>();
        this.library_units = new ArrayList<>();
        this.library_tolerances = new ArrayList<>();
        this.library_parameters = new ArrayList<>();
        this.library_functions = new ArrayList<>();
        this.library_metrics = new ArrayList<>();
        this.library_expressions = new ArrayList<>();
        this.library_equipments = new ArrayList<>();
    }

    public library_Library(
        String name,        String protocols        ArrayList<library_NodeType> library_nodetypes,        ArrayList<library_Unit> library_units,        ArrayList<library_Tolerance> library_tolerances,        ArrayList<library_Parameter> library_parameters,        ArrayList<library_Function> library_functions,        ArrayList<library_Metric> library_metrics,        ArrayList<library_Expression> library_expressions,        ArrayList<library_Equipment> library_equipments    ) {
        this.name = name;
        this.protocols = protocols;
        this.library_nodetypes = library_nodetypes;
        this.library_units = library_units;
        this.library_tolerances = library_tolerances;
        this.library_parameters = library_parameters;
        this.library_functions = library_functions;
        this.library_metrics = library_metrics;
        this.library_expressions = library_expressions;
        this.library_equipments = library_equipments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getProtocols() {
        return protocols;
    }

    public void setProtocols(String protocols) {
        this.protocols = protocols;
    }

    public List<library_NodeType> getLibrary_nodetypes() {
        return library_nodetypes;
    }

    public void addLibrary_nodetype(Library_nodetype library_nodetype) {
        this.library_nodetypes.add(library_nodetype);
    }
    public List<library_Unit> getLibrary_units() {
        return library_units;
    }

    public void addLibrary_unit(Library_unit library_unit) {
        this.library_units.add(library_unit);
    }
    public List<library_Tolerance> getLibrary_tolerances() {
        return library_tolerances;
    }

    public void addLibrary_tolerance(Library_tolerance library_tolerance) {
        this.library_tolerances.add(library_tolerance);
    }
    public List<library_Parameter> getLibrary_parameters() {
        return library_parameters;
    }

    public void addLibrary_parameter(Library_parameter library_parameter) {
        this.library_parameters.add(library_parameter);
    }
    public List<library_Function> getLibrary_functions() {
        return library_functions;
    }

    public void addLibrary_function(Library_function library_function) {
        this.library_functions.add(library_function);
    }
    public List<library_Metric> getLibrary_metrics() {
        return library_metrics;
    }

    public void addLibrary_metric(Library_metric library_metric) {
        this.library_metrics.add(library_metric);
    }
    public List<library_Expression> getLibrary_expressions() {
        return library_expressions;
    }

    public void addLibrary_expression(Library_expression library_expression) {
        this.library_expressions.add(library_expression);
    }
    public List<library_Equipment> getLibrary_equipments() {
        return library_equipments;
    }

    public void addLibrary_equipment(Library_equipment library_equipment) {
        this.library_equipments.add(library_equipment);
    }

}