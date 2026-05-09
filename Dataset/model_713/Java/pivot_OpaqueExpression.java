





import java.util.List;
import java.util.ArrayList;

public class pivot_OpaqueExpression extends ValueSpecification {

    private String language;
    private String body;





    private pivot_ExpressionInOCL pivot_expressioninocl;


    public pivot_OpaqueExpression(
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

    public pivot_ExpressionInOCL getPivot_expressioninocl() {
        return pivot_expressioninocl;
    }

    public void setPivot_expressioninocl(pivot_ExpressionInOCL pivot_expressioninocl) {
        this.pivot_expressioninocl = pivot_expressioninocl;
    }

}