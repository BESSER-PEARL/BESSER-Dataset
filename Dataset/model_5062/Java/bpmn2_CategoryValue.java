





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CategoryValue extends BaseElement {

    private String value;





    private bpmn2_Category bpmn2_category;


    public bpmn2_CategoryValue(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public bpmn2_Category getBpmn2_category() {
        return bpmn2_category;
    }

    public void setBpmn2_category(bpmn2_Category bpmn2_category) {
        this.bpmn2_category = bpmn2_category;
    }

}