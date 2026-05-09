





import java.util.List;
import java.util.ArrayList;

public class library_Tolerance  {

    private String name;
    private String expression;
    private String level;





    private library_Equipment library_equipment;


    public library_Tolerance(
        String name,        String expression,        String level    ) {
        this.name = name;
        this.expression = expression;
        this.level = level;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
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

    public library_Equipment getLibrary_equipment() {
        return library_equipment;
    }

    public void setLibrary_equipment(library_Equipment library_equipment) {
        this.library_equipment = library_equipment;
    }

}