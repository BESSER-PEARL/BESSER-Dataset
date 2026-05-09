





import java.util.List;
import java.util.ArrayList;

public class UML2_OpaqueExpression extends ValueSpecification {

    private String language;
    private String bodies;





    private UML2_Lifeline uml2_lifeline;




    private UML2_Abstraction uml2_abstraction;




    private UML2_Parameter uml2_parameter;




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

    public UML2_Lifeline getUml2_lifeline() {
        return uml2_lifeline;
    }

    public void setUml2_lifeline(UML2_Lifeline uml2_lifeline) {
        this.uml2_lifeline = uml2_lifeline;
    }
    public UML2_Abstraction getUml2_abstraction() {
        return uml2_abstraction;
    }

    public void setUml2_abstraction(UML2_Abstraction uml2_abstraction) {
        this.uml2_abstraction = uml2_abstraction;
    }
    public UML2_Parameter getUml2_parameter() {
        return uml2_parameter;
    }

    public void setUml2_parameter(UML2_Parameter uml2_parameter) {
        this.uml2_parameter = uml2_parameter;
    }
    public UML2_Behavior getUml2_behavior() {
        return uml2_behavior;
    }

    public void setUml2_behavior(UML2_Behavior uml2_behavior) {
        this.uml2_behavior = uml2_behavior;
    }

}