





import java.util.List;
import java.util.ArrayList;

public class library_Tolerance extends Base {

    private String name;
    private String level;





    private library_Expression library_expression;




    private library_Component library_component;


    public library_Tolerance(
        String name,        String level    ) {
        super(
        );
        this.name = name;
        this.level = level;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }

    public library_Expression getLibrary_expression() {
        return library_expression;
    }

    public void setLibrary_expression(library_Expression library_expression) {
        this.library_expression = library_expression;
    }
    public library_Component getLibrary_component() {
        return library_component;
    }

    public void setLibrary_component(library_Component library_component) {
        this.library_component = library_component;
    }

}