





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_InputSet extends BaseElement {

    private String name;





    private List<BPMN2Model_OutputSet> bpmn2model_outputsets;




    private BPMN2Model_ThrowEvent bpmn2model_throwevent;




    private BPMN2Model_OutputSet bpmn2model_outputset;


    public BPMN2Model_InputSet(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2model_outputsets = new ArrayList<>();
    }

    public BPMN2Model_InputSet(
        String name        ArrayList<BPMN2Model_OutputSet> bpmn2model_outputsets    ) {
        this.name = name;
        this.bpmn2model_outputsets = bpmn2model_outputsets;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<BPMN2Model_OutputSet> getBpmn2model_outputsets() {
        return bpmn2model_outputsets;
    }

    public void addBpmn2model_outputset(Bpmn2model_outputset bpmn2model_outputset) {
        this.bpmn2model_outputsets.add(bpmn2model_outputset);
    }
    public BPMN2Model_ThrowEvent getBpmn2model_throwevent() {
        return bpmn2model_throwevent;
    }

    public void setBpmn2model_throwevent(BPMN2Model_ThrowEvent bpmn2model_throwevent) {
        this.bpmn2model_throwevent = bpmn2model_throwevent;
    }
    public BPMN2Model_OutputSet getBpmn2model_outputset() {
        return bpmn2model_outputset;
    }

    public void setBpmn2model_outputset(BPMN2Model_OutputSet bpmn2model_outputset) {
        this.bpmn2model_outputset = bpmn2model_outputset;
    }

}