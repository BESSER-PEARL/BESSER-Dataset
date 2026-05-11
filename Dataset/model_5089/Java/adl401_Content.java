





import java.util.List;
import java.util.ArrayList;

public class adl401_Content  {

    private String language;
    private String expression;



    public adl401_Content(
        String language,        String expression    ) {
        this.language = language;
        this.expression = expression;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }


}