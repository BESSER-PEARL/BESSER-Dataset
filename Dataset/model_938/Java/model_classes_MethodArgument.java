





import java.util.List;
import java.util.ArrayList;

public class model_classes_MethodArgument extends UnicaseModelElement {

    private String signature;
    private String defaultValue;
    private String label;
    private String direction;
    private String type;



    public model_classes_MethodArgument(
        String signature,        String defaultValue,        String label,        String direction,        String type    ) {
        super(
        );
        this.signature = signature;
        this.defaultValue = defaultValue;
        this.label = label;
        this.direction = direction;
        this.type = type;
    }


    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}