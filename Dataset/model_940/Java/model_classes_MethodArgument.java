





import java.util.List;
import java.util.ArrayList;

public class model_classes_MethodArgument extends UnicaseModelElement {

    private String type;
    private String signature;
    private String label;
    private String defaultValue;
    private String direction;



    public model_classes_MethodArgument(
        String type,        String signature,        String label,        String defaultValue,        String direction    ) {
        super(
        );
        this.type = type;
        this.signature = signature;
        this.label = label;
        this.defaultValue = defaultValue;
        this.direction = direction;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}