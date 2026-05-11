





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_DataInput extends ItemAwareElement {

    private String isCollection;





    private bpmnprof_InputSet bpmnprof_inputset;




    private List<bpmnprof_InputSet> bpmnprof_inputsets;




    private bpmnprof_InputSet bpmnprof_inputset;




    private bpmnprof_InputOutputSpecification bpmnprof_inputoutputspecification;




    private List<bpmnprof_InputSet> bpmnprof_inputsets;




    private List<bpmnprof_InputSet> bpmnprof_inputsets;




    private bpmnprof_MultiInstanceLoopCharacteristics bpmnprof_multiinstanceloopcharacteristics;




    private bpmnprof_InputSet bpmnprof_inputset;


    public bpmnprof_DataInput(
        String isCollection    ) {
        super(
        );
        this.isCollection = isCollection;
        this.bpmnprof_inputsets = new ArrayList<>();
        this.bpmnprof_inputsets = new ArrayList<>();
        this.bpmnprof_inputsets = new ArrayList<>();
    }

    public bpmnprof_DataInput(
        String isCollection        ArrayList<bpmnprof_InputSet> bpmnprof_inputsets,        ArrayList<bpmnprof_InputSet> bpmnprof_inputsets,        ArrayList<bpmnprof_InputSet> bpmnprof_inputsets    ) {
        this.isCollection = isCollection;
        this.bpmnprof_inputsets = bpmnprof_inputsets;
        this.bpmnprof_inputsets = bpmnprof_inputsets;
        this.bpmnprof_inputsets = bpmnprof_inputsets;
    }

    public String getIscollection() {
        return isCollection;
    }

    public void setIscollection(String isCollection) {
        this.isCollection = isCollection;
    }

    public bpmnprof_InputSet getBpmnprof_inputset() {
        return bpmnprof_inputset;
    }

    public void setBpmnprof_inputset(bpmnprof_InputSet bpmnprof_inputset) {
        this.bpmnprof_inputset = bpmnprof_inputset;
    }
    public List<bpmnprof_InputSet> getBpmnprof_inputsets() {
        return bpmnprof_inputsets;
    }

    public void addBpmnprof_inputset(Bpmnprof_inputset bpmnprof_inputset) {
        this.bpmnprof_inputsets.add(bpmnprof_inputset);
    }
    public bpmnprof_InputSet getBpmnprof_inputset() {
        return bpmnprof_inputset;
    }

    public void setBpmnprof_inputset(bpmnprof_InputSet bpmnprof_inputset) {
        this.bpmnprof_inputset = bpmnprof_inputset;
    }
    public bpmnprof_InputOutputSpecification getBpmnprof_inputoutputspecification() {
        return bpmnprof_inputoutputspecification;
    }

    public void setBpmnprof_inputoutputspecification(bpmnprof_InputOutputSpecification bpmnprof_inputoutputspecification) {
        this.bpmnprof_inputoutputspecification = bpmnprof_inputoutputspecification;
    }
    public List<bpmnprof_InputSet> getBpmnprof_inputsets() {
        return bpmnprof_inputsets;
    }

    public void addBpmnprof_inputset(Bpmnprof_inputset bpmnprof_inputset) {
        this.bpmnprof_inputsets.add(bpmnprof_inputset);
    }
    public List<bpmnprof_InputSet> getBpmnprof_inputsets() {
        return bpmnprof_inputsets;
    }

    public void addBpmnprof_inputset(Bpmnprof_inputset bpmnprof_inputset) {
        this.bpmnprof_inputsets.add(bpmnprof_inputset);
    }
    public bpmnprof_MultiInstanceLoopCharacteristics getBpmnprof_multiinstanceloopcharacteristics() {
        return bpmnprof_multiinstanceloopcharacteristics;
    }

    public void setBpmnprof_multiinstanceloopcharacteristics(bpmnprof_MultiInstanceLoopCharacteristics bpmnprof_multiinstanceloopcharacteristics) {
        this.bpmnprof_multiinstanceloopcharacteristics = bpmnprof_multiinstanceloopcharacteristics;
    }
    public bpmnprof_InputSet getBpmnprof_inputset() {
        return bpmnprof_inputset;
    }

    public void setBpmnprof_inputset(bpmnprof_InputSet bpmnprof_inputset) {
        this.bpmnprof_inputset = bpmnprof_inputset;
    }

}