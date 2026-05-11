





import java.util.List;
import java.util.ArrayList;

public class bpmn2_DataState extends BaseElement {

    private String name;





    private bpmn2_ItemAwareElement bpmn2_itemawareelement;


    public bpmn2_DataState(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_ItemAwareElement getBpmn2_itemawareelement() {
        return bpmn2_itemawareelement;
    }

    public void setBpmn2_itemawareelement(bpmn2_ItemAwareElement bpmn2_itemawareelement) {
        this.bpmn2_itemawareelement = bpmn2_itemawareelement;
    }

}