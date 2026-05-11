





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_DataInput extends ItemAwareElement {

    private boolean isCollection;
    private String name;





    private BPMN2Model_InputSet bpmn2model_inputset;




    private BPMN2Model_ThrowEvent bpmn2model_throwevent;




    private List<BPMN2Model_InputSet> bpmn2model_inputsets;




    private BPMN2Model_MultiInstanceLoopCharacteristics bpmn2model_multiinstanceloopcharacteristics;




    private BPMN2Model_InputOutputSpecification bpmn2model_inputoutputspecification;




    private BPMN2Model_InputSet bpmn2model_inputset;




    private BPMN2Model_InputSet bpmn2model_inputset;




    private List<BPMN2Model_InputSet> bpmn2model_inputsets;




    private List<BPMN2Model_InputSet> bpmn2model_inputsets;


    public BPMN2Model_DataInput(
        boolean isCollection,        String name    ) {
        super(
        );
        this.isCollection = isCollection;
        this.name = name;
        this.bpmn2model_inputsets = new ArrayList<>();
        this.bpmn2model_inputsets = new ArrayList<>();
        this.bpmn2model_inputsets = new ArrayList<>();
    }

    public BPMN2Model_DataInput(
        boolean isCollection,        String name        ArrayList<BPMN2Model_InputSet> bpmn2model_inputsets,        ArrayList<BPMN2Model_InputSet> bpmn2model_inputsets,        ArrayList<BPMN2Model_InputSet> bpmn2model_inputsets    ) {
        this.isCollection = isCollection;
        this.name = name;
        this.bpmn2model_inputsets = bpmn2model_inputsets;
        this.bpmn2model_inputsets = bpmn2model_inputsets;
        this.bpmn2model_inputsets = bpmn2model_inputsets;
    }

    public boolean getIscollection() {
        return isCollection;
    }

    public void setIscollection(boolean isCollection) {
        this.isCollection = isCollection;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public BPMN2Model_InputSet getBpmn2model_inputset() {
        return bpmn2model_inputset;
    }

    public void setBpmn2model_inputset(BPMN2Model_InputSet bpmn2model_inputset) {
        this.bpmn2model_inputset = bpmn2model_inputset;
    }
    public BPMN2Model_ThrowEvent getBpmn2model_throwevent() {
        return bpmn2model_throwevent;
    }

    public void setBpmn2model_throwevent(BPMN2Model_ThrowEvent bpmn2model_throwevent) {
        this.bpmn2model_throwevent = bpmn2model_throwevent;
    }
    public List<BPMN2Model_InputSet> getBpmn2model_inputsets() {
        return bpmn2model_inputsets;
    }

    public void addBpmn2model_inputset(Bpmn2model_inputset bpmn2model_inputset) {
        this.bpmn2model_inputsets.add(bpmn2model_inputset);
    }
    public BPMN2Model_MultiInstanceLoopCharacteristics getBpmn2model_multiinstanceloopcharacteristics() {
        return bpmn2model_multiinstanceloopcharacteristics;
    }

    public void setBpmn2model_multiinstanceloopcharacteristics(BPMN2Model_MultiInstanceLoopCharacteristics bpmn2model_multiinstanceloopcharacteristics) {
        this.bpmn2model_multiinstanceloopcharacteristics = bpmn2model_multiinstanceloopcharacteristics;
    }
    public BPMN2Model_InputOutputSpecification getBpmn2model_inputoutputspecification() {
        return bpmn2model_inputoutputspecification;
    }

    public void setBpmn2model_inputoutputspecification(BPMN2Model_InputOutputSpecification bpmn2model_inputoutputspecification) {
        this.bpmn2model_inputoutputspecification = bpmn2model_inputoutputspecification;
    }
    public BPMN2Model_InputSet getBpmn2model_inputset() {
        return bpmn2model_inputset;
    }

    public void setBpmn2model_inputset(BPMN2Model_InputSet bpmn2model_inputset) {
        this.bpmn2model_inputset = bpmn2model_inputset;
    }
    public BPMN2Model_InputSet getBpmn2model_inputset() {
        return bpmn2model_inputset;
    }

    public void setBpmn2model_inputset(BPMN2Model_InputSet bpmn2model_inputset) {
        this.bpmn2model_inputset = bpmn2model_inputset;
    }
    public List<BPMN2Model_InputSet> getBpmn2model_inputsets() {
        return bpmn2model_inputsets;
    }

    public void addBpmn2model_inputset(Bpmn2model_inputset bpmn2model_inputset) {
        this.bpmn2model_inputsets.add(bpmn2model_inputset);
    }
    public List<BPMN2Model_InputSet> getBpmn2model_inputsets() {
        return bpmn2model_inputsets;
    }

    public void addBpmn2model_inputset(Bpmn2model_inputset bpmn2model_inputset) {
        this.bpmn2model_inputsets.add(bpmn2model_inputset);
    }

}