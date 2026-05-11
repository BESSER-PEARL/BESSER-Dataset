





import java.util.List;
import java.util.ArrayList;

public class model_Annotation extends OnoObject {

    private String key;
    private String value;





    private model_TMCLConstruct model_tmclconstruct;


    public model_Annotation(
        String key,        String value    ) {
        super(
        );
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public model_TMCLConstruct getModel_tmclconstruct() {
        return model_tmclconstruct;
    }

    public void setModel_tmclconstruct(model_TMCLConstruct model_tmclconstruct) {
        this.model_tmclconstruct = model_tmclconstruct;
    }

}