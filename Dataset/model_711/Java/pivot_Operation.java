





import java.util.List;
import java.util.ArrayList;

public class pivot_Operation extends Namespace, TemplateableElement, Feature, ParameterableElement {

    private String isInvalidating;
    private String isValidating;





    private pivot_Class pivot_class;




    private pivot_MessageType pivot_messagetype;




    private pivot_Operation pivot_operation;


    public pivot_Operation(
        String isInvalidating,        String isValidating    ) {
        super(
        );
        this.isInvalidating = isInvalidating;
        this.isValidating = isValidating;
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

    public pivot_Class getPivot_class() {
        return pivot_class;
    }

    public void setPivot_class(pivot_Class pivot_class) {
        this.pivot_class = pivot_class;
    }
    public pivot_MessageType getPivot_messagetype() {
        return pivot_messagetype;
    }

    public void setPivot_messagetype(pivot_MessageType pivot_messagetype) {
        this.pivot_messagetype = pivot_messagetype;
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }

}