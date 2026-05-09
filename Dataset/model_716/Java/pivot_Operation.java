





import java.util.List;
import java.util.ArrayList;

public class pivot_Operation extends Namespace, Feature, TemplateableElement {

    private String isTypeof;
    private String isInvalidating;
    private String isValidating;





    private pivot_Operation pivot_operation;




    private pivot_OperationCallExp pivot_operationcallexp;




    private pivot_MessageType pivot_messagetype;


    public pivot_Operation(
        String isTypeof,        String isInvalidating,        String isValidating    ) {
        super(
        );
        this.isTypeof = isTypeof;
        this.isInvalidating = isInvalidating;
        this.isValidating = isValidating;
    }


    public String getIstypeof() {
        return isTypeof;
    }

    public void setIstypeof(String isTypeof) {
        this.isTypeof = isTypeof;
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

    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }
    public pivot_OperationCallExp getPivot_operationcallexp() {
        return pivot_operationcallexp;
    }

    public void setPivot_operationcallexp(pivot_OperationCallExp pivot_operationcallexp) {
        this.pivot_operationcallexp = pivot_operationcallexp;
    }
    public pivot_MessageType getPivot_messagetype() {
        return pivot_messagetype;
    }

    public void setPivot_messagetype(pivot_MessageType pivot_messagetype) {
        this.pivot_messagetype = pivot_messagetype;
    }

}