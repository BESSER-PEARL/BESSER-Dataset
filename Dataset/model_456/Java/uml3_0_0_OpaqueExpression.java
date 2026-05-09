





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_OpaqueExpression extends ValueSpecification {

    private String language;
    private String body;





    private uml3_0_0_Parameter uml3_0_0_parameter;




    private uml3_0_0_Behavior uml3_0_0_behavior;




    private uml3_0_0_Abstraction uml3_0_0_abstraction;


    public uml3_0_0_OpaqueExpression(
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

    public uml3_0_0_Parameter getUml3_0_0_parameter() {
        return uml3_0_0_parameter;
    }

    public void setUml3_0_0_parameter(uml3_0_0_Parameter uml3_0_0_parameter) {
        this.uml3_0_0_parameter = uml3_0_0_parameter;
    }
    public uml3_0_0_Behavior getUml3_0_0_behavior() {
        return uml3_0_0_behavior;
    }

    public void setUml3_0_0_behavior(uml3_0_0_Behavior uml3_0_0_behavior) {
        this.uml3_0_0_behavior = uml3_0_0_behavior;
    }
    public uml3_0_0_Abstraction getUml3_0_0_abstraction() {
        return uml3_0_0_abstraction;
    }

    public void setUml3_0_0_abstraction(uml3_0_0_Abstraction uml3_0_0_abstraction) {
        this.uml3_0_0_abstraction = uml3_0_0_abstraction;
    }

}