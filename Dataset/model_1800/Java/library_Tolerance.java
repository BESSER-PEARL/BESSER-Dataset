





import java.util.List;
import java.util.ArrayList;

public class library_Tolerance  {

    private String expression;
    private String level;
    private String name;





    private library_Equipment library_equipment;


    public library_Tolerance(
        String expression,        String level,        String name    ) {
        this.expression = expression;
        this.level = level;
        this.name = name;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public library_Equipment getLibrary_equipment() {
        return library_equipment;
    }

    public void setLibrary_equipment(library_Equipment library_equipment) {
        this.library_equipment = library_equipment;
    }

}