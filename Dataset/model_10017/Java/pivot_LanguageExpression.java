





import java.util.List;
import java.util.ArrayList;

public class pivot_LanguageExpression extends ValueSpecification {

    private String body;
    private String language;





    private pivot_Operation pivot_operation;


    public pivot_LanguageExpression(
        String body,        String language    ) {
        super(
        );
        this.body = body;
        this.language = language;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }

}