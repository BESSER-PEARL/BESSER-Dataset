





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Category extends RootElement {

    private String name;





    private List<bpmn2_CategoryValue> bpmn2_categoryvalues;


    public bpmn2_Category(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_categoryvalues = new ArrayList<>();
    }

    public bpmn2_Category(
        String name        ArrayList<bpmn2_CategoryValue> bpmn2_categoryvalues    ) {
        this.name = name;
        this.bpmn2_categoryvalues = bpmn2_categoryvalues;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<bpmn2_CategoryValue> getBpmn2_categoryvalues() {
        return bpmn2_categoryvalues;
    }

    public void addBpmn2_categoryvalue(Bpmn2_categoryvalue bpmn2_categoryvalue) {
        this.bpmn2_categoryvalues.add(bpmn2_categoryvalue);
    }

}