





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_OpaqueExpression extends ValueSpecification {

    private String bodies;
    private String language;





    private UML2WithID_Lifeline uml2withid_lifeline;




    private UML2WithID_Abstraction uml2withid_abstraction;




    private UML2WithID_Parameter uml2withid_parameter;




    private UML2WithID_Behavior uml2withid_behavior;


    public UML2WithID_OpaqueExpression(
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

    public UML2WithID_Lifeline getUml2withid_lifeline() {
        return uml2withid_lifeline;
    }

    public void setUml2withid_lifeline(UML2WithID_Lifeline uml2withid_lifeline) {
        this.uml2withid_lifeline = uml2withid_lifeline;
    }
    public UML2WithID_Abstraction getUml2withid_abstraction() {
        return uml2withid_abstraction;
    }

    public void setUml2withid_abstraction(UML2WithID_Abstraction uml2withid_abstraction) {
        this.uml2withid_abstraction = uml2withid_abstraction;
    }
    public UML2WithID_Parameter getUml2withid_parameter() {
        return uml2withid_parameter;
    }

    public void setUml2withid_parameter(UML2WithID_Parameter uml2withid_parameter) {
        this.uml2withid_parameter = uml2withid_parameter;
    }
    public UML2WithID_Behavior getUml2withid_behavior() {
        return uml2withid_behavior;
    }

    public void setUml2withid_behavior(UML2WithID_Behavior uml2withid_behavior) {
        this.uml2withid_behavior = uml2withid_behavior;
    }

}