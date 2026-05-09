





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_OpaqueExpression extends ValueSpecification {

    private String body;
    private String language;





    private CompleteDSLPckg_Parameter completedslpckg_parameter;


    public CompleteDSLPckg_OpaqueExpression(
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

    public CompleteDSLPckg_Parameter getCompletedslpckg_parameter() {
        return completedslpckg_parameter;
    }

    public void setCompletedslpckg_parameter(CompleteDSLPckg_Parameter completedslpckg_parameter) {
        this.completedslpckg_parameter = completedslpckg_parameter;
    }

}