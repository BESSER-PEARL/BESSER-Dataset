





import java.util.List;
import java.util.ArrayList;

public class library_Expression extends Base {

    private String expressionLines;
    private String name;



    public library_Expression(
        String expressionLines,        String name    ) {
        super(
        );
        this.expressionLines = expressionLines;
        this.name = name;
    }


    public String getExpressionlines() {
        return expressionLines;
    }

    public void setExpressionlines(String expressionLines) {
        this.expressionLines = expressionLines;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}