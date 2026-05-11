





import java.util.List;
import java.util.ArrayList;

public class bpmn2_InputSet extends BaseElement {

    private String name;





    private bpmn2_OutputSet bpmn2_outputset;




    private List<bpmn2_OutputSet> bpmn2_outputsets;




    private bpmn2_InputOutputSpecification bpmn2_inputoutputspecification;




    private bpmn2_ThrowEvent bpmn2_throwevent;


    public bpmn2_InputSet(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_outputsets = new ArrayList<>();
    }

    public bpmn2_InputSet(
        String name        ArrayList<bpmn2_OutputSet> bpmn2_outputsets    ) {
        this.name = name;
        this.bpmn2_outputsets = bpmn2_outputsets;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_OutputSet getBpmn2_outputset() {
        return bpmn2_outputset;
    }

    public void setBpmn2_outputset(bpmn2_OutputSet bpmn2_outputset) {
        this.bpmn2_outputset = bpmn2_outputset;
    }
    public List<bpmn2_OutputSet> getBpmn2_outputsets() {
        return bpmn2_outputsets;
    }

    public void addBpmn2_outputset(Bpmn2_outputset bpmn2_outputset) {
        this.bpmn2_outputsets.add(bpmn2_outputset);
    }
    public bpmn2_InputOutputSpecification getBpmn2_inputoutputspecification() {
        return bpmn2_inputoutputspecification;
    }

    public void setBpmn2_inputoutputspecification(bpmn2_InputOutputSpecification bpmn2_inputoutputspecification) {
        this.bpmn2_inputoutputspecification = bpmn2_inputoutputspecification;
    }
    public bpmn2_ThrowEvent getBpmn2_throwevent() {
        return bpmn2_throwevent;
    }

    public void setBpmn2_throwevent(bpmn2_ThrowEvent bpmn2_throwevent) {
        this.bpmn2_throwevent = bpmn2_throwevent;
    }

}