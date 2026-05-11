





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_DataOutput extends ItemAwareElement {

    private String name;
    private boolean isCollection;





    private List<BPMN2Model_OutputSet> bpmn2model_outputsets;




    private BPMN2Model_OutputSet bpmn2model_outputset;




    private BPMN2Model_InputOutputSpecification bpmn2model_inputoutputspecification;




    private BPMN2Model_MultiInstanceLoopCharacteristics bpmn2model_multiinstanceloopcharacteristics;




    private List<BPMN2Model_OutputSet> bpmn2model_outputsets;




    private BPMN2Model_OutputSet bpmn2model_outputset;




    private BPMN2Model_CatchEvent bpmn2model_catchevent;




    private BPMN2Model_OutputSet bpmn2model_outputset;




    private List<BPMN2Model_OutputSet> bpmn2model_outputsets;


    public BPMN2Model_DataOutput(
        String name,        boolean isCollection    ) {
        super(
        );
        this.name = name;
        this.isCollection = isCollection;
        this.bpmn2model_outputsets = new ArrayList<>();
        this.bpmn2model_outputsets = new ArrayList<>();
        this.bpmn2model_outputsets = new ArrayList<>();
    }

    public BPMN2Model_DataOutput(
        String name,        boolean isCollection        ArrayList<BPMN2Model_OutputSet> bpmn2model_outputsets,        ArrayList<BPMN2Model_OutputSet> bpmn2model_outputsets,        ArrayList<BPMN2Model_OutputSet> bpmn2model_outputsets    ) {
        this.name = name;
        this.isCollection = isCollection;
        this.bpmn2model_outputsets = bpmn2model_outputsets;
        this.bpmn2model_outputsets = bpmn2model_outputsets;
        this.bpmn2model_outputsets = bpmn2model_outputsets;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIscollection() {
        return isCollection;
    }

    public void setIscollection(boolean isCollection) {
        this.isCollection = isCollection;
    }

    public List<BPMN2Model_OutputSet> getBpmn2model_outputsets() {
        return bpmn2model_outputsets;
    }

    public void addBpmn2model_outputset(Bpmn2model_outputset bpmn2model_outputset) {
        this.bpmn2model_outputsets.add(bpmn2model_outputset);
    }
    public BPMN2Model_OutputSet getBpmn2model_outputset() {
        return bpmn2model_outputset;
    }

    public void setBpmn2model_outputset(BPMN2Model_OutputSet bpmn2model_outputset) {
        this.bpmn2model_outputset = bpmn2model_outputset;
    }
    public BPMN2Model_InputOutputSpecification getBpmn2model_inputoutputspecification() {
        return bpmn2model_inputoutputspecification;
    }

    public void setBpmn2model_inputoutputspecification(BPMN2Model_InputOutputSpecification bpmn2model_inputoutputspecification) {
        this.bpmn2model_inputoutputspecification = bpmn2model_inputoutputspecification;
    }
    public BPMN2Model_MultiInstanceLoopCharacteristics getBpmn2model_multiinstanceloopcharacteristics() {
        return bpmn2model_multiinstanceloopcharacteristics;
    }

    public void setBpmn2model_multiinstanceloopcharacteristics(BPMN2Model_MultiInstanceLoopCharacteristics bpmn2model_multiinstanceloopcharacteristics) {
        this.bpmn2model_multiinstanceloopcharacteristics = bpmn2model_multiinstanceloopcharacteristics;
    }
    public List<BPMN2Model_OutputSet> getBpmn2model_outputsets() {
        return bpmn2model_outputsets;
    }

    public void addBpmn2model_outputset(Bpmn2model_outputset bpmn2model_outputset) {
        this.bpmn2model_outputsets.add(bpmn2model_outputset);
    }
    public BPMN2Model_OutputSet getBpmn2model_outputset() {
        return bpmn2model_outputset;
    }

    public void setBpmn2model_outputset(BPMN2Model_OutputSet bpmn2model_outputset) {
        this.bpmn2model_outputset = bpmn2model_outputset;
    }
    public BPMN2Model_CatchEvent getBpmn2model_catchevent() {
        return bpmn2model_catchevent;
    }

    public void setBpmn2model_catchevent(BPMN2Model_CatchEvent bpmn2model_catchevent) {
        this.bpmn2model_catchevent = bpmn2model_catchevent;
    }
    public BPMN2Model_OutputSet getBpmn2model_outputset() {
        return bpmn2model_outputset;
    }

    public void setBpmn2model_outputset(BPMN2Model_OutputSet bpmn2model_outputset) {
        this.bpmn2model_outputset = bpmn2model_outputset;
    }
    public List<BPMN2Model_OutputSet> getBpmn2model_outputsets() {
        return bpmn2model_outputsets;
    }

    public void addBpmn2model_outputset(Bpmn2model_outputset bpmn2model_outputset) {
        this.bpmn2model_outputsets.add(bpmn2model_outputset);
    }

}