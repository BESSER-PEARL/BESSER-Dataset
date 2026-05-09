





import java.util.List;
import java.util.ArrayList;

public class uml_OpaqueExpression extends ValueSpecification {

    private String language;
    private String body;





    private uml_Abstraction uml_abstraction;


    public uml_OpaqueExpression(
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

    public uml_Abstraction getUml_abstraction() {
        return uml_abstraction;
    }

    public void setUml_abstraction(uml_Abstraction uml_abstraction) {
        this.uml_abstraction = uml_abstraction;
    }

}