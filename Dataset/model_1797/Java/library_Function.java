





import java.util.List;
import java.util.ArrayList;

public class library_Function  {

    private String description;
    private String functionName;





    private List<library_Parameter> library_parameters;




    private List<library_NetXResource> library_netxresources;




    private List<library_Expression> library_expressions;




    private library_Function library_function;




    private library_Expression library_expression;




    private List<library_DiagramInfo> library_diagraminfos;




    private List<library_Protocol> library_protocols;




    private List<library_Metric> library_metrics;




    private library_MultiImage library_multiimage;




    private List<library_NetXResource> library_netxresources;




    private List<library_Function> library_functions;




    private library_Expression library_expression;




    private List<library_Tolerance> library_tolerances;


    public library_Function(
        String description,        String functionName    ) {
        this.description = description;
        this.functionName = functionName;
        this.library_parameters = new ArrayList<>();
        this.library_netxresources = new ArrayList<>();
        this.library_expressions = new ArrayList<>();
        this.library_diagraminfos = new ArrayList<>();
        this.library_protocols = new ArrayList<>();
        this.library_metrics = new ArrayList<>();
        this.library_netxresources = new ArrayList<>();
        this.library_functions = new ArrayList<>();
        this.library_tolerances = new ArrayList<>();
    }

    public library_Function(
        String description,        String functionName        ArrayList<library_Parameter> library_parameters,        ArrayList<library_NetXResource> library_netxresources,        ArrayList<library_Expression> library_expressions,        ArrayList<library_DiagramInfo> library_diagraminfos,        ArrayList<library_Protocol> library_protocols,        ArrayList<library_Metric> library_metrics,        ArrayList<library_NetXResource> library_netxresources,        ArrayList<library_Function> library_functions,        ArrayList<library_Tolerance> library_tolerances    ) {
        this.description = description;
        this.functionName = functionName;
        this.library_parameters = library_parameters;
        this.library_netxresources = library_netxresources;
        this.library_expressions = library_expressions;
        this.library_diagraminfos = library_diagraminfos;
        this.library_protocols = library_protocols;
        this.library_metrics = library_metrics;
        this.library_netxresources = library_netxresources;
        this.library_functions = library_functions;
        this.library_tolerances = library_tolerances;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getFunctionname() {
        return functionName;
    }

    public void setFunctionname(String functionName) {
        this.functionName = functionName;
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
    public List<library_Expression> getLibrary_expressions() {
        return library_expressions;
    }

    public void addLibrary_expression(Library_expression library_expression) {
        this.library_expressions.add(library_expression);
    }
    public library_Function getLibrary_function() {
        return library_function;
    }

    public void setLibrary_function(library_Function library_function) {
        this.library_function = library_function;
    }
    public library_Expression getLibrary_expression() {
        return library_expression;
    }

    public void setLibrary_expression(library_Expression library_expression) {
        this.library_expression = library_expression;
    }
    public List<library_DiagramInfo> getLibrary_diagraminfos() {
        return library_diagraminfos;
    }

    public void addLibrary_diagraminfo(Library_diagraminfo library_diagraminfo) {
        this.library_diagraminfos.add(library_diagraminfo);
    }
    public List<library_Protocol> getLibrary_protocols() {
        return library_protocols;
    }

    public void addLibrary_protocol(Library_protocol library_protocol) {
        this.library_protocols.add(library_protocol);
    }
    public List<library_Metric> getLibrary_metrics() {
        return library_metrics;
    }

    public void addLibrary_metric(Library_metric library_metric) {
        this.library_metrics.add(library_metric);
    }
    public library_MultiImage getLibrary_multiimage() {
        return library_multiimage;
    }

    public void setLibrary_multiimage(library_MultiImage library_multiimage) {
        this.library_multiimage = library_multiimage;
    }
    public List<library_NetXResource> getLibrary_netxresources() {
        return library_netxresources;
    }

    public void addLibrary_netxresource(Library_netxresource library_netxresource) {
        this.library_netxresources.add(library_netxresource);
    }
    public List<library_Function> getLibrary_functions() {
        return library_functions;
    }

    public void addLibrary_function(Library_function library_function) {
        this.library_functions.add(library_function);
    }
    public library_Expression getLibrary_expression() {
        return library_expression;
    }

    public void setLibrary_expression(library_Expression library_expression) {
        this.library_expression = library_expression;
    }
    public List<library_Tolerance> getLibrary_tolerances() {
        return library_tolerances;
    }

    public void addLibrary_tolerance(Library_tolerance library_tolerance) {
        this.library_tolerances.add(library_tolerance);
    }

}