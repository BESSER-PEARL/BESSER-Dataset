





import java.util.List;
import java.util.ArrayList;

public class pivot_Operation extends TemplateableElement, Namespace, ParameterableElement, Feature {

    private String isInvalidating;
    private String isValidating;





    private List<pivot_Parameter> pivot_parameters;




    private pivot_MessageType pivot_messagetype;




    private pivot_Parameter pivot_parameter;




    private pivot_Precedence pivot_precedence;




    private pivot_OperationCallExp pivot_operationcallexp;




    private pivot_OpaqueExpression pivot_opaqueexpression;




    private List<pivot_Operation> pivot_operations;


    public pivot_Operation(
        String isInvalidating,        String isValidating    ) {
        super(
        );
        this.isInvalidating = isInvalidating;
        this.isValidating = isValidating;
        this.pivot_parameters = new ArrayList<>();
        this.pivot_operations = new ArrayList<>();
    }

    public pivot_Operation(
        String isInvalidating,        String isValidating        ArrayList<pivot_Parameter> pivot_parameters,        ArrayList<pivot_Operation> pivot_operations    ) {
        this.isInvalidating = isInvalidating;
        this.isValidating = isValidating;
        this.pivot_parameters = pivot_parameters;
        this.pivot_operations = pivot_operations;
    }

    public String getIsinvalidating() {
        return isInvalidating;
    }

    public void setIsinvalidating(String isInvalidating) {
        this.isInvalidating = isInvalidating;
    }
    public String getIsvalidating() {
        return isValidating;
    }

    public void setIsvalidating(String isValidating) {
        this.isValidating = isValidating;
    }

    public List<pivot_Parameter> getPivot_parameters() {
        return pivot_parameters;
    }

    public void addPivot_parameter(Pivot_parameter pivot_parameter) {
        this.pivot_parameters.add(pivot_parameter);
    }
    public pivot_MessageType getPivot_messagetype() {
        return pivot_messagetype;
    }

    public void setPivot_messagetype(pivot_MessageType pivot_messagetype) {
        this.pivot_messagetype = pivot_messagetype;
    }
    public pivot_Parameter getPivot_parameter() {
        return pivot_parameter;
    }

    public void setPivot_parameter(pivot_Parameter pivot_parameter) {
        this.pivot_parameter = pivot_parameter;
    }
    public pivot_Precedence getPivot_precedence() {
        return pivot_precedence;
    }

    public void setPivot_precedence(pivot_Precedence pivot_precedence) {
        this.pivot_precedence = pivot_precedence;
    }
    public pivot_OperationCallExp getPivot_operationcallexp() {
        return pivot_operationcallexp;
    }

    public void setPivot_operationcallexp(pivot_OperationCallExp pivot_operationcallexp) {
        this.pivot_operationcallexp = pivot_operationcallexp;
    }
    public pivot_OpaqueExpression getPivot_opaqueexpression() {
        return pivot_opaqueexpression;
    }

    public void setPivot_opaqueexpression(pivot_OpaqueExpression pivot_opaqueexpression) {
        this.pivot_opaqueexpression = pivot_opaqueexpression;
    }
    public List<pivot_Operation> getPivot_operations() {
        return pivot_operations;
    }

    public void addPivot_operation(Pivot_operation pivot_operation) {
        this.pivot_operations.add(pivot_operation);
    }

}