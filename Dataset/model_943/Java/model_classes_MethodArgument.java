





import java.util.List;
import java.util.ArrayList;

public class model_classes_MethodArgument extends UnicaseModelElement {

    private String direction;
    private String label;
    private String type;
    private String defaultValue;
    private String signature;



    public model_classes_MethodArgument(
        String direction,        String label,        String type,        String defaultValue,        String signature    ) {
        super(
        );
        this.direction = direction;
        this.label = label;
        this.type = type;
        this.defaultValue = defaultValue;
        this.signature = signature;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }


}