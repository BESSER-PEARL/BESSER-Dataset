





import java.util.List;
import java.util.ArrayList;

public class model_testspecification_ParameterAssignment extends IContentElement {

    private String value;
    private String condition;



    public model_testspecification_ParameterAssignment(
        String value,        String condition    ) {
        super(
        );
        this.value = value;
        this.condition = condition;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }


}