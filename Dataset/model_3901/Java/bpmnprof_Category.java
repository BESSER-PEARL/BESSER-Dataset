





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_Category extends RootElement {






    private List<bpmnprof_CategoryValue> bpmnprof_categoryvalues;


    public bpmnprof_Category(
    ) {
        super(
        );
        this.bpmnprof_categoryvalues = new ArrayList<>();
    }

    public bpmnprof_Category(
        ArrayList<bpmnprof_CategoryValue> bpmnprof_categoryvalues    ) {
        this.bpmnprof_categoryvalues = bpmnprof_categoryvalues;
    }


    public List<bpmnprof_CategoryValue> getBpmnprof_categoryvalues() {
        return bpmnprof_categoryvalues;
    }

    public void addBpmnprof_categoryvalue(Bpmnprof_categoryvalue bpmnprof_categoryvalue) {
        this.bpmnprof_categoryvalues.add(bpmnprof_categoryvalue);
    }

}