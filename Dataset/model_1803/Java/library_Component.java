





import java.util.List;
import java.util.ArrayList;

public class library_Component extends Base {

    private String name;
    private String description;
    private String duration;





    private library_Expression library_expression;




    private library_Expression library_expression;


    public library_Component(
        String name,        String description,        String duration    ) {
        super(
        );
        this.name = name;
        this.description = description;
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
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
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