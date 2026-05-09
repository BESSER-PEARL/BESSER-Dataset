





import java.util.List;
import java.util.ArrayList;

public class RefUML_OpaqueExpression extends ValueSpecification {

    private String body;
    private String language;



    public RefUML_OpaqueExpression(
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


}