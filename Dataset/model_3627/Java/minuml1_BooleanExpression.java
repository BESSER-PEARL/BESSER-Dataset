





import java.util.List;
import java.util.ArrayList;

public class minuml1_BooleanExpression  {

    private String body;
    private String language;





    private minuml1_Guard minuml1_guard;


    public minuml1_BooleanExpression(
        String body,        String language    ) {
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

    public minuml1_Guard getMinuml1_guard() {
        return minuml1_guard;
    }

    public void setMinuml1_guard(minuml1_Guard minuml1_guard) {
        this.minuml1_guard = minuml1_guard;
    }

}