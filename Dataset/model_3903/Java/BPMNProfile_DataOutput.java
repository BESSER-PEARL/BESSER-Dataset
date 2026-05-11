





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_DataOutput extends ItemAwareElement {

    private String isCollection;





    private BPMNProfile_OutputSet bpmnprofile_outputset;




    private List<BPMNProfile_OutputSet> bpmnprofile_outputsets;




    private List<BPMNProfile_OutputSet> bpmnprofile_outputsets;




    private BPMNProfile_OutputSet bpmnprofile_outputset;




    private BPMNProfile_InputOutputSpecification bpmnprofile_inputoutputspecification;




    private BPMNProfile_OutputSet bpmnprofile_outputset;




    private BPMNProfile_MultiInstanceLoopCharacteristics bpmnprofile_multiinstanceloopcharacteristics;




    private List<BPMNProfile_OutputSet> bpmnprofile_outputsets;


    public BPMNProfile_DataOutput(
        String isCollection    ) {
        super(
        );
        this.isCollection = isCollection;
        this.bpmnprofile_outputsets = new ArrayList<>();
        this.bpmnprofile_outputsets = new ArrayList<>();
        this.bpmnprofile_outputsets = new ArrayList<>();
    }

    public BPMNProfile_DataOutput(
        String isCollection        ArrayList<BPMNProfile_OutputSet> bpmnprofile_outputsets,        ArrayList<BPMNProfile_OutputSet> bpmnprofile_outputsets,        ArrayList<BPMNProfile_OutputSet> bpmnprofile_outputsets    ) {
        this.isCollection = isCollection;
        this.bpmnprofile_outputsets = bpmnprofile_outputsets;
        this.bpmnprofile_outputsets = bpmnprofile_outputsets;
        this.bpmnprofile_outputsets = bpmnprofile_outputsets;
    }

    public String getIscollection() {
        return isCollection;
    }

    public void setIscollection(String isCollection) {
        this.isCollection = isCollection;
    }

    public BPMNProfile_OutputSet getBpmnprofile_outputset() {
        return bpmnprofile_outputset;
    }

    public void setBpmnprofile_outputset(BPMNProfile_OutputSet bpmnprofile_outputset) {
        this.bpmnprofile_outputset = bpmnprofile_outputset;
    }
    public List<BPMNProfile_OutputSet> getBpmnprofile_outputsets() {
        return bpmnprofile_outputsets;
    }

    public void addBpmnprofile_outputset(Bpmnprofile_outputset bpmnprofile_outputset) {
        this.bpmnprofile_outputsets.add(bpmnprofile_outputset);
    }
    public List<BPMNProfile_OutputSet> getBpmnprofile_outputsets() {
        return bpmnprofile_outputsets;
    }

    public void addBpmnprofile_outputset(Bpmnprofile_outputset bpmnprofile_outputset) {
        this.bpmnprofile_outputsets.add(bpmnprofile_outputset);
    }
    public BPMNProfile_OutputSet getBpmnprofile_outputset() {
        return bpmnprofile_outputset;
    }

    public void setBpmnprofile_outputset(BPMNProfile_OutputSet bpmnprofile_outputset) {
        this.bpmnprofile_outputset = bpmnprofile_outputset;
    }
    public BPMNProfile_InputOutputSpecification getBpmnprofile_inputoutputspecification() {
        return bpmnprofile_inputoutputspecification;
    }

    public void setBpmnprofile_inputoutputspecification(BPMNProfile_InputOutputSpecification bpmnprofile_inputoutputspecification) {
        this.bpmnprofile_inputoutputspecification = bpmnprofile_inputoutputspecification;
    }
    public BPMNProfile_OutputSet getBpmnprofile_outputset() {
        return bpmnprofile_outputset;
    }

    public void setBpmnprofile_outputset(BPMNProfile_OutputSet bpmnprofile_outputset) {
        this.bpmnprofile_outputset = bpmnprofile_outputset;
    }
    public BPMNProfile_MultiInstanceLoopCharacteristics getBpmnprofile_multiinstanceloopcharacteristics() {
        return bpmnprofile_multiinstanceloopcharacteristics;
    }

    public void setBpmnprofile_multiinstanceloopcharacteristics(BPMNProfile_MultiInstanceLoopCharacteristics bpmnprofile_multiinstanceloopcharacteristics) {
        this.bpmnprofile_multiinstanceloopcharacteristics = bpmnprofile_multiinstanceloopcharacteristics;
    }
    public List<BPMNProfile_OutputSet> getBpmnprofile_outputsets() {
        return bpmnprofile_outputsets;
    }

    public void addBpmnprofile_outputset(Bpmnprofile_outputset bpmnprofile_outputset) {
        this.bpmnprofile_outputsets.add(bpmnprofile_outputset);
    }

}