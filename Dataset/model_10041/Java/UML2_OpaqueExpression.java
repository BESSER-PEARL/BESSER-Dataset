





import java.util.List;
import java.util.ArrayList;

public class UML2_OpaqueExpression extends ValueSpecification {

    private String bodies;
    private String language;





    private UML2_Lifeline uml2_lifeline;


    public UML2_OpaqueExpression(
        String bodies,        String language    ) {
        super(
        );
        this.bodies = bodies;
        this.language = language;
    }


    public String getBodies() {
        return bodies;
    }

    public void setBodies(String bodies) {
        this.bodies = bodies;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public UML2_Lifeline getUml2_lifeline() {
        return uml2_lifeline;
    }

    public void setUml2_lifeline(UML2_Lifeline uml2_lifeline) {
        this.uml2_lifeline = uml2_lifeline;
    }

}