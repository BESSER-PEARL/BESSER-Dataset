





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_DataOutput extends ItemAwareElement {

    private String isCollection;





    private bpmnprof_OutputSet bpmnprof_outputset;




    private List<bpmnprof_OutputSet> bpmnprof_outputsets;




    private List<bpmnprof_OutputSet> bpmnprof_outputsets;




    private bpmnprof_OutputSet bpmnprof_outputset;




    private bpmnprof_InputOutputSpecification bpmnprof_inputoutputspecification;




    private bpmnprof_MultiInstanceLoopCharacteristics bpmnprof_multiinstanceloopcharacteristics;




    private bpmnprof_OutputSet bpmnprof_outputset;




    private List<bpmnprof_OutputSet> bpmnprof_outputsets;


    public bpmnprof_DataOutput(
        String isCollection    ) {
        super(
        );
        this.isCollection = isCollection;
        this.bpmnprof_outputsets = new ArrayList<>();
        this.bpmnprof_outputsets = new ArrayList<>();
        this.bpmnprof_outputsets = new ArrayList<>();
    }

    public bpmnprof_DataOutput(
        String isCollection        ArrayList<bpmnprof_OutputSet> bpmnprof_outputsets,        ArrayList<bpmnprof_OutputSet> bpmnprof_outputsets,        ArrayList<bpmnprof_OutputSet> bpmnprof_outputsets    ) {
        this.isCollection = isCollection;
        this.bpmnprof_outputsets = bpmnprof_outputsets;
        this.bpmnprof_outputsets = bpmnprof_outputsets;
        this.bpmnprof_outputsets = bpmnprof_outputsets;
    }

    public String getIscollection() {
        return isCollection;
    }

    public void setIscollection(String isCollection) {
        this.isCollection = isCollection;
    }

    public bpmnprof_OutputSet getBpmnprof_outputset() {
        return bpmnprof_outputset;
    }

    public void setBpmnprof_outputset(bpmnprof_OutputSet bpmnprof_outputset) {
        this.bpmnprof_outputset = bpmnprof_outputset;
    }
    public List<bpmnprof_OutputSet> getBpmnprof_outputsets() {
        return bpmnprof_outputsets;
    }

    public void addBpmnprof_outputset(Bpmnprof_outputset bpmnprof_outputset) {
        this.bpmnprof_outputsets.add(bpmnprof_outputset);
    }
    public List<bpmnprof_OutputSet> getBpmnprof_outputsets() {
        return bpmnprof_outputsets;
    }

    public void addBpmnprof_outputset(Bpmnprof_outputset bpmnprof_outputset) {
        this.bpmnprof_outputsets.add(bpmnprof_outputset);
    }
    public bpmnprof_OutputSet getBpmnprof_outputset() {
        return bpmnprof_outputset;
    }

    public void setBpmnprof_outputset(bpmnprof_OutputSet bpmnprof_outputset) {
        this.bpmnprof_outputset = bpmnprof_outputset;
    }
    public bpmnprof_InputOutputSpecification getBpmnprof_inputoutputspecification() {
        return bpmnprof_inputoutputspecification;
    }

    public void setBpmnprof_inputoutputspecification(bpmnprof_InputOutputSpecification bpmnprof_inputoutputspecification) {
        this.bpmnprof_inputoutputspecification = bpmnprof_inputoutputspecification;
    }
    public bpmnprof_MultiInstanceLoopCharacteristics getBpmnprof_multiinstanceloopcharacteristics() {
        return bpmnprof_multiinstanceloopcharacteristics;
    }

    public void setBpmnprof_multiinstanceloopcharacteristics(bpmnprof_MultiInstanceLoopCharacteristics bpmnprof_multiinstanceloopcharacteristics) {
        this.bpmnprof_multiinstanceloopcharacteristics = bpmnprof_multiinstanceloopcharacteristics;
    }
    public bpmnprof_OutputSet getBpmnprof_outputset() {
        return bpmnprof_outputset;
    }

    public void setBpmnprof_outputset(bpmnprof_OutputSet bpmnprof_outputset) {
        this.bpmnprof_outputset = bpmnprof_outputset;
    }
    public List<bpmnprof_OutputSet> getBpmnprof_outputsets() {
        return bpmnprof_outputsets;
    }

    public void addBpmnprof_outputset(Bpmnprof_outputset bpmnprof_outputset) {
        this.bpmnprof_outputsets.add(bpmnprof_outputset);
    }

}