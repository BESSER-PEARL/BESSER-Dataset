





import java.util.List;
import java.util.ArrayList;

public class uml_UML_OpaqueExpression extends UML_ValueSpecification {

    private String language;
    private String body;





    private uml_UML_Constraint uml_uml_constraint;


    public uml_UML_OpaqueExpression(
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

    public uml_UML_Constraint getUml_uml_constraint() {
        return uml_uml_constraint;
    }

    public void setUml_uml_constraint(uml_UML_Constraint uml_uml_constraint) {
        this.uml_uml_constraint = uml_uml_constraint;
    }

}