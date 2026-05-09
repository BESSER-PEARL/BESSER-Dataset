





import java.util.List;
import java.util.ArrayList;

public class fUML_BasicBehaviors_OpaqueBehavior extends Behavior {

    private String language;
    private String body;



    public fUML_BasicBehaviors_OpaqueBehavior(
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