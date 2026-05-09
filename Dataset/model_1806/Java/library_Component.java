





import java.util.List;
import java.util.ArrayList;

public class library_Component extends Base {

    private String name;
    private String duration;
    private String description;





    private List<library_Tolerance> library_tolerances;




    private library_Expression library_expression;




    private library_Expression library_expression;


    public library_Component(
        String name,        String duration,        String description    ) {
        super(
        );
        this.name = name;
        this.duration = duration;
        this.description = description;
        this.library_tolerances = new ArrayList<>();
    }

    public library_Component(
        String name,        String duration,        String description        ArrayList<library_Tolerance> library_tolerances    ) {
        this.name = name;
        this.duration = duration;
        this.description = description;
        this.library_tolerances = library_tolerances;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public List<library_Tolerance> getLibrary_tolerances() {
        return library_tolerances;
    }

    public void addLibrary_tolerance(Library_tolerance library_tolerance) {
        this.library_tolerances.add(library_tolerance);
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

}