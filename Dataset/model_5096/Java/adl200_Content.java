





import java.util.List;
import java.util.ArrayList;

public class adl200_Content  {

    private String expression;
    private String language;



    public adl200_Content(
        String expression,        String language    ) {
        this.expression = expression;
        this.language = language;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }


}