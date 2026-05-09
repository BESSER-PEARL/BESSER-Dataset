





import java.util.List;
import java.util.ArrayList;

public class library_Component extends Base {

    private String duration;
    private String name;
    private String description;





    private library_Expression library_expression;




    private library_Expression library_expression;




    private List<library_Tolerance> library_tolerances;




    private List<library_Parameter> library_parameters;


    public library_Component(
        String duration,        String name,        String description    ) {
        super(
        );
        this.duration = duration;
        this.name = name;
        this.description = description;
        this.library_tolerances = new ArrayList<>();
        this.library_parameters = new ArrayList<>();
    }

    public library_Component(
        String duration,        String name,        String description        ArrayList<library_Tolerance> library_tolerances,        ArrayList<library_Parameter> library_parameters    ) {
        this.duration = duration;
        this.name = name;
        this.description = description;
        this.library_tolerances = library_tolerances;
        this.library_parameters = library_parameters;
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

    public library_Expression getLibrary_expression() {
        return library_expression;
    }

    public void setLibrary_expression(library_Expression library_expression) {
        this.library_expression = library_expression;
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
    public List<library_Parameter> getLibrary_parameters() {
        return library_parameters;
    }

    public void addLibrary_parameter(Library_parameter library_parameter) {
        this.library_parameters.add(library_parameter);
    }

}