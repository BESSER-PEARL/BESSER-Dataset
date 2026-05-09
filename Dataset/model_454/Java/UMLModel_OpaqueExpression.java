





import java.util.List;
import java.util.ArrayList;

public class UMLModel_OpaqueExpression extends ValueSpecification {

    private String result;
    private String language;
    private String body;
    private String behavior;



    public UMLModel_OpaqueExpression(
        String result,        String language,        String body,        String behavior    ) {
        super(
        );
        this.result = result;
        this.language = language;
        this.body = body;
        this.behavior = behavior;
    }


    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
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
    public String getBehavior() {
        return behavior;
    }

    public void setBehavior(String behavior) {
        this.behavior = behavior;
    }


}