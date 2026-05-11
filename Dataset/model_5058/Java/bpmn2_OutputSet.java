





import java.util.List;
import java.util.ArrayList;

public class bpmn2_OutputSet extends BaseElement {

    private String name;





    private bpmn2_InputSet bpmn2_inputset;




    private bpmn2_InputOutputSpecification bpmn2_inputoutputspecification;




    private List<bpmn2_InputSet> bpmn2_inputsets;


    public bpmn2_OutputSet(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_inputsets = new ArrayList<>();
    }

    public bpmn2_OutputSet(
        String name        ArrayList<bpmn2_InputSet> bpmn2_inputsets    ) {
        this.name = name;
        this.bpmn2_inputsets = bpmn2_inputsets;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_InputSet getBpmn2_inputset() {
        return bpmn2_inputset;
    }

    public void setBpmn2_inputset(bpmn2_InputSet bpmn2_inputset) {
        this.bpmn2_inputset = bpmn2_inputset;
    }
    public bpmn2_InputOutputSpecification getBpmn2_inputoutputspecification() {
        return bpmn2_inputoutputspecification;
    }

    public void setBpmn2_inputoutputspecification(bpmn2_InputOutputSpecification bpmn2_inputoutputspecification) {
        this.bpmn2_inputoutputspecification = bpmn2_inputoutputspecification;
    }
    public List<bpmn2_InputSet> getBpmn2_inputsets() {
        return bpmn2_inputsets;
    }

    public void addBpmn2_inputset(Bpmn2_inputset bpmn2_inputset) {
        this.bpmn2_inputsets.add(bpmn2_inputset);
    }

}