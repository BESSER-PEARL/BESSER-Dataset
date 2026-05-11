





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Category extends RootElement {

    private String name;





    private List<BPMN2Model_CategoryValue> bpmn2model_categoryvalues;


    public BPMN2Model_Category(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2model_categoryvalues = new ArrayList<>();
    }

    public BPMN2Model_Category(
        String name        ArrayList<BPMN2Model_CategoryValue> bpmn2model_categoryvalues    ) {
        this.name = name;
        this.bpmn2model_categoryvalues = bpmn2model_categoryvalues;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<BPMN2Model_CategoryValue> getBpmn2model_categoryvalues() {
        return bpmn2model_categoryvalues;
    }

    public void addBpmn2model_categoryvalue(Bpmn2model_categoryvalue bpmn2model_categoryvalue) {
        this.bpmn2model_categoryvalues.add(bpmn2model_categoryvalue);
    }

}