





import java.util.List;
import java.util.ArrayList;

public class library_Expression extends Base {

    private String name;
    private String expressionLines;





    private library_Tolerance library_tolerance;


    public library_Expression(
        String name,        String expressionLines    ) {
        super(
        );
        this.name = name;
        this.expressionLines = expressionLines;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getExpressionlines() {
        return expressionLines;
    }

    public void setExpressionlines(String expressionLines) {
        this.expressionLines = expressionLines;
    }

    public library_Tolerance getLibrary_tolerance() {
        return library_tolerance;
    }

    public void setLibrary_tolerance(library_Tolerance library_tolerance) {
        this.library_tolerance = library_tolerance;
    }

}