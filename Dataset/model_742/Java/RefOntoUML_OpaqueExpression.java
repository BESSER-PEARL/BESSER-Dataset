





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_OpaqueExpression extends ValueSpecification {

    private String language;
    private String body;



    public RefOntoUML_OpaqueExpression(
        String language,        String body    ) {
        super(
        );
        this.language = language;
        this.body = body;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }


}