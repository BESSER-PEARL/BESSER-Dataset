





import java.util.List;
import java.util.ArrayList;

public class UML2_OpaqueExpression extends ValueSpecification {

    private String language;
    private String bodies;





    private UML2_Behavior uml2_behavior;


    public UML2_OpaqueExpression(
        String language,        String bodies    ) {
        super(
        );
        this.language = language;
        this.bodies = bodies;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getBodies() {
        return bodies;
    }

    public void setBodies(String bodies) {
        this.bodies = bodies;
    }

    public UML2_Behavior getUml2_behavior() {
        return uml2_behavior;
    }

    public void setUml2_behavior(UML2_Behavior uml2_behavior) {
        this.uml2_behavior = uml2_behavior;
    }

}