





import java.util.List;
import java.util.ArrayList;

public class model_classes_MethodArgument extends UnicaseModelElement {

    private String label;
    private String signature;
    private String direction;
    private String defaultValue;
    private String type;



    public model_classes_MethodArgument(
        String label,        String signature,        String direction,        String defaultValue,        String type    ) {
        super(
        );
        this.label = label;
        this.signature = signature;
        this.direction = direction;
        this.defaultValue = defaultValue;
        this.type = type;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}