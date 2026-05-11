





import java.util.List;
import java.util.ArrayList;

public class minuml2_OpaqueExpression  {

    private String body;
    private String language;





    private minuml2_ActivityEdge minuml2_activityedge;


    public minuml2_OpaqueExpression(
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

    public minuml2_ActivityEdge getMinuml2_activityedge() {
        return minuml2_activityedge;
    }

    public void setMinuml2_activityedge(minuml2_ActivityEdge minuml2_activityedge) {
        this.minuml2_activityedge = minuml2_activityedge;
    }

}